<template>
  <div class="image-modal" @click="closeModal">
    <div class="modal-overlay" @click="closeModal"></div>
    <div class="modal-content" @click.stop>
      <!-- 关闭按钮 -->
      <button @click="close" class="close-btn">×</button>
      
      <!-- 导航按钮 -->
      <button 
        v-if="images.length > 1" 
        @click="previous" 
        class="nav-btn prev"
        :disabled="currentIndex === 0"
      >
        ‹
      </button>
      
      <button 
        v-if="images.length > 1" 
        @click="next" 
        class="nav-btn next"
        :disabled="currentIndex === images.length - 1"
      >
        ›
      </button>
      
      <!-- 主图片 -->
      <div class="image-container">
        <img 
          v-if="currentImage" 
          :src="currentImage.file" 
          :alt="`图片 ${currentIndex + 1}`"
          class="modal-image"
        />
        <div v-else class="loading-image">
          <div class="spinner"></div>
        </div>
      </div>
      
      <!-- 图片信息 -->
      <div v-if="images.length > 1" class="image-info">
        <span class="image-counter">
          {{ currentIndex + 1 }} / {{ images.length }}
        </span>
        
        <!-- 缩略图导航 -->
        <div class="thumbnail-nav">
          <img 
            v-for="(image, index) in images" 
            :key="index"
            :src="image.file" 
            :alt="`缩略图 ${index + 1}`"
            class="thumbnail"
            :class="{ active: index === currentIndex }"
            @click="goToImage(index)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ImageModal',
  props: {
    images: {
      type: Array,
      required: true
    },
    currentIndex: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      index: this.currentIndex
    };
  },
  computed: {
    currentImage() {
      return this.images[this.index];
    }
  },
  watch: {
    currentIndex: {
      handler(newIndex) {
        this.index = newIndex;
      }
    }
  },
  mounted() {
    // 监听键盘事件
    document.addEventListener('keydown', this.handleKeydown);
  },
  beforeUnmount() {
    // 移除键盘事件监听
    document.removeEventListener('keydown', this.handleKeydown);
  },
  methods: {
    close() {
      this.$emit('close');
    },
    
    closeModal(event) {
      if (event.target === event.currentTarget) {
        this.close();
      }
    },
    
    next() {
      if (this.index < this.images.length - 1) {
        this.index++;
        this.$emit('next');
      }
    },
    
    previous() {
      if (this.index > 0) {
        this.index--;
        this.$emit('previous');
      }
    },
    
    goToImage(index) {
      this.index = index;
    },
    
    handleKeydown(event) {
      switch (event.key) {
        case 'Escape':
          this.close();
          break;
        case 'ArrowLeft':
          this.previous();
          break;
        case 'ArrowRight':
          this.next();
          break;
      }
    }
  }
};
</script>

<style scoped>
.image-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.9);
}

.modal-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.close-btn {
  position: absolute;
  top: -50px;
  right: 0;
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  font-size: 24px;
  cursor: pointer;
  transition: all 0.3s;
  z-index: 1001;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
}

.nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 60px;
  height: 60px;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  font-size: 30px;
  cursor: pointer;
  transition: all 0.3s;
  z-index: 1001;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-btn:hover:not(:disabled) {
  background: rgba(255, 105, 180, 0.8);
  transform: translateY(-50%) scale(1.1);
}

.nav-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.nav-btn.prev {
  left: -80px;
}

.nav-btn.next {
  right: -80px;
}

.image-container {
  position: relative;
  max-width: 100%;
  max-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-image {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
  border-radius: 10px;
  box-shadow: 0 10px 50px rgba(0, 0, 0, 0.5);
}

.loading-image {
  width: 100px;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top: 4px solid #ff69b4;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.image-info {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

.image-counter {
  color: #fff;
  font-size: 1rem;
  background: rgba(0, 0, 0, 0.5);
  padding: 5px 15px;
  border-radius: 20px;
}

.thumbnail-nav {
  display: flex;
  gap: 10px;
  max-width: 80vw;
  overflow-x: auto;
  padding: 10px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 10px;
}

.thumbnail {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s;
  border: 2px solid transparent;
  opacity: 0.6;
}

.thumbnail:hover, .thumbnail.active {
  opacity: 1;
  transform: scale(1.1);
  border-color: #ff69b4;
}

@media (max-width: 768px) {
  .nav-btn {
    width: 50px;
    height: 50px;
    font-size: 24px;
  }
  
  .nav-btn.prev {
    left: -60px;
  }
  
  .nav-btn.next {
    right: -60px;
  }
  
  .close-btn {
    top: -40px;
    width: 35px;
    height: 35px;
    font-size: 20px;
  }
  
  .thumbnail {
    width: 50px;
    height: 50px;
  }
  
  .modal-image {
    max-height: 70vh;
  }
}

@media (max-width: 480px) {
  .nav-btn.prev {
    left: 10px;
  }
  
  .nav-btn.next {
    right: 10px;
  }
  
  .thumbnail-nav {
    max-width: 90vw;
  }
}
</style>