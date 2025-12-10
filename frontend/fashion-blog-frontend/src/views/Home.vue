<template>
  <div class="home">
    <header class="header">
      <h1 class="site-title">时尚博客</h1>
      <nav class="nav">
        <ul>
          <li><a href="/">首页</a></li>
          <li><a href="#">分类</a></li>
          <li><a href="#">关于</a></li>
          <li><a href="#">联系</a></li>
        </ul>
      </nav>
    </header>
    
    <main class="main-content">
      <section class="featured-post">
        <div class="post-card featured">
          <img src="https://via.placeholder.com/800x400" alt="Featured Post" class="post-image">
          <div class="post-content">
            <div class="post-meta">
              <span class="post-category">时尚趋势</span>
              <span class="post-date">2023-10-15</span>
            </div>
            <h2 class="post-title">2023年秋季时尚趋势预测</h2>
            <p class="post-excerpt">探索今年秋季最热门的时尚趋势，从服装到配饰，让你的衣橱焕然一新。</p>
            <a href="/post/1" class="read-more">阅读更多</a>
          </div>
        </div>
      </section>
      
      <section class="recent-posts">
        <h2 class="section-title">最新文章</h2>
        <div class="posts-grid">
          <div class="post-card" v-for="post in posts" :key="post.id">
            <img :src="`https://via.placeholder.com/400x250?text=Post+${post.id}`" :alt="post.title" class="post-image">
            <div class="post-content">
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
    </main>
    
    <footer class="footer">
      <p>&copy; 2023 时尚博客. 保留所有权利.</p>
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
      posts: [
        {
          id: 2,
          title: '如何搭配秋季外套',
          category: '搭配技巧',
          date: '2023-10-10',
          excerpt: '学习如何将秋季外套与不同风格的服装搭配，打造时尚又舒适的造型。'
        },
        {
          id: 3,
          title: '2023年流行色解析',
          category: '时尚趋势',
          date: '2023-10-05',
          excerpt: '深入了解2023年的流行色及其在时尚界的应用。'
        },
        {
          id: 4,
          title: '必备配饰推荐',
          category: '配饰指南',
          date: '2023-09-28',
          excerpt: '秋季必备的配饰清单，让你的整体造型更加完美。'
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
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  border-bottom: 1px solid #e0e0e0;
}

.site-title {
  font-size: 2.5rem;
  color: #333;
  margin: 0;
}

.nav ul {
  display: flex;
  list-style: none;
  gap: 20px;
  margin: 0;
  padding: 0;
}

.nav a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: color 0.3s;
}

.nav a:hover {
  color: #666;
}

.main-content {
  padding: 40px 0;
}

.featured-post {
  margin-bottom: 60px;
}

.post-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
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
  color: #666;
}

.post-category {
  background: #f0f0f0;
  padding: 3px 8px;
  border-radius: 4px;
  font-weight: 500;
}

.post-title {
  font-size: 1.8rem;
  margin: 10px 0;
  color: #333;
}

.post-card.featured .post-title {
  font-size: 2.2rem;
}

.post-excerpt {
  color: #666;
  margin-bottom: 20px;
  line-height: 1.6;
}

.read-more {
  display: inline-block;
  padding: 10px 20px;
  background: #333;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background 0.3s;
  align-self: flex-start;
}

.read-more:hover {
  background: #555;
}

.section-title {
  font-size: 2rem;
  margin-bottom: 30px;
  color: #333;
  text-align: center;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
}

.footer {
  text-align: center;
  padding: 40px 0;
  border-top: 1px solid #e0e0e0;
  color: #666;
}

.social-links {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.social-links a {
  color: #666;
  text-decoration: none;
  transition: color 0.3s;
}

.social-links a:hover {
  color: #333;
}
</style>