<template>
  <div class="home">
    <header class="header">
      <h1 class="site-title">rann的小试间</h1>
    </header>
    
    <!-- 中心导航按钮 -->
    <div class="center-nav">
      <nav class="main-nav-buttons">
        <ul>
          <li><a href="/" class="no-border-btn" :class="{ active: currentRoute === '/' }" @click.prevent="setActiveRoute('/')">首页</a></li>
          <li><a href="/blog" class="no-border-btn" :class="{ active: currentRoute === '/blog' }" @click.prevent="setActiveRoute('/blog')">博客</a></li>
          <li><a href="/blog/create" class="no-border-btn" :class="{ active: currentRoute === '/blog/create' }" @click.prevent="setActiveRoute('/blog/create')">发布</a></li>
        </ul>
        <!-- 游走悬浮按键 -->
        <div class="floating-indicator" :style="floatingStyle" v-if="showFloating"></div>
      </nav>
    </div>
    
    <div class="content-wrapper">
      <aside class="left-sidebar">
        <nav class="main-nav">
          <ul>
            <li><a href="#">分类</a></li>
            <li><a href="#">关于</a></li>
            <li><a href="#">联系</a></li>
            <li class="dropdown-container">
              <a href="#" class="dropdown-trigger" @mouseenter="showCategories = true" @mouseleave="startHideCategories()">文章分类</a>
              <div class="dropdown-content" v-show="showCategories" @mouseenter="cancelHideCategories()" @mouseleave="startHideCategories()">
                <ul class="categories-list">
                  <li><a href="#">时尚趋势</a> <span class="category-count">12</span></li>
                  <li><a href="#">搭配技巧</a> <span class="category-count">8</span></li>
                  <li><a href="#">配饰指南</a> <span class="category-count">5</span></li>
                  <li><a href="#">品牌故事</a> <span class="category-count">6</span></li>
                  <li><a href="#">时尚事件</a> <span class="category-count">4</span></li>
                </ul>
              </div>
            </li>
            <li class="dropdown-container">
              <a href="#" class="dropdown-trigger" @mouseenter="showTags = true" @mouseleave="startHideTags()">热门标签</a>
              <div class="dropdown-content tags-dropdown" v-show="showTags" @mouseenter="cancelHideTags()" @mouseleave="startHideTags()">
                <div class="tags-cloud">
                  <a href="#" class="tag">春季时尚</a>
                  <a href="#" class="tag">穿搭技巧</a>
                  <a href="#" class="tag">流行趋势</a>
                  <a href="#" class="tag">配饰搭配</a>
                  <a href="#" class="tag">品牌推荐</a>
                  <a href="#" class="tag">时尚博主</a>
                  <a href="#" class="tag">潮流单品</a>
                  <a href="#" class="tag">街头风格</a>
                </div>
              </div>
            </li>
          </ul>
        </nav>
      </aside>
      
      <main class="main-content">
        <section class="featured-post">
          <div class="post-card featured">
            <div class="post-image">
              <img src="/images/featured-fashion.svg" alt="2027春季时尚趋势 - 粉色针织马甲" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div class="post-content">
              <div class="post-meta">
                <span class="post-category">时尚趋势</span>
                <span class="post-date">2027-10-15</span>
              </div>
              <h2 class="post-title">2027年春季时尚趋势预测</h2>
              <p class="post-excerpt">探索2027年春季最热门的时尚趋势，从服装到配饰，让你的衣橱焕然一新。</p>
              <a href="/post/1" class="read-more">阅读更多</a>
            </div>
          </div>
        </section>
        
        <!-- 时尚新闻区域 -->
        <section class="fashion-news">
          <h2 class="section-title">时尚资讯</h2>
          <div class="news-grid">
            <div class="news-item" v-for="(news, index) in fashionNews" :key="index">
              <div class="news-image">
                <div class="placeholder" :style="{ backgroundColor: '#' + (Math.random() * 0xFFFFFF << 0).toString(16) }">
                  {{ news.category }}
                </div>
              </div>
              <div class="news-content">
                <div class="news-meta">
                  <span class="news-category">{{ news.category }}</span>
                  <span class="news-date">{{ news.date }}</span>
                </div>
                <h3 class="news-title">{{ news.title }}</h3>
                <p class="news-excerpt">{{ news.excerpt }}</p>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
    
    <footer class="footer">
      <p>&copy; 2027 服装品牌. 保留所有权利.</p>
      <div class="social-links">
        <a href="#">Instagram</a>
        <a href="#">Facebook</a>
        <a href="#">Twitter</a>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      searchQuery: '',
      currentRoute: '/', // 当前活动路由
      // 游走悬浮按键相关数据
      showFloating: false,
      floatingStyle: {
        width: '60px',
        transform: 'translateX(0px)',
        transition: 'all 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55)'
      },
      floatingInterval: null,
      // 浮框显示状态
      showCategories: false,
      showTags: false,
      hideCategoriesTimer: null,
      hideTagsTimer: null,
      fashionNews: [
        {
          category: '时装周',
          title: '2027年巴黎时装周亮点',
          date: '2027-10-12',
          excerpt: '巴黎时装周带来了令人惊艳的设计，展示了未来时尚的新趋势和可能性。'
        },
        {
          category: '品牌动态',
          title: '新兴环保品牌崛起',
          date: '2027-10-08',
          excerpt: '越来越多品牌开始关注可持续发展，推出环保时尚产品系列。'
        },
        {
          category: '潮流预测',
          title: '春季流行色彩指南',
          date: '2027-10-05',
          excerpt: '从温暖的大地色系到清新的薄荷绿，了解2027春季的流行色彩。'
        }
      ]
    }
  },
  mounted() {
    // 初始化指示器位置
    this.updateIndicator()
    // 监听窗口大小变化，重新计算指示器位置
    window.addEventListener('resize', this.updateIndicator)
    // 延迟启动游走悬浮按键效果，确保DOM完全渲染
    setTimeout(() => {
      this.startFloatingAnimation()
    }, 500)
  },
  beforeUnmount() {
    // 清理事件监听器
    window.removeEventListener('resize', this.updateIndicator)
    // 清理游走动画
    this.stopFloatingAnimation()
    // 清理定时器
    this.clearAllTimers()
  },
  methods: {
    updateIndicator() {
      this.$nextTick(() => {
        const activeLink = this.$el.querySelector('.main-nav-buttons a.active')
        if (activeLink) {
          const linkRect = activeLink.getBoundingClientRect()
          const containerRect = this.$el.querySelector('.main-nav-buttons ul').getBoundingClientRect()
          
          this.indicatorStyle = {
            width: `${linkRect.width}px`,
            transform: `translateX(${linkRect.left - containerRect.left}px)`,
            transition: 'all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)'
          }
        }
      })
    },
    setActiveRoute(route) {
      this.currentRoute = route
      // 点击任何按钮时都启动游走效果
      this.startFloatingAnimation()
    },
    // 启动游走悬浮按键动画
    startFloatingAnimation() {
      console.log('启动游走悬浮按键动画')
      this.showFloating = true
      this.stopFloatingAnimation() // 先停止之前的动画
      
      // 使用$nextTick确保DOM更新完成
      this.$nextTick(() => {
        const buttons = this.$el.querySelectorAll('.main-nav-buttons a')
        console.log('找到按钮数量:', buttons.length)
        if (buttons.length === 0) {
          console.log('未找到导航按钮')
          return
        }
        
        let currentIndex = 0
        
        // 立即移动到第一个按钮
        this.moveToButton(buttons, currentIndex)
        console.log('移动到按钮:', currentIndex)
        
        this.floatingInterval = setInterval(() => {
          currentIndex = (currentIndex + 1) % buttons.length
          this.moveToButton(buttons, currentIndex)
          console.log('移动到按钮:', currentIndex)
        }, 1500) // 每1.5秒移动一次
      })
    },
    // 移动到指定按钮
    moveToButton(buttons, index) {
      const button = buttons[index]
      if (!button) return
      
      const buttonRect = button.getBoundingClientRect()
      const container = this.$el.querySelector('.main-nav-buttons ul')
      if (!container) return
      
      const containerRect = container.getBoundingClientRect()
      
      this.floatingStyle = {
        width: `${buttonRect.width}px`,
        transform: `translateX(${buttonRect.left - containerRect.left}px)`,
        transition: 'all 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55)'
      }
    },
    // 停止游走动画
    stopFloatingAnimation() {
      if (this.floatingInterval) {
        clearInterval(this.floatingInterval)
        this.floatingInterval = null
      }
    },
    // 清理所有定时器
    clearAllTimers() {
      if (this.hideCategoriesTimer) {
        clearTimeout(this.hideCategoriesTimer)
        this.hideCategoriesTimer = null
      }
      if (this.hideTagsTimer) {
        clearTimeout(this.hideTagsTimer)
        this.hideTagsTimer = null
      }
    },
    // 开始隐藏分类浮框（延迟）
    startHideCategories() {
      this.hideCategoriesTimer = setTimeout(() => {
        this.showCategories = false
      }, 300)
    },
    // 取消隐藏分类浮框
    cancelHideCategories() {
      if (this.hideCategoriesTimer) {
        clearTimeout(this.hideCategoriesTimer)
        this.hideCategoriesTimer = null
      }
    },
    // 开始隐藏标签浮框（延迟）
    startHideTags() {
      this.hideTagsTimer = setTimeout(() => {
        this.showTags = false
      }, 300)
    },
    // 取消隐藏标签浮框
    cancelHideTags() {
      if (this.hideTagsTimer) {
        clearTimeout(this.hideTagsTimer)
        this.hideTagsTimer = null
      }
    }
  }
}
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
  justify-content: center !important; /* 标题居中 */
  align-items: center !important;
  padding: 25px 40px !important;
  position: relative !important;
  margin-bottom: 0 !important;
  /* 完全去掉背景，避免与全局背景叠加产生边界 */
  background: transparent !important;
  background-image: none !important;
  background-blend-mode: normal !important;
  /* 强制去掉所有边框和边界效果 */
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
  /* 整体透明度 */
  opacity: 1 !important;
  /* 过渡动画 */
  transition: all 0.3s ease !important;
  /* 确保没有任何边框相关的样式 */
  clip: auto !important;
  overflow: visible !important;
}

.site-title {
  font-size: 2rem !important; /* 减小字体大小 */
  margin: 0 0 0 0;
  background: linear-gradient(90deg, #ff94d2, #b388eb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.8), 0 0 40px rgba(255, 148, 210, 0.5), 0 0 60px rgba(255, 148, 210, 0.3);
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
  margin-bottom: 20px;
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
  /* 去掉黑色透明边框 */
  border: none;
  position: relative;
  overflow: hidden;
}

.main-nav a::before {
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

.main-nav a:hover {
  background: transparent;
  color: #ff69b4;
}

.search-section, .categories-section, .tags-section {
  margin-top: 30px;
}

.search-section h3, .categories-section h3, .tags-section h3 {
  font-size: 1.2rem;
  margin-bottom: 15px;
  color: #fff;
  /* 去掉白色透明边框 */
  border-bottom: none;
  padding-bottom: 8px;
}

.search-form {
  display: flex;
  gap: 10px;
}

.search-input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.search-button {
  padding: 8px 16px;
  background: rgba(255, 105, 180, 0.8);
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s;
}

.search-button:hover {
  background: rgba(255, 105, 180, 1);
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
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.post-image {
  flex: 0 0 300px;
  height: 200px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
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
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.news-item {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s;
}

.news-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.news-image {
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

/* 中心导航按钮样式 */
.center-nav {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px 0;
  margin-bottom: 20px;
  background: transparent;
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
}

.main-nav-buttons ul {
  display: flex;
  list-style: none;
  gap: 1em; /* 一个字的间隙 */
  margin: 0;
  padding: 0;
  justify-content: center;
}

/* 使用更具体的选择器确保样式生效 */
.home .center-nav .main-nav-buttons a {
  text-decoration: none;
  color: #fff;
  font-weight: 600;
  font-size: 1.1rem;
  padding: 12px 25px;
  border-radius: 25px;
  background: transparent; /* 完全透明背景 */
  /* 彻底清除所有可能的边框样式 */
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
  transition: all 0.3s ease;
  backdrop-filter: none; /* 移除模糊效果 */
  /* 添加额外的边框清除属性 */
  border-width: 0 !important;
  border-style: none !important;
  border-color: transparent !important;
  /* 确保字体清晰显示 - 使用淡紫色 */
  text-shadow: 0 0 8px rgba(147, 112, 219, 0.8), 0 0 16px rgba(147, 112, 219, 0.5);
  font-weight: 700; /* 加粗字体 */
}

/* 悬停状态 */
.home .center-nav .main-nav-buttons a:hover {
  background: rgba(255, 105, 180, 0.2); /* 悬停时添加淡粉色半透明背景 */
  color: #fff;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4) !important;
  /* 悬停时也确保无边框 */
  border: none !important;
  outline: none !important;
  /* 添加额外的边框清除属性 */
  border-width: 0 !important;
  border-style: none !important;
  border-color: transparent !important;
  /* 增强悬停时的字体阴影 - 使用更亮的淡紫色 */
  text-shadow: 0 0 10px rgba(186, 85, 211, 0.9), 0 0 20px rgba(147, 112, 219, 0.6);
}

/* 活动状态按钮样式 */
.home .center-nav .main-nav-buttons a.active {
  background: rgba(255, 105, 180, 0.1) !important;
  color: #fff !important;
  /* 活动状态时保持无边框 */
  border: none !important;
  outline: none !important;
  text-shadow: 0 0 10px rgba(186, 85, 211, 0.8), 0 0 20px rgba(147, 112, 219, 0.4);
}

/* 游走悬浮按键样式 */
.floating-indicator {
  position: absolute;
  height: 100%;
  background: transparent; /* 完全透明背景 */
  border: none; /* 去掉边框 */
  border-radius: 25px; /* 圆角，与按钮保持一致 */
  pointer-events: none; /* 不影响点击事件 */
  z-index: 0; /* 位于按钮下方 */
  top: 0;
  left: 0;
  box-shadow: none; /* 去掉发光效果 */
}

/* 脉冲动画效果 */
@keyframes pulse {
  0% {
    box-shadow: none;
    transform: scale(1);
  }
  50% {
    box-shadow: none;
    transform: scale(1);
  }
  100% {
    box-shadow: none;
    transform: scale(1);
  }
}

/* 确保正确的层级关系 */
.main-nav-buttons {
  position: relative;
}

.main-nav-buttons ul {
  position: relative;
  z-index: 2; /* 按钮在最上层 */
}

.floating-indicator {
  z-index: 0; /* 金色游走按键在按钮下方 */
}
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  font-family: 'Microsoft YaHei', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: 
    radial-gradient(circle at 25% 25%, rgba(168, 230, 207, 0.8) 0%, rgba(168, 230, 207, 0.3) 35%, transparent 60%),
    radial-gradient(circle at 75% 75%, rgba(255, 211, 182, 0.8) 0%, rgba(255, 211, 182, 0.3) 35%, transparent 60%);
}

/* 左侧导航样式 */
.left-sidebar {
  width: 250px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  z-index: 10; /* 增加左侧边栏的层级 */
}

.main-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.main-nav li {
  margin-bottom: 8px;
  position: relative;
}

.main-nav a {
  display: block;
  text-decoration: none;
  color: #fff;
  padding: 12px 15px;
  border-radius: 8px;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.main-nav a:hover {
  background: rgba(255, 105, 180, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
}

/* 下拉菜单容器 */
.dropdown-container {
  position: relative;
}

.dropdown-trigger {
  cursor: pointer;
  position: relative;
}

/* 下拉内容样式 */
.dropdown-content {
  position: absolute;
  top: 100%;
  left: 0;
  width: 280px;
  background: linear-gradient(135deg, 
    rgba(255, 105, 180, 0.15) 0%, 
    rgba(255, 255, 255, 0.1) 50%, 
    rgba(168, 230, 207, 0.1) 100%);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  padding: 15px;
  z-index: 1000;
  box-shadow: 
    0 10px 30px rgba(255, 105, 180, 0.2),
    0 5px 15px rgba(168, 230, 207, 0.1);
  backdrop-filter: blur(20px);
  animation: fadeIn 0.3s ease;
}

.tags-dropdown {
  width: 320px;
}

/* 下拉菜单动画 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 分类列表样式 */
.categories-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.categories-list li {
  margin-bottom: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 6px;
  padding: 8px 12px;
  transition: all 0.3s ease;
}

.categories-list li:hover {
  background: rgba(255, 105, 180, 0.1);
  transform: translateX(3px);
}

.categories-list a {
  background: none;
  border: none;
  padding: 0;
  color: #fff;
  text-decoration: none;
  transition: all 0.3s ease;
  flex-grow: 1;
}

.categories-list a:hover {
  color: #ff69b4;
}

.category-count {
  background: rgba(255, 105, 180, 0.3);
  color: #fff;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8rem;
  min-width: 30px;
  text-align: center;
}

/* 标签云样式 */
.tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  display: inline-block;
  background: linear-gradient(135deg, 
    rgba(255, 105, 180, 0.2) 0%, 
    rgba(255, 255, 255, 0.1) 100%);
  color: #fff;
  padding: 4px 12px;
  border-radius: 15px;
  text-decoration: none;
  font-size: 0.85rem;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.tag:hover {
  background: linear-gradient(135deg, 
    rgba(255, 105, 180, 0.4) 0%, 
    rgba(255, 255, 255, 0.2) 100%);
  transform: translateY(-2px);
  box-shadow: 0 3px 10px rgba(255, 105, 180, 0.3);
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
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.post-image {
  flex: 0 0 300px;
  height: 200px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
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
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.news-item {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s;
}

.news-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.news-image {
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
</style>