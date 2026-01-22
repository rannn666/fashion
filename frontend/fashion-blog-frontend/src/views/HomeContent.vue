<template>
  <div class="home-content">
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
  </div>
</template>

<script>
export default {
  name: 'HomeContent'
}
</script>

<style scoped>
.home-content {
  padding: 2rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

/* 导航栏样式 */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  margin-bottom: 2rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.nav-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.nav-link {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-weight: 500;
  font-size: 0.95rem;
}

.nav-link:hover {
  background: rgba(255, 148, 210, 0.2);
  color: #ff94d2;
  transform: translateY(-2px);
}

/* 标题样式 */
.welcome-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  text-align: center;
  background: linear-gradient(45deg, #ff94d2, #a18aff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-family: 'Poppins', 'Inter', sans-serif;
}

.subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 3rem;
  font-weight: 400;
  font-family: 'Inter', 'Segoe UI', sans-serif;
}

/* 博客网格样式 */
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.blog-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  overflow: hidden;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  font-family: 'Inter', 'Segoe UI', sans-serif;
}

.blog-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 148, 210, 0.4);
}

.blog-image {
  width: 100%;
  height: 200px;
  background: linear-gradient(45deg, #ff94d2, #a18aff);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
}

.blog-content {
  padding: 1.5rem;
}

.blog-title {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #fff;
  font-family: 'Poppins', 'Inter', sans-serif;
}

.blog-excerpt {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 1rem;
  font-family: 'Inter', 'Segoe UI', sans-serif;
}

.blog-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.6);
  font-family: 'Inter', 'Segoe UI', sans-serif;
}

.view-more {
  display: block;
  text-align: center;
  padding: 1rem;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
  font-weight: 500;
  font-family: 'Poppins', 'Inter', sans-serif;
}

.view-more:hover {
  color: #ff94d2;
  background: rgba(255, 255, 255, 0.03);
}

/* 推荐用户部分 */
.recommended-users {
  margin-top: 3rem;
}

.section-title {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  text-align: center;
  color: #fff;
  font-family: 'Poppins', 'Inter', sans-serif;
}

.user-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.user-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  font-family: 'Inter', 'Segoe UI', sans-serif;
}

.user-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 148, 210, 0.4);
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(45deg, #ff94d2, #a18aff);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0 auto 1rem;
}

.username {
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.5rem;
  font-family: 'Poppins', 'Inter', sans-serif;
}

.follow-button {
  background: rgba(255, 148, 210, 0.2);
  color: #ff94d2;
  border: 1px solid rgba(255, 148, 210, 0.3);
  padding: 0.5rem 1rem;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
  font-family: 'Poppins', 'Inter', sans-serif;
}

.follow-button:hover {
  background: rgba(255, 148, 210, 0.3);
  transform: translateY(-1px);
}

/* 特色帖子样式 */
.featured-post {
  margin-bottom: 40px;
}

.post-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  overflow: hidden;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  display: flex;
  flex-direction: row;
  font-family: 'Inter', 'Segoe UI', sans-serif;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.featured {
  min-height: 250px;
}

.post-image {
  flex: 1;
  min-width: 300px;
  height: 100%;
  background: linear-gradient(45deg, #ff94d2, #a18aff);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
}

.post-content {
  flex: 1;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.post-meta {
  display: flex;
  gap: 15px;
  margin-bottom: 15px;
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
</style>