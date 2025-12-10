<template>
  <div class="post-detail">
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
      <article class="post">
        <div class="post-header">
          <div class="post-meta">
            <span class="post-category">{{ post.category }}</span>
            <span class="post-date">{{ post.date }}</span>
            <span class="post-author">作者: {{ post.author }}</span>
          </div>
          <h1 class="post-title">{{ post.title }}</h1>
        </div>
        
        <img :src="post.image" :alt="post.title" class="post-image">
        
        <div class="post-content">
          <div v-html="post.content"></div>
        </div>
        
        <div class="post-tags">
          <span class="tag" v-for="tag in post.tags" :key="tag">{{ tag }}</span>
        </div>
        
        <div class="social-share">
          <h3>分享这篇文章</h3>
          <div class="social-links">
            <a href="#" class="share-link">Facebook</a>
            <a href="#" class="share-link">Twitter</a>
            <a href="#" class="share-link">Instagram</a>
            <a href="#" class="share-link">Pinterest</a>
          </div>
        </div>
      </article>
      
      <section class="related-posts">
        <h2>相关文章</h2>
        <div class="posts-grid">
          <div class="post-card" v-for="relatedPost in relatedPosts" :key="relatedPost.id">
            <img :src="relatedPost.image" :alt="relatedPost.title" class="post-image">
            <div class="post-content">
              <div class="post-meta">
                <span class="post-category">{{ relatedPost.category }}</span>
                <span class="post-date">{{ relatedPost.date }}</span>
              </div>
              <h3 class="post-title">{{ relatedPost.title }}</h3>
              <a :href="`/post/${relatedPost.id}`" class="read-more">阅读更多</a>
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
  name: 'PostDetailPage',
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      post: {},
      relatedPosts: []
    }
  },
  mounted() {
    // In a real app, you would fetch this data from an API
    this.fetchPostData()
    this.fetchRelatedPosts()
  },
  methods: {
    fetchPostData() {
      // Simulate API call
      const posts = {
        '1': {
          id: '1',
          title: '2023年秋季时尚趋势预测',
          category: '时尚趋势',
          date: '2023-10-15',
          author: '时尚编辑',
          image: 'https://via.placeholder.com/800x500?text=Post+1',
          content: '<p>随着秋季的到来，时尚界迎来了新一轮的潮流变化。今年秋季的时尚趋势融合了经典与现代元素，创造出独特而多样化的风格。</p><p>首先，大地色调成为主流，棕色、卡其色和橄榄绿等自然色彩占据了T台的主导地位。这些色调不仅符合秋季的氛围，还能轻松搭配各种服装。</p><h3>关键趋势</h3><p>1. 宽松剪裁：舒适的宽松剪裁成为今年的流行趋势，无论是外套、毛衣还是裤装，都强调舒适与时尚的结合。</p><p>2. 复古元素：70年代的复古风格再次回归，喇叭裤、宽领衬衫和复古印花成为时尚爱好者的首选。</p><p>3. 层次感穿搭：通过叠穿不同材质和厚度的衣物，创造出丰富的层次感，既保暖又时尚。</p><p>4. 可持续时尚：环保和可持续发展成为时尚界的重要议题，许多品牌推出了环保材质制成的服装。</p><p>在配饰方面，宽檐帽、复古墨镜和大容量手提包成为今年秋季的必备单品。这些配饰不仅能提升整体造型，还能展现个人风格。</p><p>总的来说，2023年秋季的时尚趋势注重舒适性、多样性和可持续性，让每个人都能找到适合自己的风格。</p>',
          tags: ['秋季时尚', '潮流趋势', '穿搭技巧']
        },
        '2': {
          id: '2',
          title: '如何搭配秋季外套',
          category: '搭配技巧',
          date: '2023-10-10',
          author: '时尚达人',
          image: 'https://via.placeholder.com/800x500?text=Post+2',
          content: '<p>秋季外套是衣橱中的必备单品，如何搭配才能既时尚又实用呢？本文将为你介绍几种秋季外套的搭配技巧。</p><h3>1. 牛仔外套</h3><p>牛仔外套是秋季最百搭的单品之一，可以搭配几乎所有的服装。你可以将牛仔外套与连衣裙、T恤、衬衫等搭配，创造出休闲又时尚的风格。</p><h3>2. 风衣</h3><p>风衣是秋季的经典单品，适合正式和休闲场合。搭配长裤和衬衫可以打造商务风格，搭配牛仔裤和T恤则更加休闲。</p><h3>3. 羊毛大衣</h3><p>羊毛大衣是秋季保暖的最佳选择，同时也是时尚的象征。深色羊毛大衣可以搭配浅色内搭，创造出优雅的层次感。</p><h3>4. 皮夹克</h3><p>皮夹克适合喜欢酷感风格的人，可以搭配牛仔裤、黑色裤子或皮质裙装，展现个性魅力。</p><p>通过这些搭配技巧，你可以在秋季展现出独特的时尚风格，同时保持舒适和温暖。</p>',
          tags: ['外套搭配', '秋季穿搭', '时尚技巧']
        }
      }
      
      this.post = posts[this.id] || posts['1']
    },
    fetchRelatedPosts() {
      // Simulate API call for related posts
      this.relatedPosts = [
        {
          id: '3',
          title: '2023年流行色解析',
          category: '时尚趋势',
          date: '2023-10-05',
          image: 'https://via.placeholder.com/400x250?text=Post+3'
        },
        {
          id: '4',
          title: '必备配饰推荐',
          category: '配饰指南',
          date: '2023-09-28',
          image: 'https://via.placeholder.com/400x250?text=Post+4'
        }
      ]
    }
  }
}
</script>

<style scoped>
.post-detail {
  max-width: 1000px;
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

.post {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 50px;
}

.post-header {
  padding: 30px;
}

.post-meta {
  display: flex;
  flex-wrap: wrap;
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
  font-size: 2.5rem;
  margin: 10px 0;
  color: #333;
  line-height: 1.3;
}

.post-image {
  width: 100%;
  height: 500px;
  object-fit: cover;
}

.post-content {
  padding: 30px;
  color: #333;
  line-height: 1.8;
}

.post-content h3 {
  margin: 30px 0 15px;
  font-size: 1.5rem;
  color: #333;
}

.post-tags {
  padding: 0 30px 30px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tag {
  background: #f0f0f0;
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.9rem;
  color: #666;
}

.social-share {
  padding: 30px;
  border-top: 1px solid #e0e0e0;
  border-bottom: 1px solid #e0e0e0;
}

.social-share h3 {
  margin: 0 0 15px;
  color: #333;
}

.social-links {
  display: flex;
  gap: 15px;
}

.share-link {
  padding: 8px 15px;
  background: #f0f0f0;
  color: #333;
  text-decoration: none;
  border-radius: 4px;
  transition: background 0.3s;
}

.share-link:hover {
  background: #e0e0e0;
}

.related-posts {
  margin-top: 50px;
}

.related-posts h2 {
  font-size: 2rem;
  margin-bottom: 30px;
  color: #333;
  text-align: center;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
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

.post-card .post-image {
  height: 200px;
}

.post-card .post-content {
  padding: 20px;
}

.post-card .post-title {
  font-size: 1.3rem;
  margin: 10px 0;
}

.footer {
  text-align: center;
  padding: 40px 0;
  border-top: 1px solid #e0e0e0;
  color: #666;
}

.footer .social-links {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.footer .social-links a {
  color: #666;
  text-decoration: none;
  transition: color 0.3s;
}

.footer .social-links a:hover {
  color: #333;
}
</style>