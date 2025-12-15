<template>
  <div class="blog-create">
    <!-- 返回按钮 -->
    <div class="navigation">
      <button @click="$router.go(-1)" class="back-btn">
        ← 返回
      </button>
    </div>

    <!-- 发布表单 -->
    <div class="create-form-container">
      <h1 class="page-title">发布新博客</h1>
      
      <form @submit.prevent="submitPost" class="blog-form">
        <!-- 基本信息 -->
        <div class="form-section">
          <h2 class="section-title">基本信息</h2>
          
          <div class="form-group">
            <label for="title" class="form-label">标题 *</label>
            <input 
              v-model="form.title"
              type="text" 
              id="title"
              placeholder="给你的博客起个吸引人的标题..."
              class="form-input"
              required
              maxlength="200"
            >
            <div class="input-help">{{ form.title.length }}/200</div>
          </div>

          <div class="form-group">
            <label for="content_type" class="form-label">内容类型 *</label>
            <select v-model="form.content_type" id="content_type" class="form-select" required>
              <option value="">请选择内容类型</option>
              <option value="text">纯文字</option>
              <option value="video">视频</option>
              <option value="image">图片</option>
              <option value="mixed">混合内容</option>
            </select>
          </div>
        </div>

        <!-- 文字内容 -->
        <div v-if="form.content_type === 'text' || form.content_type === 'mixed'" class="form-section">
          <h2 class="section-title">文字内容</h2>
          
          <div class="form-group">
            <label for="content" class="form-label">正文内容 *</label>
            <textarea 
              v-model="form.content"
              id="content"
              placeholder="分享你的时尚见解、穿搭心得或生活感悟..."
              class="form-textarea"
              rows="10"
              required
            ></textarea>
            <div class="input-help">{{ form.content.length }} 字符</div>
          </div>
        </div>

        <!-- 视频上传 -->
        <div v-if="form.content_type === 'video' || form.content_type === 'mixed'" class="form-section">
          <h2 class="section-title">视频内容</h2>
          
          <div class="form-group">
            <label class="form-label">上传视频 *</label>
            <div class="file-upload-area" @click="triggerVideoUpload">
              <input 
                ref="videoInput"
                type="file" 
                @change="handleVideoUpload" 
                accept="video/*"
                class="hidden-input"
              >
              
              <div v-if="!form.video_file" class="upload-placeholder">
                <div class="upload-icon">📹</div>
                <p class="upload-text">点击上传视频</p>
                <p class="upload-help">支持 MP4, MOV, AVI 格式，大小不超过 100MB</p>
              </div>
              
              <div v-else class="uploaded-video">
                <video 
                  :src="videoPreviewUrl" 
                  class="video-preview"
                  controls
                ></video>
                <button @click.stop="removeVideo" class="remove-btn">移除</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 图片上传 -->
        <div v-if="form.content_type === 'image' || form.content_type === 'mixed'" class="form-section">
          <h2 class="section-title">图片内容</h2>
          
          <div class="form-group">
            <label class="form-label">上传图片 *</label>
            <div class="file-upload-area" @click="triggerImageUpload">
              <input 
                ref="imageInput"
                type="file" 
                @change="handleImageUpload" 
                accept="image/*"
                multiple
                class="hidden-input"
              >
              
              <div v-if="form.image_files.length === 0" class="upload-placeholder">
                <div class="upload-icon">🖼️</div>
                <p class="upload-text">点击上传图片</p>
                <p class="upload-help">支持 JPG, PNG, GIF 格式，可上传多张</p>
              </div>
              
              <div v-else class="uploaded-images">
                <div 
                  v-for="(image, index) in form.image_files" 
                  :key="index"
                  class="image-item"
                >
                  <img :src="image.preview" :alt="`图片 ${index + 1}`" class="image-preview">
                  <button @click.stop="removeImage(index)" class="remove-btn">×</button>
                </div>
                <div @click.stop="triggerImageUpload" class="add-more-images">
                  + 添加更多
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 预览区域 -->
        <div v-if="showPreview" class="form-section">
          <h2 class="section-title">预览效果</h2>
          <div class="preview-container">
            <div class="blog-post-preview">
              <h3 class="preview-title">{{ form.title || '标题预览' }}</h3>
              <div class="preview-meta">
                <span class="preview-author">{{ currentUser?.username || '用户' }}</span>
                <span class="preview-type">{{ getContentTypeLabel(form.content_type) }}</span>
              </div>
              <div class="preview-content">
                <p v-if="form.content" class="preview-text">{{ form.content.substring(0, 200) }}{{ form.content.length > 200 ? '...' : '' }}</p>
                <div v-if="form.video_file" class="preview-video">
                  <video :src="videoPreviewUrl" class="preview-video-element"></video>
                </div>
                <div v-if="form.image_files.length" class="preview-images">
                  <img 
                    v-for="(image, index) in form.image_files.slice(0, 3)" 
                    :key="index"
                    :src="image.preview" 
                    :alt="`预览图片 ${index + 1}`"
                    class="preview-image"
                  >
                  <span v-if="form.image_files.length > 3" class="more-images">
                    +{{ form.image_files.length - 3 }} 更多
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 表单操作 -->
        <div class="form-actions">
          <button 
            type="button" 
            @click="togglePreview" 
            class="preview-btn"
            :class="{ active: showPreview }"
          >
            👁️ {{ showPreview ? '隐藏' : '预览' }}
          </button>
          
          <div class="submit-actions">
            <button 
              type="button" 
              @click="saveDraft" 
              class="draft-btn"
              :disabled="isSubmitting"
            >
              💾 保存草稿
            </button>
            
            <button 
              type="submit" 
              class="publish-btn"
              :disabled="!isFormValid || isSubmitting"
            >
              {{ isSubmitting ? '发布中...' : '🚀 发布博客' }}
            </button>
          </div>
        </div>
      </form>
    </div>

    <!-- 进度条 -->
    <div v-if="isSubmitting" class="progress-overlay">
      <div class="progress-container">
        <div class="spinner"></div>
        <p>正在发布博客...</p>
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: uploadProgress + '%' }"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'BlogCreate',
  data() {
    return {
      form: {
        title: '',
        content_type: '',
        content: '',
        video_file: null,
        image_files: []
      },
      videoPreviewUrl: null,
      showPreview: false,
      isSubmitting: false,
      uploadProgress: 0,
      currentUser: null
    };
  },
  computed: {
    isFormValid() {
      if (!this.form.title.trim()) return false;
      if (!this.form.content_type) return false;
      
      switch (this.form.content_type) {
        case 'text':
          return this.form.content.trim().length > 0;
        case 'video':
          return this.form.video_file !== null;
        case 'image':
          return this.form.image_files.length > 0;
        case 'mixed':
          return (this.form.content.trim().length > 0 || this.form.video_file !== null || this.form.image_files.length > 0);
        default:
          return false;
      }
    }
  },
  created() {
    this.currentUser = this.$store?.state?.user || { username: '当前用户' };
  },
  methods: {
    triggerVideoUpload() {
      this.$refs.videoInput.click();
    },
    
    triggerImageUpload() {
      this.$refs.imageInput.click();
    },
    
    handleVideoUpload(event) {
      const file = event.target.files[0];
      if (!file) return;
      
      // 检查文件大小 (100MB)
      if (file.size > 100 * 1024 * 1024) {
        this.$toast?.error('视频文件大小不能超过100MB');
        return;
      }
      
      // 检查文件类型
      const allowedTypes = ['video/mp4', 'video/mov', 'video/avi', 'video/quicktime'];
      if (!allowedTypes.includes(file.type)) {
        this.$toast?.error('不支持的视频格式');
        return;
      }
      
      this.form.video_file = file;
      this.videoPreviewUrl = URL.createObjectURL(file);
    },
    
    handleImageUpload(event) {
      const files = Array.from(event.target.files);
      
      files.forEach(file => {
        // 检查文件大小 (10MB)
        if (file.size > 10 * 1024 * 1024) {
          this.$toast?.error(`图片 ${file.name} 大小超过10MB，已跳过`);
          return;
        }
        
        // 检查文件类型
        const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
        if (!allowedTypes.includes(file.type)) {
          this.$toast?.error(`不支持的图片格式: ${file.name}`);
          return;
        }
        
        // 检查最多9张图片
        if (this.form.image_files.length >= 9) {
          this.$toast?.error('最多只能上传9张图片');
          return;
        }
        
        const previewUrl = URL.createObjectURL(file);
        this.form.image_files.push({
          file,
          preview: previewUrl
        });
      });
      
      // 清空input
      event.target.value = '';
    },
    
    removeVideo() {
      this.form.video_file = null;
      if (this.videoPreviewUrl) {
        URL.revokeObjectURL(this.videoPreviewUrl);
        this.videoPreviewUrl = null;
      }
    },
    
    removeImage(index) {
      const image = this.form.image_files[index];
      if (image.preview) {
        URL.revokeObjectURL(image.preview);
      }
      this.form.image_files.splice(index, 1);
    },
    
    togglePreview() {
      this.showPreview = !this.showPreview;
    },
    
    async saveDraft() {
      // 保存草稿到本地存储
      localStorage.setItem('blog_draft', JSON.stringify({
        ...this.form,
        video_file: this.form.video_file?.name || null,
        image_files: this.form.image_files.map(img => ({ name: img.file.name, size: img.file.size }))
      }));
      this.$toast?.success('草稿已保存');
    },
    
    async submitPost() {
      if (!this.isFormValid) {
        this.$toast?.error('请填写完整信息');
        return;
      }
      
      this.isSubmitting = true;
      this.uploadProgress = 0;
      
      try {
        const formData = new FormData();
        formData.append('title', this.form.title);
        formData.append('content_type', this.form.content_type);
        formData.append('content', this.form.content || '');
        
        if (this.form.video_file) {
          formData.append('video_file', this.form.video_file);
        }
        
        // 添加图片文件
        this.form.image_files.forEach((imageObj) => {
          formData.append('image_files', imageObj.file);
        });
        
        // 模拟上传进度
        const progressInterval = setInterval(() => {
          if (this.uploadProgress < 90) {
            this.uploadProgress += Math.random() * 10;
          }
        }, 200);
        
        const response = await axios.post('/api/posts/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        
        clearInterval(progressInterval);
        this.uploadProgress = 100;
        
        // 清除草稿
        localStorage.removeItem('blog_draft');
        
        this.$toast?.success('博客发布成功！');
        this.$router.push(`/blog/${response.data.id}`);
        
      } catch (error) {
        console.error('发布博客失败:', error);
        this.$toast?.error('发布失败，请检查网络连接或登录状态');
      } finally {
        this.isSubmitting = false;
        this.uploadProgress = 0;
      }
    },
    
    getContentTypeLabel(type) {
      const typeMap = {
        'text': '文字',
        'video': '视频',
        'image': '图片',
        'mixed': '混合'
      };
      return typeMap[type] || '';
    },
    
    loadDraft() {
      const draft = localStorage.getItem('blog_draft');
      if (draft) {
        try {
          const draftData = JSON.parse(draft);
          this.form = {
            ...this.form,
            ...draftData
          };
          this.$toast?.info('已加载保存的草稿');
        } catch (error) {
          console.error('加载草稿失败:', error);
        }
      }
    }
  },
  
  mounted() {
    this.loadDraft();
  },
  
  beforeUnmount() {
    // 清理预览URL
    if (this.videoPreviewUrl) {
      URL.revokeObjectURL(this.videoPreviewUrl);
    }
    this.form.image_files.forEach(img => {
      if (img.preview) {
        URL.revokeObjectURL(img.preview);
      }
    });
  }
};
</script>

<style scoped>
.blog-create {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  color: #4a3c5c;
}

.navigation {
  margin-bottom: 20px;
}

.back-btn {
  padding: 10px 20px;
  border: 2px solid #ff69b4;
  border-radius: 20px;
  background: transparent;
  color: #ff69b4;
  cursor: pointer;
  transition: all 0.3s;
}

.back-btn:hover {
  background: #ff69b4;
  color: #fff;
}

.create-form-container {
  background: transparent;
  border-radius: 15px;
  padding: 30px;
  margin-bottom: 20px;
  border: 1px solid rgba(74, 60, 92, 0.3);
}

.page-title {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 30px;
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.form-section {
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 1px solid #333;
}

.form-section:last-child {
  border-bottom: none;
}

.section-title {
  font-size: 1.3rem;
  margin-bottom: 20px;
  color: #ff69b4;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #ccc;
}

.form-input, .form-select, .form-textarea {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
  outline: none;
  border-color: #ff69b4;
}

.form-textarea {
  resize: vertical;
  min-height: 120px;
}

.input-help {
  margin-top: 5px;
  font-size: 0.85rem;
  color: #888;
  text-align: right;
}

.file-upload-area {
  border: 2px dashed rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  padding: 30px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s;
  background: rgba(255, 255, 255, 0.15);
}

.file-upload-area:hover {
  border-color: #ff69b4;
  background: rgba(255, 105, 180, 0.05);
}

.hidden-input {
  display: none;
}

.upload-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.upload-icon {
  font-size: 3rem;
  opacity: 0.6;
}

.upload-text {
  font-size: 1.1rem;
  color: #ccc;
}

.upload-help {
  font-size: 0.9rem;
  color: #888;
}

.uploaded-video, .uploaded-images {
  display: flex;
  flex-direction: column;
  gap: 15px;
  align-items: center;
}

.video-preview {
  max-width: 100%;
  max-height: 300px;
  border-radius: 10px;
}

.image-item {
  position: relative;
  display: inline-block;
}

.image-preview {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 10px;
}

.remove-btn {
  position: absolute;
  top: -10px;
  right: -10px;
  width: 25px;
  height: 25px;
  border: none;
  border-radius: 50%;
  background: #ff4444;
  color: #fff;
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}

.remove-btn:hover {
  background: #ff6666;
  transform: scale(1.1);
}

.add-more-images {
  width: 150px;
  height: 150px;
  border: 2px dashed #666;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #888;
  cursor: pointer;
  transition: all 0.3s;
}

.add-more-images:hover {
  border-color: #c67bb4;
  color: #c67bb4;
}

.preview-container {
  background: rgba(255, 255, 255, 0.15);
  border-radius: 10px;
  padding: 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.blog-post-preview {
  max-width: 100%;
}

.preview-title {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #fff;
}

.preview-meta {
  display: flex;
  gap: 15px;
  margin-bottom: 15px;
  font-size: 0.9rem;
  color: #888;
}

.preview-type {
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  color: #fff;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.8rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.preview-content {
  color: #ccc;
  line-height: 1.6;
}

.preview-text {
  margin-bottom: 15px;
}

.preview-video {
  margin-bottom: 15px;
}

.preview-video-element {
  width: 100%;
  max-height: 200px;
  border-radius: 10px;
}

.preview-images {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.preview-image {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 8px;
}

.more-images {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  color: #ccc;
  font-size: 0.8rem;
}

.form-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.3);
}

.preview-btn {
  padding: 10px 20px;
  border: 2px solid rgba(74, 60, 92, 0.3);
  border-radius: 20px;
  background: transparent;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s;
}

.preview-btn.active, .preview-btn:hover {
  border-color: #c67bb4;
  color: #c67bb4;
}

.submit-actions {
  display: flex;
  gap: 15px;
}

.draft-btn {
  padding: 12px 24px;
  border: 2px solid rgba(74, 60, 92, 0.3);
  border-radius: 25px;
  background: transparent;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s;
}

.draft-btn:hover:not(:disabled) {
  border-color: rgba(255, 255, 255, 0.5);
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
}

.publish-btn {
  padding: 12px 24px;
  border: 1px solid rgba(74, 60, 92, 0.3);
  border-radius: 25px;
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.3s;
}

.publish-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(200, 140, 220, 0.3);
}

.publish-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.progress-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.progress-container {
  background: transparent;
  padding: 30px;
  border-radius: 15px;
  text-align: center;
  color: #fff;
  border: 1px solid rgba(74, 60, 92, 0.3);
}

.progress-bar {
  width: 300px;
  height: 6px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
  margin-top: 20px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  transition: width 0.3s;
  border-radius: 3px;
}

@media (max-width: 768px) {
  .blog-create {
    padding: 15px;
  }
  
  .create-form-container {
    padding: 20px;
  }
  
  .form-actions {
    flex-direction: column;
    gap: 15px;
  }
  
  .submit-actions {
    width: 100%;
    justify-content: space-between;
  }
  
  .progress-container {
    margin: 0 20px;
  }
}
</style>