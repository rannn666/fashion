<template>
  <div class="blog-detail">
    <!-- 返回按钮 -->
    <div class="navigation">
      <button @click="$router.go(-1)" class="back-btn">
        ← 返回
      </button>
    </div>

    <!-- 加载状态 -->
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>加载中...</p>
    </div>

    <!-- 博客内容 -->
    <article v-else-if="post" class="post-content">
      <!-- 文章头部 -->
      <header class="post-header">
        <h1 class="post-title">{{ post.title }}</h1>
        
        <!-- 作者信息 -->
        <div class="author-section">
          <div class="author-avatar">{{ post.author.username.charAt(0).toUpperCase() }}</div>
          <div class="author-info">
            <h3 class="author-name">{{ post.author.username }}</h3>
            <p class="post-date">{{ formatDate(post.created_at) }}</p>
          </div>
          <div class="post-actions">
            <button 
              v-if="post.liked_by_user" 
              @click="unlikePost" 
              class="action-btn liked"
            >
              ❤️ {{ post.likes_count }}
            </button>
            <button 
              v-else 
              @click="likePost" 
              class="action-btn"
            >
              🤍 {{ post.likes_count }}
            </button>
          </div>
        </div>

        <!-- 内容类型标签 -->
        <div class="content-type-badge" :class="post.content_type">
          {{ getContentTypeLabel(post.content_type) }}
        </div>
      </header>

      <!-- 文章主体内容 -->
      <div class="post-body">
        <!-- 文字内容 -->
        <div v-if="post.content" class="text-content">
          <p v-for="(paragraph, index) in formatContent(post.content)" :key="index" class="content-paragraph">
            {{ paragraph }}
          </p>
        </div>

        <!-- 视频内容 -->
        <div v-if="post.content_type === 'video' && post.video_file" class="video-content">
          <video 
            :src="post.video_file" 
            controls 
            class="main-video"
            @loadstart="videoLoading = true"
            @canplay="videoLoading = false"
          ></video>
          <div v-if="videoLoading" class="video-loading">
            <div class="spinner"></div>
            <p>视频加载中...</p>
          </div>
        </div>

        <!-- 图片内容 -->
        <div v-if="post.content_type === 'image' && post.image_files?.length" class="image-content">
          <div class="image-gallery">
            <img 
              v-for="(image, index) in post.image_files" 
              :key="index"
              :src="image.file" 
              :alt="`${post.title} - 图片 ${index + 1}`"
              class="gallery-image"
              @click="openImageModal(index)"
            >
          </div>
        </div>

        <!-- 混合内容 -->
        <div v-if="post.content_type === 'mixed'" class="mixed-content">
          <div v-if="post.content" class="text-content">
            <p v-for="(paragraph, index) in formatContent(post.content)" :key="index" class="content-paragraph">
              {{ paragraph }}
            </p>
          </div>
          
          <div v-if="post.video_file" class="video-section">
            <video 
              :src="post.video_file" 
              controls 
              class="main-video"
            ></video>
          </div>
          
          <div v-if="post.image_files?.length" class="image-section">
            <div class="image-gallery">
              <img 
                v-for="(image, index) in post.image_files" 
                :key="index"
                :src="image.file" 
                :alt="`${post.title} - 图片 ${index + 1}`"
                class="gallery-image"
                @click="openImageModal(index)"
              >
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- 评论区域 -->
    <section class="comments-section">
      <h2 class="comments-title">评论 ({{ post?.comments_count || 0 }})</h2>
      
      <!-- 发表评论 -->
      <div class="comment-form">
        <textarea 
          v-model="newComment"
          @keydown.ctrl.enter="submitComment"
          placeholder="写下你的想法... (Ctrl+Enter 发送)"
          class="comment-input"
          rows="3"
        ></textarea>
        <button @click="submitComment" :disabled="!newComment.trim()" class="submit-btn">
          发表评论
        </button>
      </div>

      <!-- 评论列表 -->
      <div class="comments-list">
        <div v-if="loadingComments" class="loading-comments">
          <div class="spinner small"></div>
          <p>加载评论中...</p>
        </div>
        
        <div v-else-if="comments.length === 0" class="no-comments">
          <p>暂无评论，来发表第一条评论吧！</p>
        </div>

        <div v-else class="comments">
          <CommentItem 
            v-for="comment in comments" 
            :key="comment.id"
            :comment="comment"
            @reply="handleReply"
          />
        </div>
      </div>
    </section>

    <!-- 图片模态框 -->
    <ImageModal 
      v-if="showImageModal"
      :images="post?.image_files || []"
      :current-index="currentImageIndex"
      @close="closeImageModal"
      @next="nextImage"
      @previous="previousImage"
    />
  </div>
</template>

<script>
import axios from 'axios';
import CommentItem from '../components/CommentItem.vue';
import ImageModal from '../components/ImageModal.vue';

export default {
  name: 'BlogDetail',
  components: {
    CommentItem,
    ImageModal
  },
  data() {
    return {
      post: null,
      comments: [],
      newComment: '',
      loading: false,
      loadingComments: false,
      videoLoading: false,
      showImageModal: false,
      currentImageIndex: 0
    };
  },
  created() {
    this.fetchPost();
    this.fetchComments();
  },
  methods: {
    async fetchPost() {
      this.loading = true;
      try {
        const response = await axios.get(`/api/posts/${this.$route.params.id}/`);
        this.post = response.data;
      } catch (error) {
        console.error('获取博客文章失败:', error);
        this.$toast?.error('获取博客文章失败');
        this.$router.push('/blog');
      } finally {
        this.loading = false;
      }
    },

    async fetchComments() {
      this.loadingComments = true;
      try {
        const response = await axios.get(`/api/posts/${this.$route.params.id}/comments/`);
        this.comments = response.data;
      } catch (error) {
        console.error('获取评论失败:', error);
      } finally {
        this.loadingComments = false;
      }
    },

    async likePost() {
      try {
        const response = await axios.post(`/api/posts/${this.post.id}/like/`);
        this.post.likes_count = response.data.likes_count;
        this.post.liked_by_user = response.data.status === 'liked';
      } catch (error) {
        console.error('点赞失败:', error);
        this.$toast?.error('点赞失败，请登录后再试');
      }
    },

    async unlikePost() {
      try {
        const response = await axios.post(`/api/posts/${this.post.id}/like/`);
        this.post.likes_count = response.data.likes_count;
        this.post.liked_by_user = response.data.status === 'liked';
      } catch (error) {
        console.error('取消点赞失败:', error);
      }
    },

    async submitComment() {
      if (!this.newComment.trim()) return;
      
      try {
        const response = await axios.post('/api/comments/', {
          post: this.post.id,
          content: this.newComment
        });
        
        this.comments.push(response.data);
        this.newComment = '';
        this.post.comments_count++;
        this.$toast?.success('评论发表成功');
      } catch (error) {
        console.error('发表评论失败:', error);
        this.$toast?.error('发表评论失败，请登录后再试');
      }
    },

    handleReply(commentData) {
      // 处理回复逻辑
      this.comments.push(commentData);
      this.post.comments_count++;
    },

    formatContent(content) {
      return content.split('\n').filter(p => p.trim());
    },

    getContentTypeLabel(type) {
      const typeMap = {
        'text': '文字',
        'video': '视频',
        'image': '图片',
        'mixed': '混合'
      };
      return typeMap[type] || type;
    },

    formatDate(dateString) {
      const date = new Date(dateString);
      const now = new Date();
      const diff = now - date;
      
      const seconds = Math.floor(diff / 1000);
      const minutes = Math.floor(seconds / 60);
      const hours = Math.floor(minutes / 60);
      const days = Math.floor(hours / 24);
      
      if (days > 0) return `${days}天前`;
      if (hours > 0) return `${hours}小时前`;
      if (minutes > 0) return `${minutes}分钟前`;
      return '刚刚';
    },

    openImageModal(index) {
      this.currentImageIndex = index;
      this.showImageModal = true;
    },

    closeImageModal() {
      this.showImageModal = false;
    },

    nextImage() {
      if (this.currentImageIndex < this.post.image_files.length - 1) {
        this.currentImageIndex++;
      }
    },

    previousImage() {
      if (this.currentImageIndex > 0) {
        this.currentImageIndex--;
      }
    }
  }
};
</script>

<style scoped>
.blog-detail {
  min-height: 100vh;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  color: #fff;
  padding: 20px;
  box-sizing: border-box;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 0;
  margin-bottom: 30px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.nav-left, .nav-center, .nav-right {
  flex: 1;
  text-align: center;
}

.nav-left {
  text-align: left;
}

.nav-right {
  text-align: right;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  transition: color 0.3s ease;
  padding: 10px 15px;
  border-radius: 10px;
  transition: all 0.3s ease;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.nav-link:hover {
  color: #ff94d2;
  background: rgba(255, 148, 210, 0.1);
}

.blog-content {
  max-width: 800px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  padding: 40px;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-header {
  text-align: center;
  margin-bottom: 30px;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 15px;
  color: #fff;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-meta {
  display: flex;
  justify-content: center;
  gap: 20px;
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.95rem;
  margin-bottom: 20px;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-author {
  font-weight: 600;
  color: #ff94d2;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-image {
  width: 100%;
  height: 400px;
  border-radius: 10px;
  overflow: hidden;
  margin: 20px 0;
  background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2rem;
  font-weight: bold;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-body {
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.1rem;
  margin: 30px 0;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.blog-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  margin-top: 30px;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.stats {
  display: flex;
  gap: 20px;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 8px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.95rem;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.action-buttons {
  display: flex;
  gap: 10px;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.action-btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
  font-size: 0.95rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.like-btn {
  background: rgba(255, 148, 210, 0.2);
  color: #ff94d2;
}

.like-btn:hover {
  background: rgba(255, 148, 210, 0.3);
}

.comment-btn {
  background: rgba(161, 138, 255, 0.2);
  color: #a18aff;
}

.comment-btn:hover {
  background: rgba(161, 138, 255, 0.3);
}

.share-btn {
  background: rgba(102, 204, 255, 0.2);
  color: #66ccff;
}

.share-btn:hover {
  background: rgba(102, 204, 255, 0.3);
}

.comments-section {
  max-width: 800px;
  margin: 40px auto 0;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  padding: 30px;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comments-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 20px;
  color: #fff;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-form {
  margin-bottom: 30px;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-input {
  width: 100%;
  padding: 15px;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 1rem;
  resize: vertical;
  min-height: 100px;
  margin-bottom: 10px;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-input:focus {
  outline: none;
  border-color: #ff94d2;
  box-shadow: 0 0 0 3px rgba(255, 148, 210, 0.3);
}

.submit-comment-btn {
  padding: 12px 24px;
  background: rgba(255, 148, 210, 0.2);
  color: #ff94d2;
  border: 2px solid rgba(255, 148, 210, 0.3);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
  font-size: 0.95rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.submit-comment-btn:hover {
  background: rgba(255, 148, 210, 0.3);
  transform: translateY(-2px);
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

@media (max-width: 768px) {
  .blog-detail {
    padding: 15px;
  }
  
  .navbar {
    margin-bottom: 20px;
  }
  
  .nav-left, .nav-right {
    flex: 0.5;
  }
  
  .nav-center {
    flex: 1;
  }
  
  .blog-content {
    padding: 25px;
  }
  
  .blog-title {
    font-size: 2rem;
  }
  
  .blog-image {
    height: 250px;
    font-size: 1.5rem;
  }
  
  .blog-body {
    font-size: 1rem;
  }
  
  .blog-footer {
    flex-direction: column;
    gap: 15px;
    align-items: flex-start;
  }
  
  .action-buttons {
    width: 100%;
    justify-content: space-between;
  }
}
</style>