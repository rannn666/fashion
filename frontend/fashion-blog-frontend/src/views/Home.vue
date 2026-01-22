<template>
  <div class="home">
    <header class="header">
      <h1 class="site-title">rann的小试间</h1>
      
      <!-- 导航按钮 - 紧贴标题正下方 -->
      <nav class="main-nav-buttons">
        <ul>
          <li><a href="#" :class="{ active: currentRoute === '/' }" @click.prevent="navigateTo('/')">首页</a></li>
          <li><a href="#" :class="{ active: currentRoute === '/blog' }" @click.prevent="navigateTo('/blog')">博客</a></li>
          <li><a href="#" :class="{ active: currentRoute === '/blog/create' }" @click.prevent="navigateTo('/blog/create')">发布</a></li>
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
          <h3 @click="toggleCategoriesDropdown">文章分类</h3>
          <div class="dropdown-container">
            <ul class="categories-list" :class="{ show: showCategoriesDropdown }">
              <li><a href="#" :class="{ active: selectedCategory === '未分类' }" @click.prevent="selectCategory('未分类')">未分类 <span class="category-count">10</span></a></li>
              <li><a href="#" :class="{ active: selectedCategory === '时尚趋势' }" @click.prevent="selectCategory('时尚趋势')">时尚趋势 <span class="category-count">8</span></a></li>
              <li><a href="#" :class="{ active: selectedCategory === '品牌动态' }" @click.prevent="selectCategory('品牌动态')">品牌动态 <span class="category-count">5</span></a></li>
              <li><a href="#" :class="{ active: selectedCategory === '潮流预测' }" @click.prevent="selectCategory('潮流预测')">潮流预测 <span class="category-count">3</span></a></li>
              <li><a href="#" :class="{ active: selectedCategory === '时装周' }" @click.prevent="selectCategory('时装周')">时装周 <span class="category-count">6</span></a></li>
              <li><a href="#" :class="{ active: selectedCategory === '搭配指南' }" @click.prevent="selectCategory('搭配指南')">搭配指南 <span class="category-count">4</span></a></li>
            </ul>
          </div>
        </div>
        
        <!-- 热门标签 -->
        <div class="tags-section">
          <h3 @click="toggleTagsDropdown">热门标签</h3>
          <div class="dropdown-container">
            <div class="tags-cloud" :class="{ show: showTagsDropdown }">
              <a href="#" class="tag" :class="{ active: selectedTag === '时尚' }" @click.prevent="selectTag('时尚')">时尚</a>
              <a href="#" class="tag" :class="{ active: selectedTag === '2026趋势' }" @click.prevent="selectTag('2026趋势')">2026趋势</a>
              <a href="#" class="tag" :class="{ active: selectedTag === '巴黎时装周' }" @click.prevent="selectTag('巴黎时装周')">巴黎时装周</a>
              <a href="#" class="tag" :class="{ active: selectedTag === '环保时尚' }" @click.prevent="selectTag('环保时尚')">环保时尚</a>
              <a href="#" class="tag" :class="{ active: selectedTag === '春季色彩' }" @click.prevent="selectTag('春季色彩')">春季色彩</a>
              <a href="#" class="tag" :class="{ active: selectedTag === '品牌' }" @click.prevent="selectTag('品牌')">品牌</a>
              <a href="#" class="tag" :class="{ active: selectedTag === '潮流' }" @click.prevent="selectTag('潮流')">潮流</a>
              <a href="#" class="tag" :class="{ active: selectedTag === '搭配' }" @click.prevent="selectTag('搭配')">搭配</a>
            </div>
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
      showCategoriesDropdown: false,
      showTagsDropdown: false,
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
        const navContainer = this.$el.querySelector('.main-nav-buttons');
        let activeLink = null;
        
        for (let i = 0; i < navLinks.length; i++) {
          if (navLinks[i].classList.contains('active')) {
            activeLink = navLinks[i];
            break;
          }
        }
        
        if (activeLink && navContainer) {
          const rect = activeLink.getBoundingClientRect();
          const parentRect = navContainer.getBoundingClientRect();
          
          this.indicatorStyle = {
            left: `${rect.left - parentRect.left}px`,
            width: `${rect.width}px`,
            transition: 'all 0.3s ease'
          };
        }
      });
    },
    
    toggleCategoriesDropdown() {
      this.showCategoriesDropdown = !this.showCategoriesDropdown;
      this.showTagsDropdown = false; // 关闭其他悬浮框
    },
    
    toggleTagsDropdown() {
      this.showTagsDropdown = !this.showTagsDropdown;
      this.showCategoriesDropdown = false; // 关闭其他悬浮框
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
}

.header {
  text-align: center;
  padding: 40px 0 30px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 40px;
}

.site-title {
  font-size: 2.5rem;
  margin-bottom: 30px;
  background: none;
  -webkit-background-clip: initial;
  -webkit-text-fill-color: initial;
  background-clip: initial;
  font-weight: 300;
  letter-spacing: 2px;
  color: #000;
}

.main-nav-buttons ul {
  display: flex;
  justify-content: center;
  gap: 40px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.main-nav-buttons a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  padding: 12px 20px;
  display: block;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-size: 1rem;
  font-weight: 500;
  position: relative;
}

.main-nav-buttons a:hover,
.main-nav-buttons a.active {
  color: #fff;
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.floating-indicator {
  position: absolute;
  bottom: -2px; /* 改为下划线 */
  height: 3px;
  background: linear-gradient(45deg, #999, rgba(153, 153, 153, 0.7)); /* 改为更浅的灰色 */
  border-radius: 2px;
  transition: all 0.3s ease;
  opacity: 1;
  z-index: 10;
  pointer-events: none;
}

.content-wrapper {
  flex: 1;
  display: flex;
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.left-sidebar {
  width: 250px;
  flex-shrink: 0;
  margin-left: -60px;
}

.categories-section, .tags-section {
  margin-bottom: 30px;
  position: relative;
}

.categories-section h3, .tags-section h3 {
  color: #fff;
  margin-bottom: 15px;
  font-size: 1.1rem;
  font-weight: 500;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding-bottom: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.categories-section h3:hover, .tags-section h3:hover {
  color: rgba(255, 255, 255, 0.8);
}

.dropdown-container {
  position: relative;
}

.categories-list, .tags-cloud {
  position: absolute;
  top: 0;
  left: 100%;
  background: rgba(0, 0, 0, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  padding: 20px;
  min-width: 200px;
  z-index: 1000;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
  transition: all 0.3s ease;
  opacity: 0;
  visibility: hidden;
  transform: translateX(-10px);
}

.categories-list {
  margin-left: -160px; /* 调整为与标签悬浮框相同的偏移量，使其在同一条垂直线上 */
}

.tags-cloud {
  margin-left: -160px; /* 标签悬浮框往左移动 */
  margin-top: -20px; /* 标签悬浮框往上移动 */
}
.categories-list.show, .tags-cloud.show {
  opacity: 1;
  visibility: visible;
  transform: translateX(0);
}

.categories-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.categories-list li {
  margin-bottom: 10px;
}

.categories-list a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.categories-list a:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}

/* 添加分类选中状态样式 */
.categories-list a.active {
  background: rgba(255, 105, 180, 0.2);
  color: #ff69b4;
  border-color: rgba(255, 105, 180, 0.4);
  font-weight: 600;
}

.category-count {
  background: rgba(255, 255, 255, 0.2);
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8rem;
}

.tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  background: rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.8);
  padding: 6px 12px;
  border-radius: 20px;
  text-decoration: none;
  font-size: 0.9rem;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.tag:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  transform: translateY(-1px);
}

/* 添加标签选中状态样式 */
.tag.active {
  background: rgba(255, 105, 180, 0.3);
  color: #ff69b4;
  border-color: rgba(255, 105, 180, 0.5);
  font-weight: 600;
}

.main-content {
  flex: 1;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.news-item {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 15px;
  overflow: hidden;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}

.news-item:hover {
  transform: translateY(-5px);
  border-color: rgba(255, 255, 255, 0.3);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.news-item.large {
  grid-column: span 2;
  display: flex;
}

.news-item.large .post-image {
  width: 50%;
  height: auto;
}

.post-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.news-content {
  padding: 25px;
}

.news-content h3 {
  color: #fff;
  margin-bottom: 15px;
  font-size: 1.3rem;
  line-height: 1.4;
}

.news-content p {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  margin-bottom: 20px;
}

.meta-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.9rem;
  margin-bottom: 20px;
}

.read-more {
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.2));
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 10px 20px;
  border-radius: 8px;
  text-decoration: none;
  display: inline-block;
  transition: all 0.3s ease;
  cursor: pointer;
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
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  background: transparent;
  /* 确保无边框和背景 */
  border: none;
  outline: none;
  box-shadow: none;
  padding: 0;
  margin: 0;
}

.main-nav-buttons ul {
  display: flex;
  justify-content: center;
  gap: 20px; /* 缩短导航栏间距 */
  list-style: none;
  margin: 0;
  padding: 0;
}

.main-nav-buttons a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  padding: 12px 15px; /* 缩短导航栏内边距 */
  display: block;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-size: 1rem;
  font-weight: 500;
  position: relative;
  background: transparent; /* 去掉半透明背景 */
  border: none;
  outline: none;
  box-shadow: none;
}

.main-nav-buttons a:hover,
.main-nav-buttons a.active {
  color: #fff;
  background: transparent; /* 去掉悬停时的半透明背景 */
  transform: translateY(-1px);
}

.no-border-btn {
  background: transparent;
  border: none;
  outline: none;
  box-shadow: none;
}

.floating-indicator {
  position: absolute;
  bottom: -2px; /* 改为下划线 */
  height: 3px;
  background: linear-gradient(45deg, #000, rgba(0, 0, 0, 0.7));
  border-radius: 2px;
  transition: all 0.3s ease;
  opacity: 1;
  z-index: 10;
  pointer-events: none;
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
    padding: 0 20px;
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

/* 确保悬浮框相关样式不影响直接显示 */
/* 移除强制隐藏的样式，让悬浮框可以正常显示 */
/* .dropdown-container,
.dropdown-content,
.categories-dropdown,
.tags-dropdown {
  display: none !important;
} */

.floating-indicator {
  opacity: 1 !important;
}
</style>