<template>
  <div class="blog-list">
    <!-- 导航栏 -->
    <nav class="navbar">
      <div class="nav-left">
        <a href="#" @click="goBack" class="nav-link">
          <span class="nav-icon">⬅️</span>
          返回
        </a>
      </div>
      <div class="nav-center">
        <span class="nav-title">时尚博客</span>
      </div>
      <div class="nav-right">
        <!-- 移除了发布按钮，避免与主页导航重复 -->
      </div>
    </nav>

    <!-- 内容筛选器 -->
    <div class="filter-section">
      <div class="filter-group">
        <label class="filter-label">分类:</label>
        <select v-model="filters.category" class="filter-select">
          <option value="">全部</option>
          <option value="穿搭">穿搭</option>
          <option value="美妆">美妆</option>
          <option value="护肤">护肤</option>
          <option value="配饰">配饰</option>
          <option value="鞋包">鞋包</option>
          <option value="其他">其他</option>
        </select>
      </div>
      
      <div class="filter-group">
        <label class="filter-label">时间:</label>
        <select v-model="filters.timeRange" class="filter-select">
          <option value="all">全部</option>
          <option value="today">今天</option>
          <option value="week">本周</option>
          <option value="month">本月</option>
        </select>
      </div>
      
      <div class="filter-group">
        <label class="filter-label">排序:</label>
        <select v-model="filters.sortBy" class="filter-select">
          <option value="latest">最新</option>
          <option value="popular">热门</option>
          <option value="likes">点赞数</option>
        </select>
      </div>
    </div>

    <!-- 博客列表 -->
    <div v-if="filteredBlogs.length > 0" class="blog-grid">
      <div 
        v-for="blog in paginatedBlogs" 
        :key="blog.id" 
        class="blog-card"
        @click="goToDetail(blog.id)"
      >
        <div class="blog-header">
          <div class="user-info">
            <div class="user-avatar">{{ getUserAvatar(blog.author) }}</div>
            <div class="user-details">
              <div class="user-name">{{ blog.author }}</div>
              <div class="blog-meta">
                <span class="blog-category">{{ blog.category }}</span>
                <span class="blog-time">{{ formatTime(blog.created_at) }}</span>
              </div>
            </div>
          </div>
        </div>

        <div class="blog-content">
          <h3 class="blog-title">{{ blog.title }}</h3>
          
          <!-- 根据内容类型显示不同内容 -->
          <div v-if="blog.content_type === 'text'" class="text-content">
            <p class="blog-text">{{ blog.content }}</p>
          </div>
          
          <div v-else-if="blog.content_type === 'image'" class="image-content">
            <div class="image-grid">
              <img 
                v-for="(image, index) in blog.images.slice(0, 3)" 
                :key="index" 
                :src="image.url" 
                :alt="`图片${index + 1}`"
                class="blog-image"
                @load="onImageLoad"
                @error="onImageError"
              />
              <div v-if="blog.images.length > 3" class="image-count">
                +{{ blog.images.length - 3 }}
              </div>
            </div>
          </div>
          
          <div v-else-if="blog.content_type === 'video'" class="video-content">
            <div class="video-container">
              <video 
                :src="blog.video.url" 
                controls 
                class="blog-video"
                @load="onVideoLoad"
                @error="onVideoError"
              >
                您的浏览器不支持视频播放
              </video>
            </div>
            <p v-if="blog.content" class="blog-text">{{ blog.content }}</p>
          </div>
          
          <div v-else-if="blog.content_type === 'mixed'" class="mixed-content">
            <p v-if="blog.content" class="blog-text">{{ blog.content }}</p>
            <div v-if="blog.images && blog.images.length > 0" class="image-grid">
              <img 
                v-for="(image, index) in blog.images.slice(0, 3)" 
                :key="index" 
                :src="image.url" 
                :alt="`图片${index + 1}`"
                class="blog-image"
                @load="onImageLoad"
                @error="onImageError"
              />
              <div v-if="blog.images.length > 3" class="image-count">
                +{{ blog.images.length - 3 }}
              </div>
            </div>
            <div v-if="blog.video" class="video-container">
              <video 
                :src="blog.video.url" 
                controls 
                class="blog-video"
                @load="onVideoLoad"
                @error="onVideoError"
              >
                您的浏览器不支持视频播放
              </video>
            </div>
          </div>
        </div>

        <div class="blog-stats">
          <div class="stat-item">
            <span class="stat-icon">👁️</span>
            <span class="stat-value">{{ blog.views }}</span>
          </div>
          <div class="stat-item" @click.stop="toggleLike(blog)">
            <span class="stat-icon" :class="{ 'liked': blog.user_liked }">
              {{ blog.user_liked ? '❤️' : '🤍' }}
            </span>
            <span class="stat-value">{{ blog.likes }}</span>
          </div>
          <div class="stat-item">
            <span class="stat-icon">💬</span>
            <span class="stat-value">{{ blog.comments }}</span>
          </div>
          <div class="stat-item">
            <span class="stat-icon">📤</span>
            <span class="stat-value">{{ blog.shares }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 空状态 -->
    <div v-else class="empty-state">
      <div class="empty-icon">📝</div>
      <h3 class="empty-title">暂无博客</h3>
      <p class="empty-description">还没有符合条件的博客，快发布第一篇吧！</p>
      <button @click="goToCreate" class="empty-btn">发布博客</button>
    </div>

    <!-- 分页组件 -->
    <div v-if="totalPages > 1" class="pagination">
      <button 
        @click="prevPage" 
        :disabled="currentPage === 1"
        class="page-btn"
      >
        上一页
      </button>
      
      <div class="page-numbers">
        <button
          v-for="page in getPageNumbers()"
          :key="page"
          @click="goToPage(page)"
          :class="['page-number', { active: page === currentPage }]"
        >
          {{ page }}
        </button>
      </div>
      
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
export default {
  name: 'BlogList',
  props: {
    goBack: {
      type: Function,
      required: true
    },
    navigateTo: {
      type: Function,
      required: true
    }
  },
  data() {
    return {
      blogs: [
        {
          id: 1,
          title: "春季穿搭指南",
          content: "春天来了，如何搭配出时尚又舒适的造型？",
          category: "穿搭",
          content_type: "text",
          author: "小美",
          created_at: new Date(Date.now() - 3600000).toISOString(),
          views: 1234,
          likes: 56,
          comments: 12,
          shares: 8,
          user_liked: false
        },
        {
          id: 2,
          title: "美妆心得分享",
          content: "今天想和大家分享我的日常美妆技巧",
          category: "美妆",
          content_type: "image",
          images: [
            { url: "https://via.placeholder.com/300x300/FF94D2/FFFFFF?text=美妆1" },
            { url: "https://via.placeholder.com/300x300/B388EB/FFFFFF?text=美妆2" },
            { url: "https://via.placeholder.com/300x300/4FC3F7/FFFFFF?text=美妆3" }
          ],
          author: "小丽",
          created_at: new Date(Date.now() - 7200000).toISOString(),
          views: 2345,
          likes: 89,
          comments: 23,
          shares: 15,
          user_liked: true
        },
        {
          id: 3,
          title: "护肤小贴士",
          content: "如何在春季做好肌肤护理？",
          category: "护肤",
          content_type: "video",
          video: { url: "https://example.com/video.mp4" },
          author: "小华",
          created_at: new Date(Date.now() - 10800000).toISOString(),
          views: 3456,
          likes: 123,
          comments: 34,
          shares: 21,
          user_liked: false
        },
        {
          id: 4,
          title: "周末出游搭配",
          content: "周末出游的完美搭配推荐",
          category: "穿搭",
          content_type: "mixed",
          images: [
            { url: "https://via.placeholder.com/300x300/FF94D2/FFFFFF?text=搭配1" },
            { url: "https://via.placeholder.com/300x300/B388EB/FFFFFF?text=搭配2" }
          ],
          video: { url: "https://example.com/outfit-video.mp4" },
          author: "小芳",
          created_at: new Date(Date.now() - 14400000).toISOString(),
          views: 4567,
          likes: 156,
          comments: 45,
          shares: 28,
          user_liked: true
        }
      ],
      filters: {
        category: '',
        timeRange: 'all',
        sortBy: 'latest'
      },
      currentPage: 1,
      itemsPerPage: 6
    };
  },
  computed: {
    filteredBlogs() {
      let filtered = this.blogs;

      // 分类筛选
      if (this.filters.category) {
        filtered = filtered.filter(blog => blog.category === this.filters.category);
      }

      // 时间筛选
      if (this.filters.timeRange !== 'all') {
        const now = new Date();
        filtered = filtered.filter(blog => {
          const blogDate = new Date(blog.created_at);
          const diffTime = Math.abs(now - blogDate);
          const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

          switch (this.filters.timeRange) {
            case 'today':
              return diffDays <= 1;
            case 'week':
              return diffDays <= 7;
            case 'month':
              return diffDays <= 30;
            default:
              return true;
          }
        });
      }

      // 排序
      filtered.sort((a, b) => {
        switch (this.filters.sortBy) {
          case 'latest':
            return new Date(b.created_at) - new Date(a.created_at);
          case 'popular':
            return (b.views + b.likes * 10 + b.comments * 5) - (a.views + a.likes * 10 + a.comments * 5);
          case 'likes':
            return b.likes - a.likes;
          default:
            return 0;
        }
      });

      return filtered;
    },
    paginatedBlogs() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.filteredBlogs.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.filteredBlogs.length / this.itemsPerPage);
    }
  },
  methods: {
    goToDetail(blogId) {
      // 通过事件通知父组件切换到详情页
      this.$emit('view-post', blogId);
    },
    
    goToCreate() {
      // 通过事件通知父组件切换到创建页面
      this.$emit('go-to-create');
    },
    
    getUserAvatar(username) {
      return username.charAt(0).toUpperCase();
    },
    
    formatTime(dateString) {
      const date = new Date(dateString);
      const now = new Date();
      const diffTime = Math.abs(now - date);
      const diffHours = Math.ceil(diffTime / (1000 * 60 * 60));
      
      if (diffHours < 1) {
        return '刚刚';
      } else if (diffHours < 24) {
        return `${diffHours}小时前`;
      } else {
        return date.toLocaleDateString('zh-CN');
      }
    },
    
    toggleLike(blog) {
      blog.user_liked = !blog.user_liked;
      blog.likes += blog.user_liked ? 1 : -1;
    },
    
    onImageLoad(event) {
      // 图片加载完成的处理
      event.target.style.opacity = 1;
    },
    
    onImageError(event) {
      // 图片加载失败后的处理
      event.target.src = 'https://via.placeholder.com/300x300/CCCCCC/FFFFFF?text=加载失败';
    },
    
    onVideoLoad(event) {
      // 视频加载完成的处理
      event.target.style.opacity = 1;
    },
    
    onVideoError(event) {
      // 视频加载失败后的处理
      console.error('视频加载失败:', event.target.src);
    },
    
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    
    goToPage(page) {
      this.currentPage = page;
    },
    
    getPageNumbers() {
      const pages = [];
      const maxVisiblePages = 5;
      let startPage = Math.max(1, this.currentPage - Math.floor(maxVisiblePages / 2));
      let endPage = Math.min(this.totalPages, startPage + maxVisiblePages - 1);
      
      if (endPage - startPage + 1 < maxVisiblePages) {
        startPage = Math.max(1, endPage - maxVisiblePages + 1);
      }
      
      for (let i = startPage; i <= endPage; i++) {
        pages.push(i);
      }
      
      return pages;
    }
  }
};
</script>

<style scoped>
.blog-list {
  min-height: 100vh;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  color: #fff;
  padding: 20px;
  box-sizing: border-box;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 0;
  margin-bottom: 30px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.nav-left, .nav-center, .nav-right {
  flex: 1;
  text-align: center;
}

.nav-left {
  text-align: left;
}

.nav-right {
  text-align: right;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  transition: color 0.3s ease;
  padding: 10px 15px;
  border-radius: 10px;
  transition: all 0.3s ease;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.nav-link:hover {
  color: #ff94d2;
  background: rgba(255, 148, 210, 0.1);
}

.nav-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #fff;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.filter-section {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
  flex-wrap: wrap;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.filter-group {
  flex: 1;
  min-width: 200px;
}

.filter-label {
  display: block;
  margin-bottom: 8px;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
  font-size: 0.95rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.filter-select {
  width: 100%;
  padding: 12px;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 1rem;
  transition: all 0.3s ease;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.filter-select:focus {
  outline: none;
  border-color: #ff94d2;
  box-shadow: 0 0 0 3px rgba(255, 148, 210, 0.3);
}

.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
  padding: 20px 0;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  overflow: hidden;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(255, 148, 210, 0.2);
  border-color: rgba(255, 148, 210, 0.3);
}

.blog-image {
  width: 100%;
  height: 200px;
  background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
  position: relative;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-content {
  padding: 25px;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-title {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 12px;
  color: #fff;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-excerpt {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 0.95rem;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.6);
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-stats {
  display: flex;
  gap: 15px;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.7);
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.action-buttons {
  display: flex;
  gap: 10px;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.action-btn {
  flex: 1;
  padding: 12px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
  font-size: 0.9rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.read-btn {
  background: rgba(255, 148, 210, 0.2);
  color: #ff94d2;
}

.read-btn:hover {
  background: rgba(255, 148, 210, 0.3);
}

.like-btn {
  background: rgba(161, 138, 255, 0.2);
  color: #a18aff;
}

.like-btn:hover {
  background: rgba(161, 138, 255, 0.3);
}

.comment-btn {
  background: rgba(102, 204, 255, 0.2);
  color: #66ccff;
}

.comment-btn:hover {
  background: rgba(102, 204, 255, 0.3);
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-top: 40px;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.page-btn {
  padding: 10px 16px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.8);
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.95rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.page-btn:hover:not(:disabled) {
  background: rgba(255, 148, 210, 0.2);
  color: #ff94d2;
  border-color: rgba(255, 148, 210, 0.4);
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.current-page {
  padding: 10px 16px;
  background: rgba(255, 148, 210, 0.2);
  border: 1px solid rgba(255, 148, 210, 0.4);
  border-radius: 8px;
  color: #ff94d2;
  font-weight: 600;
  font-size: 0.95rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: rgba(255, 255, 255, 0.6);
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 20px;
  color: rgba(255, 255, 255, 0.3);
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.empty-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 10px;
  color: rgba(255, 255, 255, 0.8);
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.empty-description {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.6);
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

@media (max-width: 768px) {
  .blog-list {
    padding: 15px;
  }
  
  .navbar {
    margin-bottom: 20px;
  }
  
  .nav-left, .nav-right {
    flex: 0.5;
  }
  
  .nav-center {
    flex: 1;
  }
  
  .filter-section {
    flex-direction: column;
    gap: 15px;
  }
  
  .blog-grid {
    grid-template-columns: 1fr;
  }
  
  .action-buttons {
    flex-direction: column;
  }
}
</style>