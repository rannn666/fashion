<template>
  <div class="star-icon">
    <svg width="24" height="20" viewBox="0 0 24 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- 渐变定义 -->
      <defs>
        <linearGradient id="starGradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff94d2" />
          <stop offset="100%" stop-color="#b388eb" />
        </linearGradient>
      </defs>
      <!-- 左侧大星星 -->
      <path d="M12 0L9.17157 7.07107L1.10051 7.07107L7.55033 11.95L4.72179 19L12 15.35L19.2782 19L16.4497 11.95L22.8995 7.07107L14.8284 7.07107L12 0Z" fill="url(#starGradient)"/>
      <!-- 大星星右下角的小星星 -->
      <path d="M20 10L20.866 12.26795L23.7321 12.26795L21.5351 14.0355L22.4011 16.903L20 15.5355L17.5989 16.903L18.4649 14.0355L16.2679 12.26795L19.134 12.26795L20 10Z" fill="url(#starGradient)"/>
    </svg>
  </div>
</template>

<script>
export default {
  name: 'StarIcon'
}
</script>

<style scoped>
.star-icon {
  display: inline-block;
  margin-right: 8px;
  vertical-align: middle;
}
</style>