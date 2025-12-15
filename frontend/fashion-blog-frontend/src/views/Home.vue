<template>
  <div class="home">
    <header class="header">
      <h1 class="site-title">时尚博客</h1>
      <nav class="top-nav">
        <ul>
          <li><a href="/">首页</a></li>
        </ul>
      </nav>
    </header>
    
    <div class="content-wrapper">
      <aside class="left-sidebar">
        <nav class="main-nav">
          <ul>
            <li><a href="#"><StarIcon />分类</a></li>
            <li><a href="#"><StarIcon />关于</a></li>
            <li><a href="#"><StarIcon />联系</a></li>
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
      </aside>
      
      <main class="main-content">
        <section class="featured-post">
          <div class="post-card featured">
            <img src="https://via.placeholder.com/800x400" alt="Featured Post" class="post-image">
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
      </main>
      
      <aside class="sidebar">
        <section class="recent-posts">
          <h2 class="section-title">最新文章</h2>
          <div class="posts-list">
            <div class="post-card sidebar-post" v-for="post in posts" :key="post.id">
              <div class="sidebar-post-content">
                <div class="post-meta">
                  <span class="post-category">{{ post.category }}</span>
                  <span class="post-date">{{ post.date }}</span>
                </div>
                <h3 class="post-title">{{ post.title }}</h3>
                <p class="post-excerpt">{{ post.excerpt }}</p>
                <a :href="`/post/${post.id}`" class="read-more">阅读更多</a>
              </div>
            </div>
          </div>
        </section>
        
        <section class="popular-posts">
          <h2 class="section-title">热门文章</h2>
          <div class="posts-list">
            <div class="post-card sidebar-post" v-for="post in popularPosts" :key="post.id">
              <div class="sidebar-post-content">
                <div class="post-meta">
                  <span class="post-category">{{ post.category }}</span>
                  <span class="post-date">{{ post.date }}</span>
                  <span class="post-views">{{ post.views }} 阅读</span>
                </div>
                <h3 class="post-title">{{ post.title }}</h3>
                <a :href="`/post/${post.id}`" class="read-more">阅读更多</a>
              </div>
            </div>
          </div>
        </section>
        
        <section class="instagram-section">
          <h2 class="section-title">Instagram</h2>
          <div class="instagram-grid">
              <a href="#" class="instagram-item" v-for="i in 6" :key="i">
                <img :src="`https://via.placeholder.com/100x100?text=Instagram+${i}`" alt="Instagram post">
              </a>
            </div>
          <a href="#" class="instagram-link">@fashionblog</a>
        </section>
      </aside>
    </div>
    
    <footer class="footer">
      <p>&copy; 2027 时尚博客. 保留所有权利.</p>
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
      ]
    }
  }
}
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  background-color: #000;
  color: #fff;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  border-bottom: 1px solid #333;
}

.site-title {
  font-size: 2.5rem;
  color: #fff;
  margin: 0;
}

.top-nav ul {
  display: flex;
  list-style: none;
  gap: 20px;
  margin: 0;
  padding: 0;
}

.top-nav a {
  text-decoration: none;
  color: #fff;
  font-weight: 500;
  transition: color 0.3s;
}

.top-nav a:hover {
  color: #ff69b4;
}

.content-wrapper {
  display: flex;
  gap: 30px;
  padding: 40px 0;
}

.left-sidebar {
  flex: 0 0 180px;
  background: #1a1a1a;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(255, 105, 180, 0.1);
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
}

.main-nav a:hover {
  background: #ff69b4;
  color: #fff;
}

.search-section, .categories-section, .tags-section {
  margin-top: 30px;
}

.search-section h3, .categories-section h3, .tags-section h3 {
  font-size: 1.2rem;
  margin-bottom: 15px;
  color: #fff;
  border-bottom: 2px solid #333;
  padding-bottom: 8px;
}

.search-form {
  display: flex;
  gap: 5px;
}

.search-input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #333;
  border-radius: 4px;
  font-size: 0.9rem;
  background: #1a1a1a;
  color: #fff;
}

.search-button {
  padding: 8px 15px;
  background: #ff69b4;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s;
}

.search-button:hover {
  background: #ff1493;
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
  color: #ccc;
  padding: 5px 10px;
  border-radius: 4px;
  transition: all 0.3s;
}

.categories-list a:hover {
  background: #ff69b4;
  color: #fff;
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
  background: #333;
  color: #ccc;
  text-decoration: none;
  border-radius: 15px;
  font-size: 0.9rem;
  transition: all 0.3s;
}

.tag:hover {
  background: #ff69b4;
  color: white;
}

.main-content {
  flex: 3;
}

.sidebar {
  flex: 1;
  background: #1a1a1a;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(255, 105, 180, 0.1);
}

.featured-post {
  margin-bottom: 60px;
}

.post-card {
  background: #1a1a1a;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(255, 105, 180, 0.1);
  transition: transform 0.3s;
}

.post-card:hover {
  transform: translateY(-5px);
}

.post-card.featured {
  display: flex;
  flex-direction: row;
  height: 400px;
}

.post-card.featured .post-image {
  width: 50%;
  height: 100%;
  object-fit: cover;
}

.post-card.featured .post-content {
  width: 50%;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.post-image {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.post-content {
  padding: 20px;
}

.post-meta {
  display: flex;
  gap: 15px;
  margin-bottom: 10px;
  font-size: 0.9rem;
  color: #ccc;
}

.post-category {
  background: #ff69b4;
  padding: 3px 8px;
  border-radius: 4px;
  font-weight: 500;
  color: #fff;
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
  color: #ccc;
  margin-bottom: 20px;
  line-height: 1.6;
}

.read-more {
  display: inline-block;
  padding: 10px 20px;
  background: #ff69b4;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background 0.3s;
  align-self: flex-start;
}

.read-more:hover {
  background: #ff1493;
}

.section-title {
  font-size: 1.8rem;
  margin-bottom: 25px;
  color: #fff;
  text-align: center;
  border-bottom: 2px solid #333;
  padding-bottom: 10px;
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
  padding: 15px 0;
  border-bottom: 1px solid #333;
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
  border-top: 1px solid #333;
  color: #ccc;
}

.social-links {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.social-links a {
  color: #ff69b4;
  text-decoration: none;
  transition: color 0.3s;
}

.social-links a:hover {
  color: #ff1493;
}
</style>