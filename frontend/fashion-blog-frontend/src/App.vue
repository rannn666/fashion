<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  font-family: 'Helvetica Neue', 'Arial', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'WenQuanYi Micro Hei', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  height: 100%;
  width: 100%;
  overflow-x: auto;
  overflow-y: auto;
  /* 黄蓝渐变背景，黄色占比约40%，使用亮黄色并加入浅黄色过渡 */
  background: 
    /* 柔和黄色径向渐变 - 左上角 */
    radial-gradient(circle at 15% 15%, rgba(255, 255, 200, 0.5) 0%, rgba(255, 255, 200, 0.3) 30%, rgba(255, 255, 200, 0.1) 60%, transparent 80%),
    /* 柔和蓝色径向渐变 - 右下角 */
    radial-gradient(circle at 85% 85%, rgba(173, 216, 255, 0.4) 0%, rgba(173, 216, 255, 0.2) 40%, rgba(173, 216, 255, 0.1) 70%, transparent 90%),
    /* 黄蓝绿线性渐变，亮黄色后加入浅黄色过渡再接蓝绿色 */
    linear-gradient(135deg, 
      #ffff99 0%,      /* 亮黄色 - 占比约25% */
      #ffffcc 25%,     /* 浅黄色 - 过渡色 */
      #cce6ff 40%,     /* 浅蓝绿色 */
      #a0eaff 70%,     /* 浅蓝绿色 */
      #cceeff 100%     /* 浅蓝绿色 */
    );
  /* 多层混合模式创造柔和感 */
  background-blend-mode: soft-light, overlay, normal;
  /* 固定背景，让滚动时保持效果 */
  background-attachment: fixed;
  /* 确保平滑过渡 */
  background-size: cover;
  background-repeat: no-repeat;
}

body {
  margin: 0;
  padding: 0;
  color: #444; /* 稍浅的深色文字，适应明亮背景 */
}

#app {
  width: 100%;
  min-height: 100vh;
  background: transparent;
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  padding: 0;
}

/* 全局字体颜色调整 - 针对明亮背景优化 */
body, .header, .site-title, .section-title, .post-card h3, .post-card p, 
.footer p, .categories-section h3, .tags-section h3, .post-title, .post-excerpt {
  color: #444 !important; /* 稍浅的深灰色文字，确保在明亮背景下清晰可见 */
}

/* 特别针对网站标题的样式 */
.site-title {
  color: #000 !important; /* 确保网站标题使用纯黑色 */
  text-shadow: none !important; /* 移除可能的文本阴影效果 */
}

/* 导航按钮文字颜色调整 */
.main-nav-buttons a {
  color: rgba(68, 68, 68, 0.8) !important; /* 稍浅的深灰色，透明度0.8 */
}

.main-nav-buttons a:hover,
.main-nav-buttons a.active {
  color: #ff69b4 !important; /* 保持粉色悬停和激活效果 */
}

/* 社交链接颜色调整 */
.social-links a {
  color: rgba(68, 68, 68, 0.7) !important;
}

.social-links a:hover {
  color: #444 !important;
}

/* 其他可能使用白色文字的元素 */
.section-title, .post-card h3, .post-card p, .categories-section h3, .tags-section h3,
.post-title, .post-excerpt, .read-more, .floating-indicator {
  color: #444 !important;
}

/* 选中状态的文字颜色 */
.main-nav-buttons a.active {
  color: #444 !important;
  font-weight: 600 !important;
}

/* 特别针对时间显示的样式，使用更深的灰色以便更好可见 */
.post-meta,
.news-meta,
.blog-meta,
.post-date,
.news-date,
.blog-date,
.date,
.time,
.created-at,
.updated-at {
  color: #333 !important; /* 深灰色，比默认的#444更深一点，提高可见度 */
  opacity: 1 !important; /* 确保完全不透明 */
}

/* 全局强制覆盖白色字体为灰色 */
*[style*="color: white"],
*[style*="color: #fff"],
*[style*="color: #ffffff"],
.color-white,
.text-white,
.white-text,
.white-font,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6,
.title,
.subtitle,
.heading,
.caption,
.news-title,
.news-excerpt,
.post-title,
.post-excerpt,
.section-title,
.category,
.tag,
.navbar *,
.nav-link,
.nav-item,
.btn,
.button,
.link,
.anchor,
a:link,
a:visited,
a:hover,
a:active {
  color: #444 !important;
}

/* 特别针对透明度白色文字的覆盖 */
*[style*="rgba(255, 255, 255,"] {
  color: rgba(68, 68, 68, 0.8) !important;
}

/* 覆盖可能的通用白色文字类 */
.white,
.light-text,
.light-color,
.bright-text {
  color: #444 !important;
}

/* 覆盖特定元素中的白色文字 */
.top-nav a,
.main-nav a,
.navbar-brand,
.navbar-nav .nav-link,
.floating-indicator,
.read-more:hover,
.post-card h3,
.post-card p,
.news-item h3,
.news-item p,
.news-title,
.news-excerpt,
.post-title,
.post-excerpt,
.section-title,
.welcome-title,
.header *,
.footer *,
.social-links *,
.action-buttons *,
.content-type-name,
.content-type-desc,
.title-input,
.comment-text,
.comment-author,
.comment-date {
  color: #444 !important;
}

/* 全局导航按钮边框清除 */
a, button, input[type="submit"], input[type="button"] {
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
}

/* 特殊CSS类确保按钮完全无边框 */
.no-border-btn {
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
  border-radius: 25px !important;
}

/* 悬停状态也确保无边框 */
.no-border-btn:hover {
  border: none !important;
  outline: none !important;
  box-shadow: 0 5px 15px rgba(255, 105, 180, 0.3) !important;
  border-width: 0 !important;
  border-style: none !important;
  border-color: transparent !important;
}

/* 彻底隐藏所有元素的焦点样式 */
*:focus,
*:focus-visible,
*:focus-within,
a:focus,
button:focus,
input:focus,
textarea:focus,
select:focus,
img:focus,
div:focus {
  outline: none !important; /* 完全隐藏焦点轮廓 */
  outline-offset: 0 !important;
  box-shadow: none !important; /* 移除可能存在的box-shadow */
  border-color: transparent !important; /* 确保边框也透明 */
  background-color: inherit !important; /* 确保背景色不变 */
}

/* 特殊针对主导航按钮的全局清除 */
.main-nav-buttons,
.main-nav-buttons a,
.main-nav-buttons ul,
.main-nav-buttons li {
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
  border-width: 0 !important;
  border-style: none !important;
  border-color: transparent !important;
}

/* 确保所有链接都没有边框 */
a[href],
a[href]:hover,
a[href]:active,
a[href]:focus {
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
}
</style>