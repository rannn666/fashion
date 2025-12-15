<template>
  <div class="post-detail">
    <header class="header">
      <h1 class="site-title">服装品牌</h1>
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
      </aside>
      
      <main class="main-content">
      <article class="post">
        <div class="post-header">
          <div class="post-meta">
            <span class="post-category">{{ post.category }}</span>
            <span class="post-date">{{ post.date }}</span>
            <span class="post-author">作者: {{ post.author }}</span>
            <span class="post-views">{{ post.views }} 阅读</span>
            <span class="post-comments">{{ post.comments }} 评论</span>
          </div>
          <h1 class="post-title">{{ post.title }}</h1>
          
          <div class="author-info">
            <div class="author-avatar">
              <div v-if="!post.authorAvatar" class="avatar-placeholder" style="background-color: #f0f0f0; width: 100px; height: 100px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #999;">{{ post.author ? post.author.charAt(0) : 'U' }}</div>
              <img v-else :src="post.authorAvatar" :alt="post.author" class="avatar-img">
            </div>
            <div class="author-details">
              <h3>{{ post.author }}</h3>
              <p class="author-bio">{{ post.authorBio }}</p>
              <div class="author-social">
                <a href="#" class="social-link">Instagram</a>
                <a href="#" class="social-link">Twitter</a>
                <a href="#" class="social-link">Pinterest</a>
              </div>
            </div>
          </div>
        </div>
        
        <div v-if="!post.image" class="post-image" style="background-color: #f0f0f0; width: 100%; height: 400px; display: flex; align-items: center; justify-content: center; color: #999; font-size: 18px;">{{ post.title }}</div>
        <img v-else :src="post.image" :alt="post.title" class="post-image">
        
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
            <a href="#" class="share-link">微信</a>
            <a href="#" class="share-link">微博</a>
          </div>
        </div>
        
        <div class="comments-section">
          <h3>{{ post.comments }} 条评论</h3>
          <div class="comments-list">
            <div class="comment" v-for="comment in comments" :key="comment.id">
              <div class="comment-avatar">
                <div v-if="!comment.avatar" class="avatar-placeholder" style="background-color: #f0f0f0; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #999;">{{ comment.author.charAt(0) }}</div>
                <img v-else :src="comment.avatar" :alt="comment.author" class="avatar-img">
              </div>
              <div class="comment-content">
                <div class="comment-header">
                  <span class="comment-author">{{ comment.author }}</span>
                  <span class="comment-date">{{ comment.date }}</span>
                </div>
                <p class="comment-text">{{ comment.content }}</p>
                <button class="reply-button">回复</button>
              </div>
            </div>
          </div>
          
          <div class="comment-form-section">
            <h3>添加评论</h3>
            <form class="comment-form">
              <div class="form-group">
                <label for="name">姓名</label>
                <input type="text" id="name" placeholder="请输入您的姓名" required>
              </div>
              <div class="form-group">
                <label for="email">邮箱</label>
                <input type="email" id="email" placeholder="请输入您的邮箱" required>
              </div>
              <div class="form-group">
                <label for="comment">评论</label>
                <textarea id="comment" rows="5" placeholder="请输入您的评论" required></textarea>
              </div>
              <button type="submit" class="submit-button">发表评论</button>
            </form>
          </div>
        </div>
      </article>
      
      <section class="related-posts">
        <h2>相关文章</h2>
        <div class="posts-grid">
          <div class="post-card" v-for="relatedPost in relatedPosts" :key="relatedPost.id">
            <div v-if="!relatedPost.image" class="post-image" style="background-color: #f0f0f0; width: 100%; height: 200px; display: flex; align-items: center; justify-content: center; color: #999; font-size: 14px;">{{ relatedPost.title }}</div>
            <img v-else :src="relatedPost.image" :alt="relatedPost.title" class="post-image">
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
  name: 'PostDetailPage',
  components: {
    StarIcon
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      post: {},
      relatedPosts: [],
      comments: [
        {
          id: 1,
          author: '时尚爱好者',
          avatar: '',
          date: '2027-10-16',
          content: '这篇文章写得非常好，对我很有帮助！'
        },
        {
          id: 2,
          author: '时尚博主',
          avatar: '',
          date: '2027-10-17',
          content: '我也很喜欢今年春季的这些趋势，尤其是明亮的色彩搭配！'
        },
        {
          id: 3,
          author: '时尚编辑',
          avatar: '',
          date: '2027-10-18',
          content: '分析得很到位，期待更多这样的文章！'
        }
      ]
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
          title: '2027年春季时尚趋势预测',
          category: '时尚趋势',
          date: '2027-10-15',
          author: '时尚编辑',
          authorAvatar: '',
          authorBio: '资深时尚编辑，专注时尚趋势研究10年，曾在多家时尚杂志担任主编。',
          views: 2567,
          comments: 32,
          image: '',
          content: '<p>随着春季的到来，时尚界迎来了新一轮的潮流变化。2027年春季的时尚趋势融合了经典与现代元素，创造出独特而多样化的风格。</p><p>首先，明亮的色彩成为主流，粉色、黄色和浅蓝色等鲜艳色彩占据了T台的主导地位。这些色调不仅符合春季的氛围，还能轻松搭配各种服装。</p><h3>关键趋势</h3><p>1. 宽松剪裁：舒适的宽松剪裁成为今年的流行趋势，无论是外套、毛衣还是裤装，都强调舒适与时尚的结合。</p><p>2. 复古元素：70年代的复古风格再次回归，喇叭裤、宽领衬衫和复古印花成为时尚爱好者的首选。</p><p>3. 层次感穿搭：通过叠穿不同材质和厚度的衣物，创造出丰富的层次感，既保暖又时尚。</p><p>4. 可持续时尚：环保和可持续发展成为时尚界的重要议题，许多品牌推出了环保材质制成的服装。</p><p>在配饰方面，宽檐帽、复古墨镜和大容量手提包成为2027年春季的必备单品。这些配饰不仅能提升整体造型，还能展现个人风格。</p><p>总的来说，2027年春季的时尚趋势注重舒适性、多样性和可持续性，让每个人都能找到适合自己的风格。</p>',
          tags: ['春季时尚', '潮流趋势', '穿搭技巧']
        },
        '2': {
          id: '2',
          title: '如何搭配春季外套',
          category: '搭配技巧',
          date: '2027-10-10',
          author: '时尚达人',
          authorAvatar: '',
          authorBio: '时尚博主，热爱分享穿搭技巧和时尚心得，拥有百万粉丝。',
          views: 1890,
          comments: 25,
          image: '',
          content: '<p>春季外套是衣橱中的必备单品，如何搭配才能既时尚又实用呢？本文将为你介绍几种春季外套的搭配技巧。</p><h3>1. 牛仔外套</h3><p>牛仔外套是春季最百搭的单品之一，可以搭配几乎所有的服装。你可以将牛仔外套与连衣裙、T恤、衬衫等搭配，创造出休闲又时尚的风格。</p><h3>2. 风衣</h3><p>风衣是春季的经典单品，适合正式和休闲场合。搭配长裤和衬衫可以打造商务风格，搭配牛仔裤和T恤则更加休闲。</p><h3>3. 针织开衫</h3><p>针织开衫是春季保暖的最佳选择，同时也是时尚的象征。浅色针织开衫可以搭配各种内搭，创造出优雅的层次感。</p><h3>4. 皮夹克</h3><p>皮夹克适合喜欢酷感风格的人，可以搭配牛仔裤、黑色裤子或皮质裙装，展现个性魅力。</p><p>通过这些搭配技巧，你可以在春季展现出独特的时尚风格，同时保持舒适和温暖。</p>',
          tags: ['外套搭配', '春季穿搭', '时尚技巧']
        }
      }
      
      this.post = posts[this.id] || posts['1']
    },
    fetchRelatedPosts() {
      // Simulate API call for related posts
      this.relatedPosts = [
        {
          id: '3',
          title: '2027年流行色解析',
          category: '时尚趋势',
          date: '2027-10-05',
          image: ''
        },
        {
          id: '4',
          title: '必备配饰推荐',
          category: '配饰指南',
          date: '2027-09-28',
          image: ''
        }
      ]
    }
  }
}
</script>

<style scoped>
.post-detail {
  width: 100%;
  margin: 0;
  padding: 0 40px;
  background: transparent;
  color: #fff;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  border-bottom: 1px solid rgba(74, 60, 92, 0.3);
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(10px);
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  margin-bottom: 40px;
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
  gap: 50px;
  padding: 40px 0;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.left-sidebar {
  flex: 0 0 190px; /* 包含padding的总宽度 */
  background: transparent;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid rgba(74, 60, 92, 0.3);
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
  color: #4a3c5c;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 10px 15px;
  border-radius: 4px;
  transition: all 0.3s;
  background: transparent;
  border: 1px solid rgba(74, 60, 92, 0.2);
}

.main-nav a:hover {
  background: rgba(255, 105, 180, 0.3); /* 鼠标悬停时背景为透明粉色 */
  color: #fff;
}

.main-content {
  flex: 1;
  min-width: 0; /* 防止内容溢出 */
}

.post {
  background: transparent;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 50px;
  border: 1px solid rgba(74, 60, 92, 0.3);
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
  color: #ccc;
}

.post-views, .post-comments {
  color: #999;
  font-size: 0.85rem;
}

.post-category {
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  padding: 3px 8px;
  border-radius: 4px;
  font-weight: 500;
  color: #fff;
}

.post-title {
  font-size: 2.5rem;
  margin: 10px 0;
  color: #fff;
  line-height: 1.3;
}

.post-image {
  width: 100%;
  height: 500px;
  object-fit: cover;
}

.post-content {
  padding: 30px;
  color: #fff;
  line-height: 1.8;
}

.post-content h3 {
  margin: 30px 0 15px;
  font-size: 1.5rem;
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.post-tags {
  padding: 0 30px 30px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tag {
  background: rgba(255, 255, 255, 0.2);
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.9rem;
  color: #fff;
}

.author-info {
  display: flex;
  gap: 20px;
  margin-top: 30px;
  padding: 20px;
  background: transparent;
  border-radius: 8px;
  border: 1px solid rgba(74, 60, 92, 0.3);
}

.author-avatar {
  flex: 0 0 80px;
}

.avatar-img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
}

.author-details {
  flex: 1;
}

.author-details h3 {
  margin: 0 0 10px;
  color: #ff69b4;
}

.author-bio {
  margin: 0 0 15px;
  color: #ccc;
  font-size: 0.95rem;
  line-height: 1.5;
}

.author-social {
  display: flex;
  gap: 10px;
}

.author-social .social-link {
  color: #ff69b4;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s;
}

.author-social .social-link:hover {
  color: #ff1493;
}

.social-share {
  padding: 30px;
  border-top: 1px solid #333;
  border-bottom: 1px solid #333;
}

.social-share h3 {
  margin: 0 0 15px;
  color: #fff;
}

.social-links {
  display: flex;
  gap: 15px;
}

.share-link {
  padding: 8px 15px;
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  transition: all 0.3s;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.share-link:hover {
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  color: #fff;
  border-color: transparent;
}

.comments-section {
  margin-top: 50px;
  padding: 30px;
  background: transparent;
  border-radius: 8px;
  border: 1px solid rgba(74, 60, 92, 0.3);
}

.comments-section h3 {
  margin: 0 0 30px;
  color: #fff;
  font-size: 1.8rem;
}

.comments-list {
  margin-bottom: 40px;
}

.comment {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
}

.comment:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.comment-avatar {
  flex: 0 0 50px;
}

.comment-content {
  flex: 1;
}

.comment-header {
  display: flex;
  gap: 15px;
  margin-bottom: 10px;
}

.comment-author {
  font-weight: 600;
  color: #ff94d2;
}

.comment-date {
  color: #999;
  font-size: 0.9rem;
}

.comment-text {
  color: #ccc;
  line-height: 1.6;
  margin-bottom: 15px;
}

.reply-button {
  padding: 5px 12px;
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s;
}

.reply-button:hover {
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  color: #fff;
  border-color: transparent;
}

.comment-form-section h3 {
  margin: 0 0 20px;
  font-size: 1.5rem;
  color: #fff;
}

.comment-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.form-group label {
  font-weight: 500;
  color: #fff;
}

.form-group input,
.form-group textarea {
  padding: 12px;
  border: 1px solid #333;
  border-radius: 4px;
  font-size: 1rem;
  font-family: inherit;
  background: #333;
  color: #fff;
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

.submit-button {
  align-self: flex-start;
  padding: 12px 25px;
  background: #ff69b4;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: background 0.3s;
}

.submit-button:hover {
  background: #ff1493;
}

.related-posts {
  margin-top: 50px;
}

.related-posts h2 {
  font-size: 2rem;
  margin-bottom: 30px;
  color: #fff;
  text-align: center;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
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

.post-card .post-image {
  height: 200px;
}

.post-card .post-content {
  padding: 20px;
}

.post-card .post-title {
  font-size: 1.3rem;
  margin: 10px 0;
  color: #fff;
}

.footer {
  text-align: center;
  padding: 40px 0;
  border-top: 1px solid #333;
  color: #ccc;
  margin-top: auto;
}

.footer .social-links {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.footer .social-links a {
  color: #ff69b4;
  text-decoration: none;
  transition: color 0.3s;
}

.footer .social-links a:hover {
  color: #ff1493;
}
</style>