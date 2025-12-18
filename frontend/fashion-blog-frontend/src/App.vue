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
  background: linear-gradient(90deg, #a8e6cf 0%, #a8e6cf 50%, #d4e4d1 55%, #e2dcc6 60%, #ead4c1 65%, #eacbb8 70%, #edc5b3 75%, #ffd3b6 80%);
  color: #4a3c5c;
  height: 100%;
  width: 100%;
  overflow-x: auto;
  overflow-y: auto;
}

body {
  background: linear-gradient(90deg, #a8e6cf 0%, #a8e6cf 50%, #d4e4d1 55%, #e2dcc6 60%, #ead4c1 65%, #eacbb8 70%, #edc5b3 75%, #ffd3b6 80%);
  color: #4a3c5c;
  margin: 0;
  padding: 0;
}

#app {
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(90deg, #a8e6cf 0%, #a8e6cf 50%, #d4e4d1 55%, #e2dcc6 60%, #ead4c1 65%, #eacbb8 70%, #edc5b3 75%, #ffd3b6 80%);
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  padding: 0;
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
</style>


















