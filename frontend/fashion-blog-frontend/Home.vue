<template>
  <div class="home">
    <header class="header">
      <h1 class="site-title">rann的小试间</h1>
      
      <!-- 导航按钮 - 紧贴标题正下方 -->
      <nav class="main-nav-buttons">
        <ul>
          <li><a href="#" class="no-border-btn" :class="{ active: currentRoute === '/' }" @click.prevent="navigateTo('/')">首页</a></li>
          <li><a href="#" class="no-border-btn" :class="{ active: currentRoute === '/blog' }" @click.prevent="navigateTo('/blog')">博客</a></li>
          <li><a href="#" class="no-border-btn" :class="{ active: currentRoute === '/blog/create' }" @click.prevent="navigateTo('/blog/create')">发布</a></li>
        </ul>
        <!-- 动态上划线指示器 -->
        <div class="floating-indicator" :style="indicatorStyle"></div>
      </nav>
    </header>
    
    <div class="content-wrapper">
      <!-- 左侧边栏 -->
      <div class="left-sidebar">
        <!-- 文章分类 -->
        <div class="categories-section">
          <h3>文章分类</h3>
          <ul class="categories-list">
            <li><a href="#" :class="{ active: selectedCategory === '未分类' }" @click.prevent="selectCategory('未分类')">未分类 <span class="category-count">10</span></a></li>
            <li><a href="#" :class="{ active: selectedCategory === '时尚趋势' }" @click.prevent="selectCategory('时尚趋势')">时尚趋势 <span class="category-count">8</span></a></li>
            <li><a href="#" :class="{ active: selectedCategory === '品牌动态' }" @click.prevent="selectCategory('品牌动态')">品牌动态 <span class="category-count">5</span></a></li>
            <li><a href="#" :class="{ active: selectedCategory === '潮流预测' }" @click.prevent="selectCategory('潮流预测')">潮流预测 <span class="category-count">3</span></a></li>
            <li><a href="#" :class="{ active: selectedCategory === '时装周' }" @click.prevent="selectCategory('时装周')">时装周 <span class="category-count">6</span></a></li>
            <li><a href="#" :class="{ active: selectedCategory === '搭配指南' }" @click.prevent="selectCategory('搭配指南')">搭配指南 <span class="category-count">4</span></a></li>
          </ul>
        </div>
        
        <!-- 热门标签 -->
        <div class="tags-section">
          <h3>热门标签</h3>
          <div class="tags-cloud">
            <a href="#" class="tag" :class="{ active: selectedTag === '时尚' }" @click.prevent="selectTag('时尚')">时尚</a>
            <a href="#" class="tag" :class="{ active: selectedTag === '2026趋势' }" @click.prevent="selectTag('2026趋势')">2026趋势</a>
            <a href="#" class="tag" :class="{ active: selectedTag === '巴黎时装周' }" @click.prevent="selectTag('巴黎时装周')">巴黎fashion</a>
            <a href="#" class="tag" :class="{ active: selectedTag === '环保时尚' }" @click.prevent="selectTag('环保时尚')">环保时尚</a>
            <a href="#" class="tag" :class="{ active: selectedTag === '春季色彩' }" @click.prevent="selectTag('春季色彩')">春季色彩</a>
            <a href="#" class="tag" :class="{ active: selectedTag === '品牌' }" @click.prevent="selectTag('品牌')">品牌</a>
            <a href="#" class="tag" :class="{ active: selectedTag === '潮流' }" @click.prevent="selectTag('潮流')">潮流</a>
            <a href="#" class="tag" :class="{ active: selectedTag === '搭配' }" @click.prevent="selectTag('搭配')">搭配</a>
          </div>
        </div>
      </div>
      
      <!-- 主内容区域 -->
      <div class="main-content">
        <!-- 动态组件区域 -->
        <component 
          :is="currentComponent" 
          v-if="currentComponent !== 'HomeContent'"
          :goBack="goToHome"
          :navigateTo="navigateTo"
          @view-post="handleViewPost"
          @go-to-create="navigateTo('/blog/create')"
          @blog-created="handleBlogCreated"
        />
        <HomeContent v-else />
      </div>
    </div>
    
    <footer class="footer">
      <p>&copy; 2026 服装品牌. 保留所有权利.</p>
      <div class="social-links">
        <a href="#">Instagram</a>
        <a href="#">Facebook</a>
        <a href="#">Twitter</a>
      </div>
    </footer>
  </div>
</template>

<script>
import HomeContent from './HomeContent.vue'
import BlogList from './BlogList.vue'
import BlogCreate from './BlogCreate.vue'

export default {
  name: 'HomePage',
  components: {
    HomeContent,
    BlogList,
    BlogCreate
  },
  data() {
    return {
      currentComponent: 'HomeContent',
      currentRoute: '/',
      indicatorStyle: {
        left: '0px',
        width: '60px'
      },
      selectedCategory: null,
      selectedTag: null
    };
  },
  mounted() {
    this.updateIndicator();
  },
  beforeUnmount() {
    // 清理定时器和其他资源
    // 如果有定时器，在这里清除
    // 示例：如果组件中有使用 setInterval，需要在此处清除
    // clearInterval(this.myTimer);
    
    // 移除可能添加的全局事件监听器
    // window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    navigateTo(route) {
      this.currentRoute = route;
      
      if (route === '/') {
        this.currentComponent = 'HomeContent';
      } else if (route === '/blog') {
        this.currentComponent = 'BlogList';
      } else if (route === '/blog/create') {
        this.currentComponent = 'BlogCreate';
      }
      
      this.updateIndicator();
    },
    
    goToHome() {
      this.navigateTo('/');
    },
    
    handleViewPost(postId) {
      // 处理查看帖子的逻辑
      console.log('View post:', postId);
    },
    
    handleBlogCreated(blogData) {
      // 处理博客创建成功的逻辑
      console.log('Blog created:', blogData);
      // 可以在这里添加成功提示或自动跳转回博客列表
      this.navigateTo('/blog');
    },
    
    // 处理分类点击事件
    selectCategory(categoryName) {
      this.selectedCategory = categoryName;
      this.selectedTag = null; // 清除标签选中状态
    },
    
    // 处理标签点击事件
    selectTag(tagName) {
      this.selectedTag = tagName;
      this.selectedCategory = null; // 清除分类选中状态
    },
    setActiveRoute(route) {
      this.currentRoute = route;
      this.updateIndicator();
    },
    
    updateIndicator() {
      // 根据当前路由更新指示器位置
      this.$nextTick(() => {
        const navLinks = this.$el.querySelectorAll('.main-nav-buttons a');
        let activeLink = null;
        
        for (let i = 0; i < navLinks.length; i++) {
          if (navLinks[i].classList.contains('active')) {
            activeLink = navLinks[i];
            break;
          }
        }
        
        if (activeLink) {
          const rect = activeLink.getBoundingClientRect();
          const parentRect = activeLink.parentElement.getBoundingClientRect();
          
          this.indicatorStyle = {
            left: `${rect.left - parentRect.left}px`,
            width: `${rect.width}px`,
            transition: 'all 0.3s ease'
          };
        }
      });
    }
  }
};
</script>

<style scoped>
.home {
  width: 100%;
  margin: 0;
  padding: 0 40px;
  color: #fff;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  /* 确保没有边框 */
  border: none;
}

.header {
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  align-items: center !important;
  padding: 25px 40px !important;
  position: relative !important;
  margin-bottom: 0 !important;
  background: transparent !important;
  background-image: none !important;
  background-blend-mode: normal !important;
  /* 确保无边框和背景 */
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
}

.site-title {
  font-size: 2.8rem;
  font-weight: 300;
  color: #000;
  margin: 0 0 20px 0;
  text-align: center;
  letter-spacing: 2px;
  text-shadow: none;
  background: none;
  -webkit-background-clip: initial;
  -webkit-text-fill-color: initial;
  background-clip: initial;
}

.top-nav {
  width: 100%;
  margin: 0;
  padding: 0;
  background: none !important;
  box-shadow: none !important;
  border: none !important;
  display: flex;
  justify-content: center;
}

.content-wrapper {
  display: flex;
  flex: 1;
  margin: 0;
  padding: 40px 0;
  gap: 0;
}

.left-sidebar {
  width: 250px;
  background: rgba(0, 0, 0, 0.3);
  padding: 30px 20px;
  border-radius: 10px;
  margin-right: 40px;
  height: fit-content;
  border: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: visible;
  z-index: 1000;
}

.main-content {
  flex: 1;
  padding: 0;
  background: none;
}

.categories-section, .tags-section {
  margin-bottom: 30px;
  opacity: 1 !important;
  visibility: visible !important;
  display: block !important;
  position: static !important;
}

.categories-section h3, .tags-section h3 {
  color: #fff;
  margin-bottom: 15px;
  font-size: 1.1rem;
  font-weight: 500;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding-bottom: 8px;
}

.categories-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.categories-list li {
  margin: 0;
  padding: 0;
}

.categories-list a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  font-size: 0.9rem;
  padding: 8px 12px;
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: block;
  transition: all 0.3s ease;
  position: relative;
}

.categories-list a:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  transform: translateY(-1px);
}

.categories-list a.active {
  background: rgba(255, 105, 180, 0.2);
  color: #ff69b4;
  border-color: rgba(255, 105, 180, 0.4);
  font-weight: 600;
}

.fashion-news {
  margin-bottom: 50px;
}

.section-title {
  font-size: 2.2rem;
  color: #fff;
  margin-bottom: 30px;
  text-align: center;
  position: relative;
  padding-bottom: 15px;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 3px;
  background: linear-gradient(45deg, #fff, rgba(255, 255, 255, 0.5));
  border-radius: 2px;
}

.news-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin-bottom: 40px;
}

.news-item {
  background: rgba(0, 0, 0, 0.4);
  border-radius: 15px;
  padding: 0;
  overflow: hidden;
  transition: all 0.4s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  position: relative;
}

.news-item.large {
  grid-column: span 2;
  display: flex;
  flex-direction: row;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.2));
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.news-item.large .post-image {
  width: 40%;
  height: 250px;
  overflow: hidden;
}

.news-item.large .post-content {
  padding: 30px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.news-item.small {
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.3), rgba(255, 255, 255, 0.05));
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.news-item.small .post-image {
  height: 180px;
  overflow: hidden;
}

.news-item.small .post-content {
  padding: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.post-image {
  position: relative;
  overflow: hidden;
  background: linear-gradient(45deg, #333, #555);
}

.post-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.news-item:hover .post-image img {
  transform: scale(1.05);
}

.post-content {
  position: relative;
  z-index: 2;
}

.post-meta {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.85rem;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 15px;
}

.post-category {
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.post-title {
  color: #fff;
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 12px;
  line-height: 1.4;
}

.post-excerpt {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 20px;
}

.read-more {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.9rem;
  padding: 8px 16px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 20px;
  transition: all 0.3s ease;
  display: inline-block;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
}

.read-more:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
  transform: translateY(-1px);
}

.post-card {
  background: rgba(0, 0, 0, 0.4);
  border-radius: 15px;
  padding: 25px;
  margin-bottom: 25px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.post-card:hover {
  border-color: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

.post-card h3 {
  color: #fff;
  margin-bottom: 15px;
  font-size: 1.4rem;
}

.post-card p {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  margin-bottom: 20px;
}

.main-nav-buttons {
  position: relative !important;
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
  background: transparent !important;
  background-image: none !important;
  background-blend-mode: normal !important;
  /* 确保无边框和背景 */
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

.main-nav-buttons ul {
  display: flex !important;
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  gap: 0 !important;
  background: transparent !important;
  border: none !important;
}

.main-nav-buttons li {
  margin: 0 !important;
  padding: 0 !important;
  background: transparent !important;
  border: none !important;
}

.main-nav-buttons a {
  color: rgba(255, 255, 255, 0.7) !important;
  text-decoration: none !important;
  padding: 12px 20px !important;
  display: block !important;
  border-radius: 8px !important;
  transition: all 0.3s ease !important;
  font-size: 1rem !important;
  font-weight: 500 !important;
  position: relative !important;
  background: transparent !important;
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
}

.main-nav-buttons a:hover,
.main-nav-buttons a.active {
  color: #ff69b4 !important;
  background: rgba(255, 105, 180, 0.15) !important;
  transform: translateY(-1px) !important;
}

.main-nav-buttons a:hover {
  color: rgba(255, 105, 180, 0.8) !important;
  background: rgba(255, 105, 180, 0.1) !important;
  transform: translateY(-1px) !important;
}

.main-nav-buttons a.active {
  color: #ff69b4 !important;
  background: rgba(255, 105, 180, 0.2) !important;
  transform: translateY(-1px) !important;
}

.no-border-btn {
  background: transparent !important;
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
}

.floating-indicator {
  position: absolute !important;
  bottom: -2px !important;
  height: 3px !important;
  background: linear-gradient(45deg, #999, rgba(153, 153, 153, 0.7)) !important; /* 改为更浅的灰色 */
  border-radius: 2px !important;
  transition: all 0.3s ease !important;
  opacity: 1 !important;
  z-index: 10 !important;
  pointer-events: none !important;
}

.footer {
  text-align: center;
  padding: 40px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  margin-top: 60px;
}

.footer p {
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 20px;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.social-links a {
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  transition: color 0.3s ease;
}

.social-links a:hover {
  color: #fff;
}

@media (max-width: 768px) {
  .home {
    padding: 0 15px;
  }
  
  .content-wrapper {
    flex-direction: column;
  }
  
  .left-sidebar {
    width: 100%;
    margin-right: 0;
    margin-bottom: 30px;
  }
  
  .news-grid {
    grid-template-columns: 1fr;
  }
  
  .news-item.large {
    grid-column: span 1;
    flex-direction: column;
  }
  
  .news-item.large .post-image {
    width: 100%;
  }
}

/* 强制显示左侧边栏内容 */
.left-sidebar .categories-section,
.left-sidebar .tags-section {
  opacity: 1 !important;
  visibility: visible !important;
  display: block !important;
  position: static !important;
  height: auto !important;
  overflow: visible !important;
}

.left-sidebar .categories-list,
.left-sidebar .tags-cloud {
  opacity: 1 !important;
  visibility: visible !important;
  display: block !important;
  position: static !important;
}

/* 确保悬浮框相关样式不影响直接显示 */
.dropdown-container,
.dropdown-content,
.categories-dropdown,
.tags-dropdown {
  display: none !important;
}

.floating-indicator {
  opacity: 1 !important;
}
</style>