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
      }
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
  border: none !important;
  border-style: none !important;
  border-width: 0 !important;
  border-color: transparent !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  outline: none !important;
  outline-width: 0 !important;
  outline-style: none !important;
  outline-color: transparent !important;
  opacity: 1 !important;
  transition: all 0.3s ease !important;
  clip: auto !important;
  overflow: visible !important;
}

.site-title {
  font-size: 2rem !important;
  margin: 0 0 0 0;
  background: linear-gradient(90deg, #ff94d2, #b388eb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  /* 移除光晕效果 */
  text-shadow: none;
  font-weight: bold;
  z-index: 10;
  position: relative;
  opacity: 1;
  filter: none;
  display: inline-block;
  padding: 10px 0;
  margin-right: -5px;
}

.top-nav ul {
  display: flex;
  list-style: none;
  gap: 20px;
  margin: 0;
  padding: 0;
}

.top-nav {
  margin-left: auto;
}

.top-nav a {
  text-decoration: none;
  color: #fff;
  font-weight: 500;
  transition: all 0.3s;
  padding: 8px 15px;
  border-radius: 4px;
  background: transparent;
  /* 去掉黑色透明边框 */
  border: none;
  position: relative;
  overflow: hidden;
}

.top-nav a::before {
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
  animation: shimmer 3s infinite;
}

.top-nav a:hover {
  color: #ff69b4;
}

.content-wrapper {
  display: flex;
  gap: 50px;
  padding: 40px 0;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.left-sidebar {
  flex: 0 0 350px; /* 左侧导航栏固定宽度 */
  background: transparent;
  padding: 25px;
  border-radius: 8px;
  min-height: fit-content;
  min-width: 0; /* 防止内容溢出 */
  /* 去掉黑色透明边框 */
  border: none;
}

.main-content {
  flex: 1; /* 主内容区域占据剩余空间 */
  box-sizing: border-box;
}

.main-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.main-nav li {
  margin-bottom: 8px;
}

.main-nav a {
  display: block;
  text-decoration: none;
  color: #fff;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 10px 15px;
  border-radius: 4px;
  transition: all 0.3s;
  background: transparent;
  border: none;
  position: relative;
  overflow: hidden;
}

/* 点击选中后的悬浮边框效果 - 明显的变色边框 */
.main-nav a.selected {
  background: rgba(255, 105, 180, 0.1);
  color: #ff69b4;
  border: 3px solid #ff69b4;
  box-shadow: 
    0 0 20px rgba(255, 105, 180, 0.6),
    0 0 40px rgba(255, 105, 180, 0.3),
    inset 0 0 15px rgba(255, 105, 180, 0.1);
}

/* 悬停状态 - 无边框，只有文字颜色变化 */
.main-nav a:hover {
  background: transparent;
  color: #ff69b4;
  border: none;
  box-shadow: none;
}

/* 点击状态 */
.main-nav a:active {
  background: transparent;
  color: #ff69b4;
  border: none;
}

/* 焦点状态 */
.main-nav a:focus {
  background: transparent;
  color: #fff;
  outline: none;
  border: none;
}

/* 下拉菜单容器 */
.dropdown-container {
  position: relative;
  display: block; /* 改为block以确保垂直排列 */
}

/* 下拉菜单内容样式 - 修改为紧贴文章分类条目下方 */
.dropdown-content {
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  border-radius: 8px;
  padding: 15px;
  z-index: 1000;
  min-width: 200px;
  max-height: 300px;
  overflow-y: auto;
}

.categories-dropdown {
  left: 35% !important; /* 往右移动一点 */
  top: 5px !important; /* 往下移动一点 */
  margin-left: 5px !important;
}

.tags-dropdown {
  left: 32% !important; /* 往右移动一点点 */
  top: 95% !important; /* 往上移动一点点 */
  margin-left: 5px !important;
}

/* 文章分类列表样式，一行显示两个 */
.category-list {
  display: grid;
  grid-template-columns: 1fr 1fr; /* 一行两列 */
  gap: 8px;
  min-width: 180px;
}

.category-list a {
  display: block;
  padding: 8px 12px;
  text-decoration: none;
  color: #333;
  border-radius: 5px;
  transition: background-color 0.3s;
  font-size: 14px;
  white-space: nowrap;
  overflow: visible;
  text-overflow: clip;
}

.category-list a:hover {
  background-color: #f0f0f0;
}

/* 为热门标签中的标签应用特定样式 */
.tags-dropdown .category-list .tag {
  padding: 5px 10px;
  background-color: #f0f0f0;
  border-radius: 15px;
  text-decoration: none;
  font-size: 13px;
  color: #333;
  transition: all 0.3s;
  white-space: nowrap;
}

.tags-dropdown .category-list .tag:hover {
  background-color: #ddd;
}

/* 标签云样式 */
.tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.tags-cloud a {
  padding: 5px 10px;
  background-color: #f0f0f0;
  border-radius: 15px;
  text-decoration: none;
  font-size: 13px;
  color: #333;
  transition: all 0.3s;
}

.tags-cloud a:hover {
  background-color: #ddd;
}
.categories-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.categories-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  padding: 8px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.categories-list a {
  text-decoration: none;
  color: #fff;
  transition: all 0.3s;
}

.categories-list a:hover {
  color: #ff69b4;
}

.category-count {
  background: rgba(255, 105, 180, 0.8);
  color: #fff;
  padding: 2px 6px;
  border-radius: 10px;
  font-size: 0.8rem;
}

.tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  text-decoration: none;
  color: #fff;
  background: rgba(255, 255, 255, 0.1);
  padding: 4px 8px;
  border-radius: 3px;
  font-size: 0.9rem;
  transition: all 0.3s;
}

.tag:hover {
  background: rgba(255, 105, 180, 0.8);
}

.featured-post {
  margin-bottom: 40px;
}

.post-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s;
}

.post-card.featured {
  display: flex;
  gap: 20px;
}

.post-card:hover {
  /* 保持空白，不执行任何悬停效果 */
}

.post-image {
  flex: 0 0 300px;
  height: 200px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden; /* 确保图片容器有overflow: hidden，防止放大时溢出 */
  position: relative;
}

.post-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease; /* 为图片添加过渡效果 */
}

.post-image img:hover {
  transform: scale(1.05); /* 图片单独放大 */
}

.post-content {
  flex: 1;
  padding: 20px;
}

.post-meta {
  display: flex;
  gap: 15px;
  margin-bottom: 10px;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.7);
}

.post-category {
  background: rgba(255, 105, 180, 0.8);
  padding: 2px 8px;
  border-radius: 3px;
  color: #fff;
}

.post-title {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #fff;
}

.post-excerpt {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  margin-bottom: 15px;
}

.read-more {
  color: #ff69b4;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s;
}

.read-more:hover {
  color: #fff;
}

.fashion-news {
  margin-bottom: 40px;
}

.section-title {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: #fff;
}

.news-grid {
  display: flex;
  gap: 8px; /* 进一步减小间隙 */
  min-height: 400px; /* 进一步降低最小高度 */
}

.news-grid-right {
  display: flex;
  flex-direction: column;
  gap: 8px; /* 进一步减小间隙 */
  flex: 1; /* 右侧区域占剩余空间的1份 */
}

/* 大内容浮框样式 - 更浮夸的设计 */
.news-item.large {
  flex: 1.2; /* 进一步调整为1.2份空间，使宽度进一步缩小 */
  background: linear-gradient(135deg, rgba(255, 105, 180, 0.1), rgba(179, 136, 235, 0.1));
  border-radius: 12px; /* 稍微减小圆角 */
  overflow: hidden;
  transition: all 0.4s ease;
  box-shadow: 
    0 8px 25px rgba(255, 105, 180, 0.25),
    inset 0 0 12px rgba(255, 105, 180, 0.15);
  border: 2px solid rgba(255, 105, 180, 0.35);
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  /* 设置为正方形，宽高比为1:1 */
  aspect-ratio: 1 / 1;
}

/* 时装周大板块图片样式 - 图片占据更大比例 */
.news-item.large .news-image {
  flex: 1; /* 图片区域占据剩余空间的大部分 */
  height: auto;
  min-height: 65%; /* 增加图片区域最小高度至65% */
  max-height: 75%; /* 最大高度调整为75% */
}

.news-item.large .news-content {
  flex: 0 0 auto; /* 内容区域不伸缩 */
  padding: 6px; /* 适当增加内边距，改善视觉效果 */
  min-height: 20%; /* 减少内容区域高度占比，为图片留出更多空间 */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  overflow: hidden; /* 防止内容溢出 */
}

.news-item.large .news-excerpt {
  font-size: 0.8rem; /* 稍微减小字体以适应更多内容 */
  line-height: 1.4; /* 紧凑行间距 */
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 最多显示3行 */
  -webkit-box-orient: vertical;
}

.news-item.small {
  flex: 1; /* 每个小板块占1份空间 */
  background: linear-gradient(135deg, rgba(179, 136, 235, 0.1), rgba(255, 105, 180, 0.1));
  border-radius: 10px; /* 稍微减小圆角 */
  overflow: hidden;
  transition: all 0.4s ease;
  box-shadow: 
    0 6px 16px rgba(179, 136, 235, 0.25),
    inset 0 0 8px rgba(179, 136, 235, 0.15);
  border: 1px solid rgba(179, 136, 235, 0.35);
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  /* 大板块高度 = 2 * 小板块高度 + 1个gap */
  /* 调整后高度 */
  min-height: 90px; /* 进一步缩小小板块高度 */
}

.news-item.small::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, 
    transparent 0%, 
    rgba(179, 136, 235, 0.1) 25%, 
    transparent 50%, 
    rgba(255, 105, 180, 0.1) 75%, 
    transparent 100%);
  z-index: -1;
  animation: shine 6s infinite;
}

/* 悬停效果 - 更浮夸 */
.news-item.large:hover,
.news-item.small:hover {
  /* 移除所有悬停效果，包括向上移动和阴影变化 */
}

/* 图片单独放大效果 */
.news-image img:hover {
  transform: scale(1.05); /* 图片单独放大 */
  transition: transform 0.4s ease;
}

/* 确保图片容器有overflow: hidden，防止放大时溢出 */
.news-image {
  overflow: hidden;
  position: relative;
  height: 150px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.placeholder {
  color: rgba(255, 255, 255, 0.7);
  font-size: 1rem;
}

.news-content {
  padding: 15px;
}

.news-meta {
  display: flex;
  gap: 10px;
  margin-bottom: 8px;
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.7);
}

.news-category {
  background: rgba(255, 105, 180, 0.8);
  padding: 1px 6px;
  border-radius: 3px;
  color: #fff;
}

.news-title {
  font-size: 1.1rem;
  margin-bottom: 8px;
  color: #fff;
}

.news-excerpt {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.5;
  font-size: 0.9rem;
}

.footer {
  text-align: center;
  padding: 20px;
  margin-top: 40px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
}

.social-links {
  margin-top: 10px;
}

.social-links a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  margin: 0 10px;
  transition: all 0.3s;
}

.social-links a:hover {
  color: #ff69b4;
}

/* 中心导航按钮样式 - 在标题下方 */
.main-nav-buttons {
  margin-top: 20px; /* 与标题保持距离 */
  width: 100%;
  display: flex;
  justify-content: center;
  position: relative;
}

.main-nav-buttons ul {
  display: flex;
  list-style: none;
  gap: 30px;
  margin: 0;
  padding: 0;
  justify-content: center;
}

.main-nav-buttons li {
  margin: 0;
}

.main-nav-buttons {
  margin-top: 20px; /* 与标题保持距离 */
  width: 100%;
  display: flex;
  justify-content: center;
  position: relative;
}

.main-nav-buttons ul {
  position: relative;
  z-index: 1;
}

.main-nav-buttons a {
  text-decoration: none;
  color: #fff;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 10px 20px;
  border-radius: 4px;
  transition: all 0.3s;
  background: transparent;
  border: none;
  position: relative;
}

.main-nav-buttons a:hover {
  background: transparent; /* 移除悬停时的半透明背景 */
  color: #ff69b4;
}

.main-nav-buttons a.active {
  /* 移除半透明背景，只保留字体颜色变化 */
  background: transparent;
  color: #ff69b4;
  border-bottom: 2px solid #ff69b4;
}

/* 动态上划线指示器 */
.floating-indicator {
  position: absolute;
  height: 2px;
  background: #ff69b4;
  border-radius: 2px;
  top: 0; /* 改为顶部，实现上划线效果 */
  width: 0;
  opacity: 0;
  transition: all 0.3s ease;
  box-shadow: 0 0 8px rgba(255, 105, 180, 0.6);
}

</style>