<template>
  <div class="home">
    <header class="header">
      <h1 class="site-title">rann的小试间</h1>
      
      <!-- 导航按钮 - 紧贴标题正下方 -->
      <nav class="main-nav-buttons">
        <ul>
          <li><a href="/" class="no-border-btn" :class="{ active: currentRoute === '/' }" @click.prevent="setActiveRoute('/')">首页</a></li>
          <li><a href="/blog" class="no-border-btn" :class="{ active: currentRoute === '/blog' }" @click.prevent="setActiveRoute('/blog')">博客</a></li>
          <li><a href="/blog/create" class="no-border-btn" :class="{ active: currentRoute === '/blog/create' }" @click.prevent="setActiveRoute('/blog/create')">发布</a></li>
        </ul>
        <!-- 动态上划线指示器 -->
        <div class="floating-indicator" :style="indicatorStyle"></div>
      </nav>
    </header>
    
    <div class="content-wrapper">
      <aside class="left-sidebar">
        <nav class="main-nav">
          <ul>
            <li><a href="#" :class="{ selected: selectedItem === 'category' }" @click.prevent="selectItem('category')">分类</a></li>
            <li><a href="#" :class="{ selected: selectedItem === 'about' }" @click.prevent="selectItem('about')">关于</a></li>
            <li><a href="#" :class="{ selected: selectedItem === 'contact' }" @click.prevent="selectItem('contact')">联系</a></li>
            <li class="dropdown-container">
              <a href="#" class="dropdown-trigger" :class="{ selected: selectedItem === 'categories' }" @click.prevent="selectItem('categories')" @mouseenter="showCategories = true" @mouseleave="startHideCategories()">文章分类</a>
              <div class="dropdown-content categories-dropdown" v-show="showCategories" @mouseenter="cancelHideCategories()" @mouseleave="startHideCategories()">
                <div class="category-list">
                  <a href="#" class="category-item">时尚趋势 <span class="category-count">12</span></a>
                  <a href="#" class="category-item">搭配技巧 <span class="category-count">8</span></a>
                  <a href="#" class="category-item">配饰指南 <span class="category-count">5</span></a>
                  <a href="#" class="category-item">品牌故事 <span class="category-count">6</span></a>
                  <a href="#" class="category-item">时尚事件 <span class="category-count">4</span></a>
                  <a href="#" class="category-item">美妆护肤 <span class="category-count">9</span></a>
                </div>
              </div>
            </li>
            <li class="dropdown-container">
              <a href="#" class="dropdown-trigger" :class="{ selected: selectedItem === 'tags' }" @click.prevent="selectItem('tags')" @mouseenter="showTags = true" @mouseleave="startHideTags()">热门标签</a>
              <div class="dropdown-content tags-dropdown" v-show="showTags" @mouseenter="cancelHideTags()" @mouseleave="startHideTags()">
                <div class="category-list">
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
                <span class="post-date">2026-04-12</span>
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
            <!-- 左侧大内容浮框 -->
            <div class="news-item large">
              <div class="news-image">
                <img src="/images/featured-fashion.svg" alt="巴黎时装周亮点" style="width: 100%; height: 100%; object-fit: cover;">
              </div>
              <div class="news-content">
                <div class="news-meta">
                  <span class="news-category">时装周</span>
                  <span class="news-date">2026-04-12</span>
                </div>
                <h3 class="news-title">2026年巴黎时装周亮点</h3>
                <p class="news-excerpt">巴黎时装周带来了令人惊艳的设计，展示了未来时尚的新趋势和可能性。</p>
              </div>
            </div>
            
            <!-- 右侧两个小内容浮框 -->
            <div class="news-grid-right">
              <div class="news-item small">
                <div class="news-image">
                  <img src="/images/featured-fashion.svg" alt="新兴环保品牌崛起" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <div class="news-content">
                  <div class="news-meta">
                    <span class="news-category">品牌动态</span>
                    <span class="news-date">2026-04-12</span>
                  </div>
                  <h3 class="news-title">新兴环保品牌崛起</h3>
                  <p class="news-excerpt">越来越多品牌开始关注可持续发展，推出环保时尚产品系列。</p>
                </div>
              </div>
              
              <div class="news-item small">
                <div class="news-image">
                  <img src="/images/featured-fashion.svg" alt="春季流行色彩指南" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <div class="news-content">
                  <div class="news-meta">
                    <span class="news-category">潮流预测</span>
                    <span class="news-date">2026-04-12</span>
                  </div>
                  <h3 class="news-title">春季流行色彩指南</h3>
                  <p class="news-excerpt">从温暖的大地色系到清新的薄荷绿，了解2026春季的流行色彩。</p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
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
export default {
  name: 'HomePage',
  data() {
    return {
      searchQuery: '',
      currentRoute: '/', // 当前活动路由
      selectedItem: null, // 当前选中的左边导航项
      // 浮框显示状态
      showCategories: false,
      showTags: false,
      hideCategoriesTimer: null,
      hideTagsTimer: null,
      fashionNews: [
        {
          category: '时装周',
          title: '2026年巴黎时装周亮点',
          date: '2026-04-12',
          excerpt: '巴黎时装周带来了令人惊艳的设计，展示了未来时尚的新趋势和可能性。各大品牌展示了创新的面料和独特的剪裁技术，预示着2027年春夏时尚的新方向。'
        },
        {
          category: '品牌动态',
          title: '新兴环保品牌崛起',
          date: '2026-04-12',
          excerpt: '越来越多品牌开始关注可持续发展，推出环保时尚产品系列。'
        },
        {
          category: '潮流预测',
          title: '春季流行色彩指南',
          date: '2026-04-12',
          excerpt: '从温暖的大地色系到清新的薄荷绿，了解2026春季的流行色彩。'
        },
        {
          category: '搭配技巧',
          title: '职场穿搭必备技巧',
          date: '2026-04-11',
          excerpt: '如何在职场中展现专业又时尚的形象？这里有一些实用的穿搭建议。'
        }
      ],
      // 添加指示器样式数据
      indicatorStyle: {
        width: '0px',
        left: '0px',
        opacity: 0,
        transition: 'all 0.3s ease'
      }
    }
  },
  mounted() {
    // 初始化指示器位置（如果存在indicatorStyle）
    this.updateIndicator()
    // 监听窗口大小变化，重新计算指示器位置
    window.addEventListener('resize', this.updateIndicator)
    
    // 为导航按钮添加鼠标移动事件监听器
    const navLinks = document.querySelectorAll('.main-nav-buttons a')
    const navContainer = document.querySelector('.main-nav-buttons ul')
    
    if (navLinks && navContainer) {
      navLinks.forEach(link => {
        link.addEventListener('mouseenter', (e) => {
          this.updateIndicatorPosition(e.target)
        })
      })
      
      // 在导航容器上监听鼠标离开事件，隐藏指示器
      navContainer.addEventListener('mouseleave', () => {
        this.indicatorStyle.opacity = 0
      })
    }
  },
  beforeUnmount() {
    // 清理定时器
    this.clearAllTimers()
    // 移除事件监听器
    window.removeEventListener('resize', this.updateIndicator)
  },
  methods: {
    setActiveRoute(route) {
      this.currentRoute = route
      // 更新指示器到当前激活的路由位置
      this.$nextTick(() => {
        const activeLink = document.querySelector('.main-nav-buttons a.active')
        if (activeLink) {
          this.updateIndicatorPosition(activeLink)
          this.indicatorStyle.opacity = 1
        }
      })
    },
    // 更新指示器位置的方法
    updateIndicator() {
      const activeLink = document.querySelector('.main-nav-buttons a.active')
      if (activeLink) {
        this.updateIndicatorPosition(activeLink)
        this.indicatorStyle.opacity = 1
      }
    },
    // 更新指示器到特定元素位置
    updateIndicatorPosition(element) {
      if (element) {
        const rect = element.getBoundingClientRect()
        const containerRect = element.closest('.main-nav-buttons').getBoundingClientRect()
        
        // 计算相对于容器的位置
        this.indicatorStyle.width = `${rect.width}px`
        this.indicatorStyle.left = `${rect.left - containerRect.left}px`
        this.indicatorStyle.opacity = 1
        
        // 添加过渡效果
        this.indicatorStyle.transition = 'all 0.3s ease'
      }
    },
    // 点击选中左边导航项
    selectItem(item) {
      if (this.selectedItem === item) {
        // 如果点击的是已选中的项，则取消选中
        this.selectedItem = null
      } else {
        // 选中新的项
        this.selectedItem = item
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