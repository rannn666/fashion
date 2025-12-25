<template>
  <div class="home">
    <header class="header">
      <h1 class="site-title">rann的小试间</h1>
    </header>
    
    <!-- 中心导航按钮 -->
    <div class="center-nav">
      <nav class="main-nav-buttons">
        <ul>
          <li><a href="/" class="no-border-btn">首页</a></li>
          <li><a href="/blog" class="no-border-btn">博客</a></li>
          <li><a href="/blog/create" class="no-border-btn">发布</a></li>
        </ul>
      </nav>
    </div>
    
    <div class="content-wrapper">
      <aside class="left-sidebar">
        <nav class="main-nav">
          <ul>
            <li><a href="#"><StarIcon />分类</a></li>
            <li><a href="#"><StarIcon />关于</a></li>
            <li><a href="#"><StarIcon />联系</a></li>
            <li><a href="/blog"><StarIcon />最新文章</a></li>
          </ul>
        </nav>
        
        <div class="search-section">
          <h3>搜索</h3>
          <form class="search-form">
            <input type="text" placeholder="搜索文章..." class="search-input">
            <button type="submit" class="search-button">搜索</button>
          </form>
        </div>
        
        <div class="categories-section">
          <h3>文章分类</h3>
          <ul class="categories-list">
            <li><a href="#">时尚趋势</a> <span class="category-count">12</span></li>
            <li><a href="#">搭配技巧</a> <span class="category-count">8</span></li>
            <li><a href="#">配饰指南</a> <span class="category-count">5</span></li>
            <li><a href="#">品牌故事</a> <span class="category-count">6</span></li>
            <li><a href="#">时尚事件</a> <span class="category-count">4</span></li>
          </ul>
        </div>
        
        <div class="tags-section">
          <h3>热门标签</h3>
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
        
      <section class="main-section-titles">
        <h3>内容分类</h3>
        <ul class="section-titles-list">
          <li><a href="#">时尚达人推荐</a></li>
          <li><a href="#">本周热门单品</a></li>
          <li><a href="#">今日搭配灵感</a></li>
        </ul>
      </section>
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
import StarIcon from '@/components/StarIcon.vue'

export default {
  name: 'HomePage',
  components: {
    StarIcon
  },
  data() {
    return {
      searchQuery: '',
      posts: [
        {
          id: 2,
          title: '如何搭配春季外套',
          category: '搭配技巧',
          date: '2027-10-10',
          excerpt: '学习如何将春季外套与不同风格的服装搭配，打造时尚又舒适的造型。'
        },
        {
          id: 3,
          title: '2027年流行色解析',
          category: '时尚趋势',
          date: '2027-10-05',
          excerpt: '深入了解2027年的流行色及其在时尚界的应用。'
        },
        {
          id: 4,
          title: '必备配饰推荐',
          category: '配饰指南',
          date: '2027-09-28',
          excerpt: '春季必备的配饰清单，让你的整体造型更加完美。'
        }
      ],
      popularPosts: [
        {
          id: 5,
          title: '时尚博主的日常穿搭灵感',
          category: '时尚趋势',
          date: '2027-09-20',
          views: 1256
        },
        {
          id: 6,
          title: '如何选择适合自己的牛仔裤',
          category: '搭配技巧',
          date: '2027-09-15',
          views: 987
        },
        {
          id: 7,
          title: '春季鞋履指南',
          category: '配饰指南',
          date: '2027-09-10',
          views: 854
        }
      ],
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
      ],
      influencers: [
        {
          name: '艾米丽·时尚',
          followers: '156K',
          specialty: '都市时尚达人'
        },
        {
          name: '路易斯·风格',
          followers: '89K',
          specialty: '街头时尚专家'
        },
        {
          name: '玛莎·造型',
          followers: '234K',
          specialty: '高级定制顾问'
        }
      ],
      trendingItems: [
        {
          name: '丝质衬衫',
          brand: 'Zara',
          price: '¥299',
          tag: '热销'
        },
        {
          name: '高腰牛仔裤',
          brand: 'H&M',
          price: '¥199',
          tag: '新上架'
        },
        {
          name: '小白鞋',
          brand: 'Nike',
          price: '¥699',
          tag: '经典'
        },
        {
          name: '针织开衫',
          brand: 'COS',
          price: '¥450',
          tag: '热门'
        }
      ],
      outfits: [
        {
          style: '办公',
          title: '优雅职场装',
          description: '专业而不失时尚感的职场搭配，让你在办公室中脱颖而出。',
          tags: ['正式', '优雅', '简约']
        },
        {
          style: '休闲',
          title: '周末轻松穿搭',
          description: '舒适acee的周末造型，既轻松又时尚。',
          tags: ['舒适', '休闲', '百搭']
        },
        {
          style: '约会',
          title: '浪漫约会装',
          description: '温柔优雅的约会搭配，展现你的女性魅力。',
          tags: ['浪漫', '优雅', '温柔']
        }
      ]
    }
  },
  methods: {
    handleSearch() {
      // 这里可以实现搜索功能，例如跳转到博客列表页并携带搜索参数
      if (this.searchQuery) {
        this.$router.push({ path: '/blog', query: { search: this.searchQuery } });
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
  gap: 5px;
}

.search-input {
  flex: 1;
  padding: 8px 12px;
  /* 去掉黑色透明边框 */
  border: none;
  border-radius: 4px;
  font-size: 0.9rem;
  background: transparent;
  color: #fff;
  transition: all 0.3s;
}

.search-input:focus {
  outline: none;
  /* 去掉白色透明边框 */
  border: none;
  box-shadow: none;
}

.search-button {
  padding: 8px 15px;
  background: linear-gradient(90deg, #c67bb4, #8b76b8);
  color: white;
  /* 去掉黑色透明边框 */
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;
}

.search-button:hover {
  background: linear-gradient(90deg, #8b76b8, #c67bb4);
  box-shadow: 0 2px 10px rgba(200, 140, 220, 0.3);
  transform: translateY(-2px);
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-decoration: none;
  color: #4a3c5c;
  padding: 5px 10px;
  border-radius: 4px;
  transition: all 0.3s;
  background: transparent;
  /* 去掉黑色透明边框 */
  border: none;
  position: relative;
  overflow: hidden;
}

.categories-list a::before {
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

.categories-list a:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

@keyframes shimmer {
  0% { transform: translateX(-100%) rotate(30deg); }
  100% { transform: translateX(100%) rotate(30deg); }
}

.category-count {
  background: #333;
  padding: 2px 6px;
  border-radius: 10px;
  font-size: 0.8rem;
  color: #ccc;
}

.tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  display: inline-block;
  padding: 5px 12px;
  background: transparent;
  /* 去掉黑色透明边框 */
  border: none;
  color: #f0f0f0;
  text-decoration: none;
  border-radius: 15px;
  font-size: 0.9rem;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.tag::before {
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

.tag:hover {
  background: linear-gradient(90deg, #ff94d2, #b388eb);
  color: white;
}

.main-content {
  flex: 1;
  min-width: 0; /* 防止内容溢出 */
}

.sidebar {
  flex: 0 0 350px; /* 增加宽度 */
  background: transparent;
  padding: 25px;
  border-radius: 8px;
  min-height: fit-content;
  min-width: 0; /* 防止内容溢出 */
  /* 去掉黑色透明边框 */
  border: none;
}

.featured-post {
  margin-bottom: 60px;
}

.post-card {
  background: transparent;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s;
  /* 确保没有边框 */
  border: none;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
}

.post-card.featured {
  display: flex;
  flex-direction: row;
  height: 400px;
  width: 100%;
  box-sizing: border-box;
}

.post-card.featured .post-image {
  width: 50%;
  height: 100%;
  object-fit: cover;
  box-sizing: border-box;
}

.post-card.featured .post-content {
  width: 50%;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-sizing: border-box;
}

.post-image {
  width: 100%;
  height: 250px;
  object-fit: cover;
  box-sizing: border-box;
}

.post-content {
  padding: 20px;
  box-sizing: border-box;
}

.post-meta {
  display: flex;
  gap: 15px;
  margin-bottom: 10px;
  font-size: 0.9rem;
  color: #ccc;
  position: relative;
}

.post-category {
  background: linear-gradient(90deg, #c67bb4, #8b76b8);
  padding: 3px 8px;
  border-radius: 4px;
  font-weight: 500;
  color: #fff;
  /* 去掉黑色透明边框 */
  border: none;
}

.post-title {
  font-size: 1.8rem;
  margin: 10px 0;
  color: #fff;
}

.post-card.featured .post-title {
  font-size: 2.2rem;
}

.post-excerpt {
  color: #e0e0e0;
  margin-bottom: 20px;
  line-height: 1.6;
}

.read-more {
  display: inline-block;
  padding: 10px 20px;
  background: linear-gradient(90deg, #ff94d2, #b388eb);
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background 0.3s;
  align-self: flex-start;
}

.read-more:hover {
  background: linear-gradient(90deg, #b388eb, #ff94d2);
}

.section-title {
  font-size: 1.8rem;
  margin-bottom: 25px;
  color: #fff;
  text-align: center;
  /* 去掉白色透明边框 */
  border-bottom: none;
  padding-bottom: 10px;
  position: relative;
  /* 小星星样式 */
  .small-star {
    width: 12px !important;
    height: 12px !important;
    margin-left: 5px;
  }
  
  /* 文字玻璃反光效果 */
  h1, h2, h3, h4, h5, h6, .post-title, .news-title {
    position: relative;
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, 0.3);
  }
  .glass-text {
    background: linear-gradient(90deg, rgba(255,255,255,0.8), rgba(255,255,255,0.5), rgba(255,255,255,0.8));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    position: relative;
    z-index: 1;
  }
}

.sidebar .section-title {
  font-size: 1.5rem;
  text-align: left;
  color: #fff;
}

.popular-posts {
  margin-top: 40px;
}

.post-views {
  font-size: 0.8rem;
  color: #999;
}

.instagram-section {
  margin-top: 40px;
}

.instagram-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-bottom: 15px;
}

.instagram-item {
  display: block;
  overflow: hidden;
  border-radius: 4px;
  transition: transform 0.3s;
}

.instagram-item:hover {
  transform: scale(1.05);
}

.instagram-item img {
  width: 100%;
  height: 100px;
  object-fit: cover;
}

.instagram-link {
  display: block;
  text-align: center;
  color: #ff69b4;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.instagram-link:hover {
  color: #ff1493;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
}

.posts-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.sidebar-post {
  padding: 15px;
  /* 去掉黑色透明边框 */
  border-bottom: none;
  background: transparent;
  border-radius: 8px;
  /* 去掉黑色透明边框 */
  border: none;
  position: relative;
  overflow: hidden;
}

.sidebar-post::before {
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
  animation: shimmer 3s infinite;
}

.sidebar-post:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.sidebar-post-content {
  padding: 0;
}

.footer {
  text-align: center;
  padding: 40px 0;
  /* 去掉白色透明边框 */
  border-top: none;
}

footer {
  color: rgba(255, 255, 255, 0.8);
  margin-top: auto; /* 确保页脚始终在页面底部 */
  background: transparent;
}

.social-links {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 20px;
}

/* 新增内容区域样式 */
.fashion-news {
  margin: 50px 0;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.news-item {
  background: transparent;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s;
  /* 确保没有边框 */
  border: none;
}

.news-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
}

.news-image {
  width: 100%;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: bold;
}

.placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: bold;
}

.news-content {
  padding: 20px;
}

.news-meta {
  display: flex;
  gap: 15px;
  margin-bottom: 10px;
  font-size: 0.9rem;
  color: #ccc;
}

.news-category {
  background: linear-gradient(90deg, #ff94d2, #b388eb);
  padding: 3px 8px;
  border-radius: 4px;
  font-weight: 500;
  color: #fff;
}

.news-title {
  color: #ffffff;
  margin: 10px 0;
  font-size: 1.3rem;
  line-height: 1.4;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, 0.3);
}

.news-excerpt {
  color: #e0e0e0;
  font-size: 0.9rem;
  line-height: 1.6;
}







.social-links a {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  transition: color 0.3s;
}

.social-links a:hover {
  color: #fff;
  text-decoration: underline;
}

.section-placeholder {
  padding: 20px;
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
  background: transparent;
  border-radius: 8px;
  /* 确保没有边框 */
  border: none;
}

.main-section-titles {
  margin-top: 30px;
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
  background: transparent;
  border-radius: 8px;
  /* 确保没有边框 */
  border: none;
}

.section-titles-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.section-titles-list li {
  margin-bottom: 15px;
}

.section-titles-list a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: all 0.3s;
  display: block;
  padding: 8px 12px;
  border-radius: 4px;
  background: transparent;
  /* 确保没有边框 */
  border: none;
  position: relative;
  overflow: hidden;
}

.section-titles-list a::before {
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

.section-titles-list a:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.3);
}
.section-titles-list a:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.3);
}

/* 小星星样式 */
.small-star {
  width: 12px !important;
  height: 12px !important;
  margin-left: 5px;
}

/* 文字玻璃反光效果 */
h1, h2, h3, h4, h5, h6, .post-title, .news-title {
  position: relative;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, 0.3);
}

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
  background: rgba(74, 60, 92, 0.3);
  /* 彻底清除所有可能的边框样式 */
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
  /* 添加额外的边框清除属性 */
  border-width: 0 !important;
  border-style: none !important;
  border-color: transparent !important;
}

/* 悬停状态 */
.home .center-nav .main-nav-buttons a:hover {
  background: rgba(74, 60, 92, 0.5);
  color: #ff69b4;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(255, 105, 180, 0.3) !important;
  /* 悬停时也确保无边框 */
  border: none !important;
  outline: none !important;
  /* 添加额外的边框清除属性 */
  border-width: 0 !important;
  border-style: none !important;
  border-color: transparent !important;
}

.site-title {
  font-size: 1.8rem;
  margin: 10px 0;
  color: #fff;
}
</style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  font-family: 'Microsoft YaHei', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: 
    radial-gradient(circle at 25% 25%, rgba(168, 230, 207, 0.8) 0%, rgba(168, 230, 207, 0.3) 35%, transparent 60%),
    radial-gradient(circle at 75% 75%, rgba(255, 211, 182, 0.8) 0%, rgba(255, 211, 182, 0.3) 35%, transparent 60%),
    linear-gradient(135deg, 
      #a8e6cf 0%, 
      #a8e6cf 30%, 
      #b8e6d3 35%, 
      #c8d4d8 40%, 
      #d8d4d3 45%, 
      #e8d4ce 47%, 
      #f0d4c9 49%, 
      #ffd3b6 51%, 
      #ffd3b6 70%, 
      #ffd3b6 100%
    );
  background-blend-mode: multiply, screen, normal;
  background-attachment: fixed;
}