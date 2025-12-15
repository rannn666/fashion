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
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  color: #fff;
}

.navigation {
  margin-bottom: 20px;
}

.back-btn {
  padding: 10px 20px;
  border: 2px solid rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  background: transparent;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s;
}

.back-btn:hover {
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  border-color: transparent;
  color: #fff;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 300px;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(255, 255, 255, 0.2);
  border-top: 4px solid #c67bb4;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

.spinner.small {
  width: 20px;
  height: 20px;
  border-width: 2px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.post-content {
  background: transparent;
  border-radius: 15px;
  overflow: hidden;
  margin-bottom: 40px;
  border: 1px solid rgba(74, 60, 92, 0.3);
}

.post-header {
  padding: 30px;
  position: relative;
}

.post-title {
  font-size: 2.5rem;
  margin-bottom: 20px;
  line-height: 1.2;
  background: linear-gradient(45deg, #ff69b4, #ff1493);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.author-section {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 20px;
}

.author-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(45deg, #ff69b4, #ff1493);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 1.5rem;
  font-weight: bold;
}

.author-info {
  flex: 1;
}

.author-name {
  margin: 0;
  font-size: 1.2rem;
  color: #fff;
}

.post-date {
  margin: 5px 0 0 0;
  color: #888;
  font-size: 0.9rem;
}

.post-actions {
  display: flex;
  gap: 10px;
}

.action-btn {
  padding: 10px 20px;
  border: 2px solid #ff69b4;
  border-radius: 20px;
  background: transparent;
  color: #ff69b4;
  cursor: pointer;
  transition: all 0.3s;
}

.action-btn:hover, .action-btn.liked {
  background: #ff69b4;
  color: #fff;
}

.content-type-badge {
  position: absolute;
  top: 30px;
  right: 30px;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: bold;
}

.content-type-badge.video { background: #ff4444; color: #fff; }
.content-type-badge.image { background: #44ff44; color: #000; }
.content-type-badge.text { background: #4444ff; color: #fff; }
.content-type-badge.mixed { background: #ff44ff; color: #fff; }

.post-body {
  padding: 0 30px 30px;
}

.text-content {
  margin-bottom: 30px;
}

.content-paragraph {
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 20px;
  color: #ccc;
}

.video-content, .image-content, .mixed-content {
  margin-bottom: 30px;
}

.main-video {
  width: 100%;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
}

.video-loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.image-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 15px;
}

.gallery-image {
  width: 100%;
  height: 250px;
  object-fit: cover;
  border-radius: 10px;
  cursor: pointer;
  transition: transform 0.3s;
}

.gallery-image:hover {
  transform: scale(1.05);
}

.comments-section {
  background: transparent;
  border-radius: 15px;
  padding: 30px;
  border: 1px solid rgba(74, 60, 92, 0.3);
}

.comments-title {
  font-size: 1.5rem;
  margin-bottom: 25px;
  color: #fff;
}

.comment-form {
  margin-bottom: 30px;
}

.comment-input {
  width: 100%;
  padding: 15px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  font-size: 1rem;
  line-height: 1.5;
  resize: vertical;
  margin-bottom: 15px;
}

.comment-input:focus {
  outline: none;
  border-color: #c67bb4;
}

.submit-btn {
  padding: 12px 24px;
  border: 1px solid rgba(74, 60, 92, 0.3);
  border-radius: 20px;
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(200, 140, 220, 0.3);
}

.submit-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.comments-list {
  min-height: 200px;
}

.loading-comments, .no-comments {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
  color: #888;
}

@media (max-width: 768px) {
  .blog-detail {
    padding: 15px;
  }
  
  .post-header {
    padding: 20px;
  }
  
  .post-title {
    font-size: 2rem;
  }
  
  .author-section {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  
  .post-body {
    padding: 0 20px 20px;
  }
  
  .comments-section {
    padding: 20px;
  }
  
  .image-gallery {
    grid-template-columns: 1fr;
  }
}
</style>