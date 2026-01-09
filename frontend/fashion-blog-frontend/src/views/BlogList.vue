<template>
  <div class="blog-list">
    <!-- 头部导航 -->
    <div class="blog-header">
      <div class="header-content">
        <h1 class="main-title">时尚博客</h1>
        <p class="subtitle">探索最新的时尚趋势，分享你的穿搭心得</p>
        <div class="search-bar">
          <input 
            v-model="searchQuery" 
            @input="searchPosts"
            type="text" 
            placeholder="搜索时尚灵感..."
            class="search-input"
          >
          <button @click="searchPosts" class="search-btn">
            <i class="icon">🔍</i>
          </button>
        </div>
      </div>
    </div>

    <!-- 内容类型筛选 -->
    <div class="filter-section">
      <div class="filter-container">
        <h2 class="filter-title">内容分类</h2>
        <div class="filter-bar">
          <button 
            v-for="type in contentTypes" 
            :key="type.value"
            @click="filterByType(type.value)"
            :class="['filter-btn', { active: selectedType === type.value }]"
          >
            <span class="filter-icon">{{ getContentTypeIcon(type.value) }}</span>
            <span class="filter-label">{{ type.label }}</span>
          </button>
        </div>
        <router-link to="/blog/create" class="create-btn">
          <i class="icon">✏️</i>
          发布新博客
        </router-link>
      </div>
    </div>

    <!-- 博客文章列表 -->
    <div class="posts-container">
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>加载中...</p>
      </div>
      
      <div v-else-if="filteredPosts.length === 0" class="no-posts">
        <h3>暂无博客文章</h3>
        <p>成为第一个分享时尚见解的人吧！</p>
        <router-link to="/blog/create" class="create-first-btn">
          发布第一篇博客
        </router-link>
      </div>

      <div v-else class="posts-grid">
        <article 
          v-for="post in filteredPosts" 
          :key="post.id" 
          class="post-card"
          @click="goToDetail(post.id)"
        >
          <!-- 文章封面 -->
          <div class="post-cover">
            <div v-if="post.content_type === 'video' && post.video_file" class="media-preview">
              <video :src="post.video_file" class="video-thumbnail" preload="metadata"></video>
              <div class="play-overlay">▶️</div>
            </div>
            
            <div v-else-if="post.content_type === 'image' && post.image_files?.length" class="media-preview">
              <img :src="post.image_files[0].file" :alt="post.title" class="image-thumbnail">
            </div>
            
            <div v-else class="text-cover" :style="getTextCoverStyle(post.id)">
              <div class="text-cover-content">
                <i class="text-icon">📝</i>
                <span class="text-type">{{ getContentTypeLabel(post.content_type) }}</span>
              </div>
            </div>

            <!-- 文章类型标识 -->
            <div class="post-type-badge" :class="post.content_type">
              <span class="badge-icon">{{ getContentTypeIcon(post.content_type) }}</span>
              <span class="badge-label">{{ getContentTypeLabel(post.content_type) }}</span>
            </div>
          </div>

          <!-- 文章内容 -->
          <div class="post-content">
            <div class="post-header">
              <h3 class="post-title">{{ post.title }}</h3>
              <div class="post-meta">
                <div class="author-info">
                  <div class="avatar">{{ post.author.username.charAt(0).toUpperCase() }}</div>
                  <span class="author-name">{{ post.author.username }}</span>
                </div>
                <span class="post-date">{{ formatDate(post.created_at) }}</span>
              </div>
            </div>
            
            <p class="post-excerpt">{{ getExcerpt(post.content) }}</p>
            
            <div class="post-stats">
              <span class="stat">
                <i class="icon">❤️</i>
                {{ post.likes_count }}
              </span>
              <span class="stat">
                <i class="icon">💬</i>
                {{ post.comments_count }}
              </span>
            </div>
          </div>

          <!-- 点赞按钮 -->
          <button 
            v-if="post.liked_by_user" 
            @click.stop="unlikePost(post)" 
            class="like-btn liked"
          >
            ❤️
          </button>
          <button 
            v-else 
            @click.stop="likePost(post)" 
            class="like-btn"
          >
            🤍
          </button>
        </article>
      </div>
    </div>

    <!-- 分页 -->
    <div v-if="totalPages > 1" class="pagination">
      <button 
        @click="previousPage" 
        :disabled="currentPage === 1"
        class="page-btn"
      >
        <i class="icon">←</i>
        上一页
      </button>
      <div class="page-info">
        <span class="current-page">{{ currentPage }}</span>
        <span class="total-pages">/ {{ totalPages }}</span>
      </div>
      <button 
        @click="nextPage" 
        :disabled="currentPage === totalPages"
        class="page-btn"
      >
        下一页
        <i class="icon">→</i>
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'BlogList',
  data() {
    return {
      posts: [
        { id: 1, title: '2027春季时尚趋势解析', content: '2027年春季，时尚界将迎来一场新的革命。从柔和的马卡龙色调到大胆的几何图案，本季节的时尚趋势将为我们带来无限灵感...', content_type: 'text', author: { username: '时尚达人' }, likes_count: 45, comments_count: 12, created_at: '2027-10-15', liked_by_user: false },
        { id: 2, title: '如何搭配春季外套', content: '春季外套是衣橱中的必备单品。本文将为您介绍几种不同风格的春季外套搭配方法，让您在这个春天既时尚又舒适...', content_type: 'text', author: { username: '搭配专家' }, likes_count: 38, comments_count: 8, created_at: '2027-10-10', liked_by_user: true },
        { id: 3, title: '2027年流行色大盘点', content: 'Pantone发布了2027年的年度流行色，这些色彩将在时尚界掀起一股 heats。together来看看这些流行色的魅力...', content_type: 'image', image_files: [{ file: '/images/fashion-color-2027.svg' }], author: { username: '色彩大师' }, likes_count: 62, comments_count: 15, created_at: '2027-10-05', liked_by_user: false },
        { id: 4, title: '必备配饰推荐', content: '配饰是整体造型的点睛之笔。本文将为您推荐几款春季必备的配饰，让您的造型更加完美...', content_type: 'text', author: { username: '配饰专家' }, likes_count: 29, comments_count: 7, created_at: '2027-09-28', liked_by_user: false },
        { id: 5, title: '街头时尚风格解析', content: '街头时尚一直是时尚界的重要组成部分。本文将为您解析2027年街头时尚的最新趋势...', content_type: 'mixed', author: { username: '街头潮人' }, likes_count: 53, comments_count: 11, created_at: '2027-09-20', liked_by_user: true },
        { id: 6, title: '如何选择适合自己的发型', content: '发型是塑造个人形象的重要因素。本文将为您介绍几种不同脸型适合的发型，帮助您找到最适合自己的发型...', content_type: 'text', author: { username: '发型设计师' }, likes_count: 35, comments_count: 9, created_at: '2027-09-15', liked_by_user: false },
        { id: 7, title: '夏季连衣裙搭配指南', content: '夏季是连衣裙的季节。本文将为您介绍几种不同风格的连衣裙搭配方法，让您在这个夏天既凉爽又时尚...', content_type: 'image', image_files: [{ file: '/images/dress-guide.svg' }], author: { username: '时尚博主' }, likes_count: 48, comments_count: 10, created_at: '2027-09-10', liked_by_user: false },
        { id: 8, title: '男士时尚穿搭技巧', content: '男士穿搭同样重要。本文将为您介绍几种不同场合的男士穿搭技巧，让您在任何场合都能展现自己的魅力...', content_type: 'text', author: { username: '男装专家' }, likes_count: 32, comments_count: 6, created_at: '2027-09-05', liked_by_user: true }
      ],
      filteredPosts: [],
      loading: false,
      searchQuery: '',
      selectedType: 'all',
      currentPage: 1,
      totalPages: 1,
      contentTypes: [
        { value: 'all', label: '全部' },
        { value: 'text', label: '文字' },
        { value: 'video', label: '视频' },
        { value: 'image', label: '图片' },
        { value: 'mixed', label: '混合' }
      ],
      coverColors: [
        'linear-gradient(135deg, #ff94d2, #b388eb)',
        'linear-gradient(135deg, #81e6d9, #3182ce)',
        'linear-gradient(135deg, #f6e05e, #fc8181)',
        'linear-gradient(135deg, #667eea, #764ba2)',
        'linear-gradient(135deg, #f093fb, #f5576c)',
        'linear-gradient(135deg, #4facfe, #00f2fe)',
        'linear-gradient(135deg, #43e97b, #38f9d7)',
        'linear-gradient(135deg, #fa709a, #fee140)'
      ]
    };
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      this.loading = true;
      try {
        // 使用本地数据替代API请求
        setTimeout(() => {
          // 应用筛选条件
          let filtered = this.posts;
          
          // 按内容类型筛选
          if (this.selectedType !== 'all') {
            filtered = filtered.filter(post => post.content_type === this.selectedType);
          }
          
          // 按搜索关键词筛选
          if (this.searchQuery) {
            const query = this.searchQuery.toLowerCase();
            filtered = filtered.filter(post => 
              post.title.toLowerCase().includes(query) || 
              post.content.toLowerCase().includes(query)
            );
          }
          
          this.filteredPosts = filtered;
          this.totalPages = Math.ceil(filtered.length / 10);
        }, 500); // 添加延迟模拟加载过程
      } catch (error) {
        console.error('获取博客文章失败:', error);
      } finally {
        this.loading = false;
      }
    },

    async likePost(post) {
      try {
        const response = await axios.post(`/api/posts/${post.id}/like/`);
        post.likes_count = response.data.likes_count;
        post.liked_by_user = response.data.status === 'liked';
      } catch (error) {
        console.error('点赞失败:', error);
        this.$toast?.error('点赞失败，请登录后再试');
      }
    },

    async unlikePost(post) {
      try {
        const response = await axios.post(`/api/posts/${post.id}/like/`);
        post.likes_count = response.data.likes_count;
        post.liked_by_user = response.data.status === 'liked';
      } catch (error) {
        console.error('取消点赞失败:', error);
      }
    },

    searchPosts() {
      this.currentPage = 1;
      this.fetchPosts();
    },

    filterByType(type) {
      this.selectedType = type;
      this.currentPage = 1;
      this.fetchPosts();
    },

    goToDetail(postId) {
      this.$router.push(`/blog/${postId}`);
    },

    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.fetchPosts();
      }
    },

    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
        this.fetchPosts();
      }
    },

    getExcerpt(content, maxLength = 120) {
      if (!content) return '';
      return content.length > maxLength ? content.substring(0, maxLength) + '...' : content;
    },

    getContentTypeLabel(type) {
      const typeMap = {
        'text': '文字',
        'video': '视频',
        'image': '图片',
        'mixed': '混合'
      };
      return typeMap[type] || type;
    },

    getContentTypeIcon(type) {
      const iconMap = {
        'text': '📝',
        'video': '🎬',
        'image': '🖼️',
        'mixed': '✨',
        'all': '📋'
      };
      return iconMap[type] || '📝';
    },

    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },

    getTextCoverStyle(postId) {
      const index = (postId - 1) % this.coverColors.length;
      return {
        background: this.coverColors[index]
      };
    }
  }
};
</script>

<style scoped>
.blog-list {
  min-height: 100vh;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  color: #fff;
  padding: 0;
  margin: 0;
}

/* 头部样式 */
.blog-header {
  background: linear-gradient(135deg, rgba(255, 148, 210, 0.1) 0%, rgba(179, 136, 235, 0.1) 100%);
  backdrop-filter: blur(10px);
  padding: 60px 20px 40px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}

.blog-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="none"/><circle cx="25" cy="25" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="25" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="25" cy="75" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="75" r="2" fill="rgba(255,255,255,0.1)"/></svg>') repeat;
  opacity: 0.3;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
  text-align: center;
}

.main-title {
  font-size: 3.5rem;
  margin-bottom: 15px;
  background: linear-gradient(45deg, #ff94d2, #b388eb, #81e6d9, #f6e05e);
  background-size: 300% 300%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  animation: gradientShift 3s ease infinite;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.subtitle {
  color: #e0e0e0;
  font-size: 1.2rem;
  margin-bottom: 40px;
  font-weight: 300;
  letter-spacing: 1px;
}

.search-bar {
  display: flex;
  justify-content: center;
  gap: 0;
  max-width: 600px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 30px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.search-input {
  flex: 1;
  padding: 18px 25px;
  border: none;
  border-radius: 30px 0 0 30px;
  background: transparent;
  color: #fff;
  font-size: 1rem;
  outline: none;
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.search-btn {
  padding: 18px 25px;
  border: none;
  border-radius: 0 30px 30px 0;
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  color: #fff;
  cursor: pointer;
  font-size: 1.2rem;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-btn:hover {
  background: linear-gradient(45deg, #b388eb, #ff94d2);
  transform: scale(1.05);
}

/* 筛选部分样式 */
.filter-section {
  padding: 30px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.filter-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}

.filter-title {
  font-size: 1.5rem;
  color: #fff;
  margin: 0;
  font-weight: 600;
}

.filter-bar {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 12px 24px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 30px;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 8px;
  backdrop-filter: blur(10px);
}

.filter-btn:hover {
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  border-color: transparent;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(255, 148, 210, 0.3);
}

.filter-btn.active {
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  border-color: transparent;
  box-shadow: 0 8px 25px rgba(255, 148, 210, 0.3);
}

.create-btn {
  padding: 12px 24px;
  border: none;
  border-radius: 30px;
  background: linear-gradient(45deg, #81e6d9, #3182ce);
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  font-weight: 600;
}

.create-btn:hover {
  background: linear-gradient(45deg, #3182ce, #81e6d9);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(129, 230, 217, 0.3);
}

/* 博客文章列表样式 */
.posts-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px 60px;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 300px;
  color: #e0e0e0;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(255, 255, 255, 0.1);
  border-top: 4px solid #ff94d2;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.no-posts {
  text-align: center;
  padding: 80px 20px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.no-posts h3 {
  color: #ffffff;
  margin-bottom: 15px;
  font-size: 1.8rem;
}

.no-posts p {
  color: #e0e0e0;
  margin-bottom: 40px;
  font-size: 1.1rem;
}

.create-first-btn {
  padding: 15px 30px;
  border: none;
  border-radius: 30px;
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  color: #fff;
  cursor: pointer;
  font-size: 1.1rem;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  transition: all 0.3s ease;
  font-weight: 600;
}

.create-first-btn:hover {
  background: linear-gradient(45deg, #b388eb, #ff94d2);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(255, 148, 210, 0.3);
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.post-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 20px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.4s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  position: relative;
}

.post-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 148, 210, 0.3);
}

/* 文章封面样式 */
.post-cover {
  position: relative;
  height: 220px;
  overflow: hidden;
}

.media-preview {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}

.video-thumbnail {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.image-thumbnail {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.post-card:hover .video-thumbnail,
.post-card:hover .image-thumbnail {
  transform: scale(1.08);
}

.text-cover {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  transition: transform 0.4s ease;
}

.text-cover::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  z-index: 1;
}

.text-cover-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  position: relative;
  z-index: 2;
}

.text-icon {
  font-size: 3rem;
  opacity: 0.9;
}

.text-type {
  font-size: 1.1rem;
  font-weight: 600;
  color: #fff;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

.post-card:hover .text-cover {
  transform: scale(1.05);
}

.play-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 4rem;
  color: rgba(255, 255, 255, 0.9);
  background: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: all 0.3s ease;
  cursor: pointer;
}

.media-preview:hover .play-overlay {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1.1);
}

/* 文章类型标识样式 */
.post-type-badge {
  position: absolute;
  top: 15px;
  right: 15px;
  padding: 8px 15px;
  border-radius: 25px;
  font-size: 0.85rem;
  font-weight: 600;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: 8px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.badge-icon {
  font-size: 1rem;
}

.badge-label {
  font-size: 0.85rem;
}

.post-type-badge.video {
  background: rgba(255, 68, 68, 0.9);
  color: #fff;
}

.post-type-badge.image {
  background: rgba(68, 255, 68, 0.9);
  color: #000;
}

.post-type-badge.text {
  background: rgba(68, 68, 255, 0.9);
  color: #fff;
}

.post-type-badge.mixed {
  background: rgba(255, 68, 255, 0.9);
  color: #fff;
}

/* 文章内容样式 */
.post-content {
  padding: 25px;
}

.post-header {
  margin-bottom: 15px;
}

.post-title {
  font-size: 1.3rem;
  margin-bottom: 10px;
  color: #ffffff;
  line-height: 1.4;
  font-weight: 700;
  transition: color 0.3s ease;
}

.post-card:hover .post-title {
  color: #ff94d2;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  font-size: 0.9rem;
}

.author-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.avatar {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: bold;
  font-size: 0.9rem;
}

.author-name {
  color: #ffffff;
  font-weight: 500;
}

.post-date {
  color: rgba(255, 255, 255, 0.6);
}

.post-excerpt {
  color: #e0e0e0;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 0.95rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-stats {
  display: flex;
  gap: 20px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.stat {
  display: flex;
  align-items: center;
  gap: 8px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  transition: color 0.3s ease;
}

.post-card:hover .stat {
  color: #fff;
}

.icon {
  font-style: normal;
  font-size: 1.1rem;
}

/* 点赞按钮样式 */
.like-btn {
  position: absolute;
  top: 15px;
  left: 15px;
  padding: 10px 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 25px;
  background: rgba(0, 0, 0, 0.5);
  color: #fff;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  backdrop-filter: blur(10px);
  z-index: 10;
  display: flex;
  align-items: center;
  gap: 5px;
}

.like-btn:hover,
.like-btn.liked {
  background: linear-gradient(45deg, #ff4d6d, #ff758f);
  border-color: #ff4d6d;
  transform: scale(1.05);
  box-shadow: 0 5px 15px rgba(255, 77, 109, 0.4);
}

/* 分页样式 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 25px;
  margin-top: 50px;
  padding-bottom: 50px;
}

.page-btn {
  padding: 12px 25px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 30px;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 8px;
  backdrop-filter: blur(10px);
}

.page-btn:hover:not(:disabled) {
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  border-color: transparent;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(255, 148, 210, 0.3);
}

.page-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.page-info {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #fff;
  font-size: 1.1rem;
}

.current-page {
  font-weight: 700;
  color: #ff94d2;
  font-size: 1.3rem;
}

.total-pages {
  color: rgba(255, 255, 255, 0.7);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .blog-header {
    padding: 40px 20px 30px;
  }
  
  .main-title {
    font-size: 2.5rem;
  }
  
  .subtitle {
    font-size: 1rem;
    margin-bottom: 30px;
  }
  
  .search-bar {
    max-width: 100%;
  }
  
  .filter-container {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .posts-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .post-card {
    margin: 0;
  }
  
  .post-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  
  .pagination {
    flex-wrap: wrap;
    gap: 15px;
  }
}

@media (max-width: 480px) {
  .blog-header {
    padding: 30px 15px 25px;
  }
  
  .main-title {
    font-size: 2rem;
  }
  
  .search-input {
    padding: 15px 20px;
    font-size: 0.9rem;
  }
  
  .search-btn {
    padding: 15px 20px;
  }
  
  .filter-bar {
    width: 100%;
    justify-content: flex-start;
  }
  
  .filter-btn {
    padding: 10px 18px;
    font-size: 0.9rem;
  }
  
  .posts-container {
    padding: 0 15px 40px;
  }
}
</style>