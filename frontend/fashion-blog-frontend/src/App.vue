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
  /* 优雅蓝紫色冷色调渐变背景 */
  background: 
    /* 深紫色渐变 - 左上角 */
    radial-gradient(circle at 15% 15%, rgba(75, 0, 130, 0.6) 0%, rgba(75, 0, 130, 0.4) 25%, rgba(75, 0, 130, 0.2) 50%, transparent 70%),
    /* 蓝色渐变 - 右下角 */
    radial-gradient(circle at 85% 85%, rgba(65, 105, 225, 0.6) 0%, rgba(65, 105, 225, 0.4) 25%, rgba(65, 105, 225, 0.2) 50%, transparent 70%),
    /* 蓝紫色线性渐变 */
    linear-gradient(135deg, 
      #1a1a2e 0%,      /* 深蓝黑色 */
      #16213e 20%,     /* 深蓝色 */
      #1f4068 40%,     /* 中蓝色 */
      #533483 60%,     /* 蓝紫色 */
      #e94560 80%,     /* 玫瑰红色点缀 */
      #0f3460 100%     /* 深蓝色 */
    );
  /* 多层混合模式创造深度感 */
  background-blend-mode: multiply, screen, normal;
  /* 固定背景，让滚动时保持效果 */
  background-attachment: fixed;
  /* 确保平滑过渡 */
  background-size: cover;
  background-repeat: no-repeat;
}

body {
  margin: 0;
  padding: 0;
  color: #e8e8e8; /* 浅色文字，适应深色冷色调背景 */
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
  border-width: 0 !important;
  border-style: none !important;
  border-color: transparent !important;
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