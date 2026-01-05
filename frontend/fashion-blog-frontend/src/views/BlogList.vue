<template>
  <div class="blog-list">
    <!-- 头部导航 -->
    <div class="blog-header">
      <h1>服装品牌</h1>
      <p>分享你的时尚见解，与社区一起交流</p>
      <div class="search-bar">
        <input 
          v-model="searchQuery" 
          @input="searchPosts"
          type="text" 
          placeholder="搜索博客文章..."
          class="search-input"
        >
        <button @click="searchPosts" class="search-btn">搜索</button>
        <router-link to="/blog/create" class="create-btn">
          <i class="icon">✏️</i>
          发布新博客
        </router-link>
      </div>
    </div>

    <!-- 内容类型筛选 -->
    <div class="filter-bar">
      <button 
        v-for="type in contentTypes" 
        :key="type.value"
        @click="filterByType(type.value)"
        :class="['filter-btn', { active: selectedType === type.value }]"
      >
        {{ type.label }}
      </button>
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
          <!-- 文章类型标识 -->
          <div class="post-type-badge" :class="post.content_type">
            {{ getContentTypeLabel(post.content_type) }}
          </div>

          <!-- 文章内容预览 -->
          <div class="post-content">
            <h3 class="post-title">{{ post.title }}</h3>
            <p class="post-excerpt">{{ getExcerpt(post.content) }}</p>
            
            <!-- 视频/图片预览 -->
            <div v-if="post.content_type === 'video' && post.video_file" class="media-preview">
              <video :src="post.video_file" class="video-thumbnail"></video>
              <div class="play-overlay">▶️</div>
            </div>
            
            <div v-if="post.content_type === 'image' && post.image_files?.length" class="media-preview">
              <img :src="post.image_files[0].file" :alt="post.title" class="image-thumbnail">
            </div>
          </div>

          <!-- 文章元信息 -->
          <div class="post-meta">
            <div class="author-info">
              <div class="avatar">{{ post.author.username.charAt(0).toUpperCase() }}</div>
              <span class="author-name">{{ post.author.username }}</span>
            </div>
            <div class="post-stats">
              <span class="stat">
                <i class="icon">❤️</i>
                {{ post.likes_count }}
              </span>
              <span class="stat">
                <i class="icon">💬</i>
                {{ post.comments_count }}
              </span>
              <span class="stat">
                <i class="icon">📅</i>
                {{ formatDate(post.created_at) }}
              </span>
            </div>
          </div>

          <!-- 点赞状态 -->
          <button 
            v-if="post.liked_by_user" 
            @click.stop="unlikePost(post)" 
            class="like-btn liked"
          >
            ❤️ 已点赞
          </button>
          <button 
            v-else 
            @click.stop="likePost(post)" 
            class="like-btn"
          >
            🤍 点赞
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
        上一页
      </button>
      <span class="page-info">
        第 {{ currentPage }} 页，共 {{ totalPages }} 页
      </span>
      <button 
        @click="nextPage" 
        :disabled="currentPage === totalPages"
        class="page-btn"
      >
        下一页
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
        { id: 3, title: '2027年流行色大盘点', content: 'Pantone发布了2027年的年度流行色，这些色彩将在时尚界掀起一股 heats。让我们一起来看看这些流行色的魅力...', content_type: 'image', image_files: [{ file: '/images/fashion-color-2027.svg' }], author: { username: '色彩大师' }, likes_count: 62, comments_count: 15, created_at: '2027-10-05', liked_by_user: false },
        { id: 4, title: '必备配饰推荐', content: '配饰是整体造型的点睛之笔。本文将为您推荐几款春季必备的配饰，让您的造型更加完美...', content_type: 'text', author: { username: '配饰专家' }, likes_count: 29, comments_count: 7, created_at: '2027-09-28', liked_by_user: false },
        { id: 5, title: '街头时尚风格解析', content: '街头时尚一直是时尚界的重要组成部分。本文将为您解析2027年街头时尚的最新趋势...', content_type: 'mixed', author: { username: '街头潮人' }, likes_count: 53, comments_count: 11, created_at: '2027-09-20', liked_by_user: true },
        { id: 6, title: '如何选择适合自己的发型', content: '发型是塑造个人形象的重要因素。本文将为您介绍几种不同脸型适合的发型，帮助您找到最适合自己的发型...', content_type: 'text', author: { username: '发型设计师' }, likes_count: 35, comments_count: 9, created_at: '2027-09-15', liked_by_user: false }
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

    getExcerpt(content, maxLength = 150) {
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

    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString('zh-CN');
    }
  }
};
</script>

<style scoped>
.blog-list {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  color: #fff;
}

.blog-header {
  text-align: center;
  margin-bottom: 40px;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(10px);
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  padding: 30px 20px;
}

.blog-header h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.8), 0 0 40px rgba(200, 140, 220, 0.5), 0 0 60px rgba(200, 140, 220, 0.3);
  font-weight: bold;
  z-index: 10;
  position: relative;
  opacity: 1;
  filter: none;
  display: inline-block;
  padding: 10px 0;
}

.blog-header p {
  color: #ccc;
  font-size: 1.1rem;
  margin-bottom: 30px;
}

.search-bar {
  display: flex;
  gap: 15px;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

.search-input {
  padding: 12px 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 25px;
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  font-size: 1rem;
  min-width: 300px;
}

.search-input:focus {
  outline: none;
  border-color: #c67bb4;
}

.search-btn, .create-btn, .create-first-btn {
  padding: 12px 24px;
  border: 1px solid rgba(74, 60, 92, 0.3);
  border-radius: 25px;
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s;
}

.search-btn:hover, .create-btn:hover, .create-first-btn:hover {
  transform: translateY(-2px);
}

.filter-bar {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 30px;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 8px 16px;
  border: 2px solid rgba(200, 140, 220, 0.3);
  border-radius: 20px;
  background: transparent;
  color: #e0e0e0;
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.filter-btn::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.3) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: rotate(30deg);
  /* animation: shimmer 3s infinite; */
}

.filter-btn.active, .filter-btn:hover {
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  border-color: rgba(74, 60, 92, 0.5);
  color: #fff;
  box-shadow: 0 5px 15px rgba(200, 140, 220, 0.3);
}

@keyframes shimmer {
  0% { transform: translateX(-100%) rotate(30deg); }
  100% { transform: translateX(100%) rotate(30deg); }
}

.posts-container {
  min-height: 400px;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 300px;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(255, 255, 255, 0.2);
  border-top: 4px solid #c67bb4;
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
  padding: 60px 20px;
}

.no-posts h3 {
  color: #ffffff;
  margin-bottom: 10px;
}

.no-posts p {
  color: #e0e0e0;
  margin-bottom: 30px;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 25px;
  margin-bottom: 40px;
}

.post-card {
  background: transparent;
  border-radius: 15px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s;
  border: 1px solid rgba(74, 60, 92, 0.3);
  position: relative;
}

.post-card::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: rotate(30deg);
  /* animation: shimmer 3s infinite; */
  pointer-events: none;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(200, 140, 220, 0.3);
}

.post-type-badge {
  position: absolute;
  top: 15px;
  right: 15px;
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: bold;
  z-index: 2;
  border: 1px solid rgba(74, 60, 92, 0.3);
}

.post-type-badge.video { background: #ff4444; color: #fff; }
.post-type-badge.image { background: #44ff44; color: #000; }
.post-type-badge.text { background: #4444ff; color: #fff; }
.post-type-badge.mixed { background: #ff44ff; color: #fff; }

.post-content {
  padding: 25px;
}

.post-title {
  font-size: 1.3rem;
  margin-bottom: 15px;
  color: #ffffff;
  line-height: 1.4;
  position: relative;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, 0.3);
}

.post-excerpt {
  color: #e0e0e0;
  line-height: 1.6;
  margin-bottom: 20px;
}

.media-preview {
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 20px;
}

.video-thumbnail, .image-thumbnail {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.play-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 3rem;
  color: rgba(255, 255, 255, 0.8);
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 25px 20px;
}

.author-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: bold;
}

.author-name {
  color: #ffffff;
  font-size: 0.9rem;
}

.post-stats {
  display: flex;
  gap: 15px;
}

.stat {
  display: flex;
  align-items: center;
  gap: 5px;
  color: #e0e0e0;
  font-size: 0.9rem;
}

.icon {
  font-style: normal;
}

.like-btn {
  position: absolute;
  bottom: 20px;
  right: 25px;
  padding: 8px 16px;
  border: 2px solid #c67bb4;
  border-radius: 20px;
  background: transparent;
  color: #c67bb4;
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.like-btn::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.3) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: rotate(30deg);
  /* animation: shimmer 3s infinite; */
}

.like-btn:hover, .like-btn.liked {
  background: #c67bb4;
  color: #fff;
  box-shadow: 0 5px 15px rgba(200, 140, 220, 0.3);
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 40px;
}

.page-btn {
  padding: 10px 20px;
  border: 2px solid #c67bb4;
  border-radius: 20px;
  background: transparent;
  color: #c67bb4;
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.page-btn::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.3) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: rotate(30deg);
  /* animation: shimmer 3s infinite; */
}

.page-btn:hover:not(:disabled) {
  background: #c67bb4;
  color: #fff;
  box-shadow: 0 5px 15px rgba(200, 140, 220, 0.3);
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  color: #ccc;
}

/* 文字玻璃反光效果 */
h1, h2, h3, h4, h5, h6, .post-title {
  position: relative;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, 0.3);
}

@media (max-width: 768px) {
  .blog-list {
    padding: 15px;
  }
  
  .posts-grid {
    grid-template-columns: 1fr;
  }
  
  .search-bar {
    flex-direction: column;
  }
  
  .search-input {
    min-width: 100%;
  }
  
  .post-meta {
    flex-direction: column;
    gap: 15px;
    align-items: flex-start;
  }
}
</style>