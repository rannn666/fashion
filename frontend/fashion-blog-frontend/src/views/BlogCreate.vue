<template>
  <div class="blog-create">
    <!-- 导航栏 -->
    <nav class="navbar">
      <div class="nav-left">
        <a href="#" @click="goBack" class="nav-link">
          <span class="nav-icon">⬅️</span>
          返回
        </a>
      </div>
      <div class="nav-center">
        <h1 class="nav-title">创建博客</h1>
      </div>
      <div class="nav-right">
        <button 
          @click="submitBlog" 
          :disabled="!isValid || uploading"
          class="publish-btn"
        >
          {{ uploading ? '发布中...' : '发布' }}
        </button>
      </div>
    </nav>

    <div class="create-content">
      <!-- 分类选择 -->
      <div class="section">
        <label class="section-label">分类 *</label>
        <div class="category-grid">
          <div 
            v-for="category in categories" 
            :key="category.value"
            class="category-item"
            :class="{ active: formData.category === category.value }"
            @click="selectCategory(category.value)"
          >
            {{ category.label }}
          </div>
        </div>
        <div v-if="!formData.category" class="error-message">请选择分类</div>
      </div>

      <!-- 标签输入 -->
      <div class="section">
        <label class="section-label">标签</label>
        <div class="tag-input-container">
          <input
            v-model="tagInput"
            @keyup.enter="addTag"
            placeholder="输入标签，按回车添加"
            class="tag-input"
          />
          <button @click="addTag" class="add-tag-btn">添加</button>
        </div>
        <div class="tags-list">
          <span 
            v-for="(tag, index) in formData.tags" 
            :key="index"
            class="tag-item"
          >
            #{{ tag }}
            <button @click="removeTag(index)" class="remove-tag">×</button>
          </span>
        </div>
      </div>

      <!-- 内容类型选择 -->
      <div class="section">
        <label class="section-label">内容类型 *</label>
        <div class="content-type-grid">
          <div 
            v-for="type in contentTypes" 
            :key="type.value"
            class="content-type-item"
            :class="{ active: formData.content_type === type.value }"
            @click="selectContentType(type.value)"
          >
            <div class="content-type-header">
              <span class="content-type-icon">{{ type.icon }}</span>
              <span class="content-type-name">{{ type.name }}</span>
            </div>
            <p class="content-type-desc">{{ type.description }}</p>
          </div>
        </div>
      </div>

      <!-- 文本内容编辑器 -->
      <div v-if="showTextContent" class="section">
        <label class="section-label">标题 *</label>
        <input
          v-model="formData.title"
          placeholder="请输入标题"
          class="title-input"
        />
        <label class="section-label">内容 *</label>
        <textarea
          v-model="formData.content"
          placeholder="分享你的时尚心得..."
          class="content-textarea"
        ></textarea>
      </div>

      <!-- 媒体上传区域 -->
      <div v-if="showMediaUpload" class="section">
        <label class="section-label">
          {{ formData.content_type === 'image' ? '图片' : 
             formData.content_type === 'video' ? '视频' : '媒体文件' }} *
        </label>
        <div 
          class="upload-area"
          @dragover.prevent="handleDragOver"
          @drop.prevent="handleDrop"
        >
          <input
            type="file"
            ref="fileInput"
            @change="handleFileSelect"
            :accept="acceptedFormats"
            multiple
            style="display: none"
          />
          <div class="upload-content" @click="triggerFileSelect">
            <div class="upload-icon">📁</div>
            <p class="upload-text">点击或拖拽上传</p>
            <p class="upload-hint">
              {{
                formData.content_type === 'image' ? '支持 JPG、PNG 格式，单张不超过5MB' :
                formData.content_type === 'video' ? '支持 MP4、WebM 格式，单个不超过500MB' :
                '支持图片和视频格式'
              }}
            </p>
          </div>
          
          <!-- 预览区域 -->
          <div v-if="hasPreviewContent" class="preview-section">
            <h3>预览</h3>
            
            <!-- 预览标题 -->
            <div v-if="formData.title" class="preview-title">
              {{ formData.title }}
            </div>
            
            <!-- 预览内容 -->
            <div v-if="formData.content" class="preview-content">
              {{ formData.content }}
            </div>
            
            <!-- 预览标签 -->
            <div v-if="formData.tags.length > 0" class="preview-tags">
              <span 
                v-for="(tag, index) in formData.tags" 
                :key="'tag-' + index"
                class="preview-tag"
              >
                #{{ tag }}
              </span>
            </div>
            
            <!-- 预览媒体文件 -->
            <div v-if="previewFiles.length > 0" class="preview-files">
              <div 
                v-for="(file, index) in previewFiles" 
                :key="'preview-' + index"
                class="preview-file"
              >
                <div v-if="file.type.startsWith('image/')" class="preview-image">
                  <img :src="file.previewUrl" :alt="file.file.name" />
                </div>
                <div v-else-if="file.type.startsWith('video/')" class="preview-video">
                  <video :src="file.previewUrl" controls />
                </div>
                <div class="preview-file-info">
                  <span class="file-name">{{ file.file.name }}</span>
                  <button 
                    @click="removePreviewFile(index)" 
                    class="remove-preview-file"
                  >
                    ×
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 隐私设置 -->
      <div class="section">
        <label class="section-label">隐私设置</label>
        <div class="privacy-options">
          <label class="radio-option">
            <input
              type="radio"
              v-model="formData.privacy"
              value="public"
            />
            公开
          </label>
          <label class="radio-option">
            <input
              type="radio"
              v-model="formData.privacy"
              value="private"
            />
            私密
          </label>
          <label class="radio-option">
            <input
              type="radio"
              v-model="formData.privacy"
              value="friends"
            />
            仅好友可见
          </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogCreate',
  props: {
    goBack: {
      type: Function,
      required: true
    },
    navigateTo: {
      type: Function,
      required: true
    }
  },
  data() {
    return {
      formData: {
        title: '',
        content: '',
        category: '',
        content_type: 'text', // 默认为文字
        images: [],
        video: null,
        tags: [],
        privacy: 'public'
      },
      tagInput: '',
      uploading: false,
      selectedFiles: [],
      previewFiles: []
    };
  },
  computed: {
    isValid() {
      return (
        this.formData.title.trim() !== '' &&
        this.formData.category !== '' &&
        this.formData.content_type !== '' &&
        (this.formData.content_type === 'text' || 
         this.selectedFiles.length > 0 ||
         (this.formData.content_type === 'mixed' && 
          (this.formData.content.trim() !== '' || this.selectedFiles.length > 0)))
      );
    },
    categories() {
      return [
        { label: '穿搭', value: '穿搭' },
        { label: '美妆', value: '美妆' },
        { label: '护肤', value: '护肤' },
        { label: '配饰', value: '配饰' },
        { label: '鞋包', value: '鞋包' },
        { label: '其他', value: '其他' }
      ];
    },
    contentTypes() {
      return [
        { 
          value: 'text', 
          name: '纯文字', 
          icon: '📝', 
          description: '仅包含文字内容' 
        },
        { 
          value: 'image', 
          name: '图片', 
          icon: '🖼️', 
          description: '包含一张或多张图片' 
        },
        { 
          value: 'video', 
          name: '视频', 
          icon: '🎥', 
          description: '包含一个视频' 
        },
        { 
          value: 'mixed', 
          name: '混合', 
          icon: '✨', 
          description: '文字、图片和视频的组合' 
        }
      ];
    },
    showTextContent() {
      return ['text', 'mixed'].includes(this.formData.content_type);
    },
    showMediaUpload() {
      return ['image', 'video', 'mixed'].includes(this.formData.content_type);
    },
    acceptedFormats() {
      switch (this.formData.content_type) {
        case 'image':
          return 'image/*';
        case 'video':
          return 'video/mp4,video/webm,video/ogg';
        case 'mixed':
          return 'image/*,video/mp4,video/webm,video/ogg';
        default:
          return '*/*';
      }
    },
    hasPreviewContent() {
      return (
        this.formData.title ||
        this.formData.content ||
        this.previewFiles.length > 0 ||
        this.formData.tags.length > 0
      );
    },
    privacyLabels() {
      return {
        public: '公开',
        private: '私密',
        friends: '仅好友可见'
      };
    }
  },
  methods: {
    removePreviewFile(index) {
      // 移除预览文件
      const fileToRemove = this.previewFiles[index];
      this.previewFiles.splice(index, 1);
      this.selectedFiles.splice(this.selectedFiles.findIndex(f => f.previewUrl === fileToRemove.previewUrl), 1);
      
      // 清理URL对象以避免内存泄漏
      if (fileToRemove.previewUrl) {
        URL.revokeObjectURL(fileToRemove.previewUrl);
      }
    },
    
    selectCategory(value) {
      this.formData.category = value;
    },
    
    selectContentType(value) {
      this.formData.content_type = value;
      // 切换类型时清空相关的媒体文件
      if (!['image', 'video', 'mixed'].includes(value)) {
        this.selectedFiles = [];
        this.previewFiles = [];
      }
    },
    
    addTag() {
      const tag = this.tagInput.trim();
      if (tag && !this.formData.tags.includes(tag)) {
        this.formData.tags.push(tag);
        this.tagInput = '';
      }
    },
    
    removeTag(index) {
      this.formData.tags.splice(index, 1);
    },
    
    triggerFileSelect() {
      this.$refs.fileInput.click();
    },
    
    handleDragOver(event) {
      event.preventDefault();
    },
    
    handleFileSelect(event) {
      const files = Array.from(event.target.files);
      this.processFiles(files);
    },
    
    handleDrop(event) {
      const files = Array.from(event.dataTransfer.files);
      this.processFiles(files);
    },
    
    processFiles(files) {
      // 根据内容类型过滤文件
      const validFiles = files.filter(file => {
        if (this.formData.content_type === 'image') {
          return file.type.startsWith('image/');
        } else if (this.formData.content_type === 'video') {
          return file.type.startsWith('video/');
        } else {
          return file.type.startsWith('image/') || file.type.startsWith('video/');
        }
      });

      // 检查数量限制
      if (this.formData.content_type === 'video' && validFiles.length > 1) {
        alert('视频类型只允许上传一个文件');
        return;
      }

      // 检查大小限制
      const maxSize = this.formData.content_type === 'video' ? 500 * 1024 * 1024 : 5 * 1024 * 1024; // 500MB for video, 5MB for others
      const oversizedFiles = validFiles.filter(file => file.size > maxSize);
      if (oversizedFiles.length > 0) {
        alert(`文件过大，请确保图片不超过5MB，视频不超过500MB`);
        return;
      }

      // 添加有效文件
      validFiles.forEach(file => {
        // 创建预览URL
        const previewUrl = URL.createObjectURL(file);
        
        this.selectedFiles.push({
          file: file,
          previewUrl: previewUrl,
          type: file.type
        });
        
        this.previewFiles.push({
          file: file,
          previewUrl: previewUrl,
          type: file.type
        });
      });
    },

    async submitBlog() {
      if (!this.isValid) {
        alert('请填写必填字段');
        return;
      }

      this.uploading = true;

      // 模拟上传过程
      setTimeout(() => {
        // 构建博客数据
        const blogData = {
          title: this.formData.title,
          content: this.formData.content,
          category: this.formData.category,
          content_type: this.formData.content_type,
          tags: this.formData.tags,
          privacy: this.formData.privacy
        };

        // 如果有上传的文件，添加到数据中
        if (this.selectedFiles.length > 0) {
          if (this.formData.content_type === 'image') {
            blogData.images = this.selectedFiles.map((file, index) => ({
              url: file.previewUrl,
              name: file.file.name,
              index: index  // 使用index值
            }));
          } else if (this.formData.content_type === 'video') {
            blogData.video = {
              url: this.selectedFiles[0].previewUrl,
              name: this.selectedFiles[0].file.name
            };
          } else if (this.formData.content_type === 'mixed') {
            blogData.images = this.selectedFiles
              .filter(file => file.type.startsWith('image/'))
              .map((file, index) => ({
                url: file.previewUrl,
                name: file.file.name,
                index: index  // 使用index值
              }));

            const videoFile = this.selectedFiles.find(file => file.type.startsWith('video/'));
            if (videoFile) {
              blogData.video = {
                url: videoFile.previewUrl,
                name: videoFile.file.name
              };
            }
          }
        }

        // 通过事件通知父组件创建成功
        this.$emit('blog-created', blogData);

        this.uploading = false;
      }, 1000);
    },

    getContentTypeName(type) {
      const typeMap = {
        text: '纯文字',
        image: '图片',
        video: '视频',
        mixed: '混合'
      };
      return typeMap[type] || type;
    }
  },

  beforeUnmount() {
    // 清理预览URL对象以避免内存泄漏
    this.previewFiles.forEach(file => {
      if (file.previewUrl) {
        URL.revokeObjectURL(file.previewUrl);
      }
    });
  }
};
</script>

<style scoped>
.blog-create {
  min-height: 100vh;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  color: #fff;
  padding: 20px;
  box-sizing: border-box;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.05);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  margin-bottom: 20px;
}

.nav-left,
.nav-right {
  flex: 1;
}

.nav-center {
  flex: 2;
  text-align: center;
}

.nav-link {
  color: rgba(255, 255, 255, 0.95); /* 提高亮度，原来是 0.8 */
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: color 0.3s ease;
  text-decoration: none; /* 明确去除下划线 */
}

.nav-link:hover {
  color: #ff94d2;
  text-decoration: none; /* 确保悬停时也没有下划线 */
}

.nav-icon {
  font-size: 1.2rem;
}

.publish-btn {
  background: linear-gradient(45deg, #ff1493, #ff69b4); /* 使用更鲜艳亮眼的深粉色到亮粉色渐变 */
  color: white;
  border: 2px solid #ffffff33; /* 添加白色边框增加对比度 */
  padding: 0.75rem 1.5rem;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 1rem;
  letter-spacing: 0.5px;
  box-shadow: 0 6px 20px rgba(255, 20, 147, 0.5); /* 更强烈的阴影效果 */
  text-transform: uppercase;
  animation: pulse 2s infinite; /* 添加轻微脉冲动画吸引注意 */
}

@keyframes pulse {
  0% {
    box-shadow: 0 6px 20px rgba(255, 20, 147, 0.5);
  }
  50% {
    box-shadow: 0 6px 25px rgba(255, 20, 147, 0.7);
  }
  100% {
    box-shadow: 0 6px 20px rgba(255, 20, 147, 0.5);
  }
}

.publish-btn:disabled {
  background: rgba(255, 255, 255, 0.1);
  cursor: not-allowed;
  color: rgba(255, 255, 255, 0.5);
}

.publish-btn:not(:disabled):hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(255, 20, 147, 0.8); /* 悬停时更强的阴影 */
  background: linear-gradient(45deg, #ff69b4, #ff8ac8); /* 悬停时颜色变化 */
  animation: none; /* 悬停时停止脉冲动画 */
}

.create-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
}

.section {
  background: rgba(255, 255, 255, 0.05);
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}

.section-label {
  display: block;
  margin-bottom: 0.75rem;
  font-weight: bold;
  color: #fff;
  font-size: 1.1rem;
}

.category-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 0.75rem;
}

.category-item {
  padding: 0.75rem;
  border: 2px solid #d8bfd8; /* 淡紫色边框 */
  background-color: #f5f5ff; /* 浅紫色背景 */
  border-radius: 4px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  color: #5a3e6b; /* 深紫色字体 */
}

.category-item:hover {
  border-color: #9370DB; /* 悬停时使用更明显的紫色 */
  background-color: #e6e6fa; /* 悬停时背景变深一点 */
  color: #4b0082; /* 悬停时字体颜色加深 */
}

.category-item.active {
  background-color: #9370DB; /* 激活状态使用紫色 */
  color: white;
  border-color: #9370DB;
}

.tag-input-container {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.tag-input {
  flex: 1;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  color: #fff;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.tag-input:focus {
  outline: none;
  border-color: #ff94d2;
  box-shadow: 0 0 0 3px rgba(255, 148, 210, 0.3);
}

.add-tag-btn {
  padding: 0.75rem 1.25rem;
  background: linear-gradient(45deg, #ff94d2, #b388eb);
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.add-tag-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(255, 148, 210, 0.4);
}

.tags-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 0.75rem;
}

.tag-item {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background: rgba(255, 148, 210, 0.2);
  color: #ff94d2;
  border-radius: 20px;
  font-size: 0.875rem;
  border: 1px solid rgba(255, 148, 210, 0.3);
}

.remove-tag {
  background: none;
  border: none;
  color: #ff94d2;
  margin-left: 0.5rem;
  cursor: pointer;
  font-size: 1.2rem;
  line-height: 1;
  font-weight: bold;
  transition: all 0.3s ease;
}

.remove-tag:hover {
  color: #ff6b6b;
  transform: scale(1.2);
}

.content-type-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.25rem;
}

.content-type-item {
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 1.25rem;
  cursor: pointer;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.05);
}

.content-type-item:hover {
  border-color: #ff94d2;
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(255, 148, 210, 0.2);
}

.content-type-item.active {
  border-color: #ff94d2;
  background: rgba(255, 148, 210, 0.1);
}

.content-type-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.content-type-icon {
  font-size: 1.75rem;
}

.content-type-name {
  font-weight: bold;
  color: #fff;
  font-size: 1.1rem;
}

.content-type-desc {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
  margin: 0;
}

.title-input {
  width: 100%;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  color: #fff;
  font-size: 1rem;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
}

.title-input:focus {
  outline: none;
  border-color: #ff94d2;
  box-shadow: 0 0 0 3px rgba(255, 148, 210, 0.3);
}

.content-textarea {
  width: 100%;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  min-height: 150px;
  resize: vertical;
  font-size: 1rem;
  color: #fff;
  transition: all 0.3s ease;
}

.content-textarea:focus {
  outline: none;
  border-color: #ff94d2;
  box-shadow: 0 0 0 3px rgba(255, 148, 210, 0.3);
}

.upload-area {
  border: 2px dashed rgba(255, 255, 255, 0.3);
  border-radius: 12px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.03);
}

.upload-area:hover {
  border-color: #ff94d2;
  background: rgba(255, 148, 210, 0.05);
}

.upload-content {
  padding: 2.5rem;
}

.upload-icon {
  font-size: 3.5rem;
  margin-bottom: 1rem;
  color: rgba(255, 255, 255, 0.7);
}

.upload-text {
  font-size: 1.2rem;
  margin: 0 0 0.75rem 0;
  color: rgba(255, 255, 255, 0.9);
}

.upload-hint {
  color: rgba(255, 255, 255, 0.6);
  margin: 0;
  font-size: 0.9rem;
}

.preview-section {
  padding: 1.25rem;
  background: rgba(255, 255, 255, 0.05);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  text-align: left;
  border-radius: 0 0 10px 10px;
  margin-top: 1rem;
}

.preview-section h3 {
  margin: 0 0 1.25rem 0;
  color: #fff;
  font-size: 1.2rem;
}

.preview-title {
  font-size: 1.25rem;
  font-weight: bold;
  margin-bottom: 0.75rem;
  color: #fff;
}

.preview-content {
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.6;
  margin-bottom: 1.25rem;
}

.preview-tags {
  margin-bottom: 1.25rem;
}

.preview-tag {
  display: inline-block;
  padding: 0.4rem 0.8rem;
  background: rgba(255, 148, 210, 0.2);
  color: #ff94d2;
  border-radius: 20px;
  font-size: 0.875rem;
  margin-right: 0.75rem;
  margin-bottom: 0.5rem;
  border: 1px solid rgba(255, 148, 210, 0.3);
}

.preview-files {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.25rem;
}

.preview-file {
  position: relative;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.preview-image img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  display: block;
}

.preview-video {
  width: 100%;
  text-align: center;
  background: #000;
}

.preview-video video {
  width: 100%;
  height: 150px;
  display: block;
}

.preview-file-info {
  padding: 0.75rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.file-name {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.9);
  word-break: break-all;
  flex: 1;
  margin-right: 0.75rem;
}

.remove-preview-file {
  background: none;
  border: none;
  font-size: 1.4rem;
  cursor: pointer;
  color: #ff6b6b;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.3s ease;
}

.remove-preview-file:hover {
  background: rgba(255, 107, 107, 0.2);
  transform: scale(1.1);
}

.privacy-options {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.radio-option {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  transition: all 0.3s ease;
}

.radio-option:hover {
  background: rgba(255, 148, 210, 0.1);
}

.error-message {
  color: #ff69b4; /* 粉色 */
  font-size: 0.875rem;
  margin-top: 0.5rem;
}
</style>