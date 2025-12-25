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
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  height: 100%;
  width: 100%;
  overflow-x: auto;
  overflow-y: auto;
  /* 水面交融背景效果 */
  background: 
    /* 蓝绿色水域 - 左上角 */
    radial-gradient(circle at 25% 25%, rgba(168, 230, 207, 0.9) 0%, rgba(168, 230, 207, 0.6) 20%, rgba(168, 230, 207, 0.3) 45%, transparent 65%),
    /* 淡粉色水域 - 右下角 */
    radial-gradient(circle at 75% 75%, rgba(255, 192, 203, 0.9) 0%, rgba(255, 192, 203, 0.6) 20%, rgba(255, 192, 203, 0.3) 45%, transparent 65%),
    /* 交融区域渐变 */
    linear-gradient(135deg, 
      #a8e6cf 0%,      /* 纯蓝绿色 */
      #a8e6cf 20%,     /* 保持蓝绿色 */
      #a8e6cf 25%,     /* 开始出现中间色 */
      #b8e6d3 30%,     /* 轻微粉色调的蓝绿色 */
      #c8d4d8 35%,     /* 中性灰蓝色 */
      #d4d8d3 40%,     /* 中性调色 */
      #e0d4ce 42%,     /* 温暖的中间色 */
      #e8d4ce 44%,     /* 继续交融 */
      #f0d4c9 46%,     /* 接近淡粉色 */
      #ffc0cb 48%,     /* 开始出现淡粉色 */
      #ffc0cb 60%,     /* 淡粉色加强 */
      #ffc0cb 80%,     /* 保持淡粉色 */
      #ffc0cb 100%     /* 纯淡粉色 */
    );
  /* 多层混合模式创造交融效果 */
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
  color: #4a3c5c;
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