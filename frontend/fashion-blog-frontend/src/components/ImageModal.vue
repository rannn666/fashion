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
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.modal-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.image-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.modal-image {
  max-width: 80vw;
  max-height: 80vh;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  color: rgba(255, 255, 255, 0.8);
  font-size: 1.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  transform: scale(1.1);
}

.nav-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 60px;
  height: 60px;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  color: rgba(255, 255, 255, 0.8);
  font-size: 1.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.nav-button:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  transform: translateY(-50%) scale(1.1);
}

.prev-btn {
  left: 20px;
}

.next-btn {
  right: 20px;
}

.caption {
  margin-top: 15px;
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
  font-size: 1rem;
  max-width: 80vw;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.image-counter {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background: rgba(0, 0, 0, 0.5);
  color: rgba(255, 255, 255, 0.8);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

@media (max-width: 768px) {
  .modal-overlay {
    background: rgba(0, 0, 0, 0.95);
  }
  
  .modal-image {
    max-width: 95vw;
    max-height: 70vh;
  }
  
  .close-btn {
    top: 15px;
    right: 15px;
    width: 40px;
    height: 40px;
    font-size: 1.2rem;
  }
  
  .nav-button {
    width: 50px;
    height: 50px;
    font-size: 1.2rem;
  }
  
  .caption {
    font-size: 0.9rem;
  }
  
  .image-counter {
    font-size: 0.8rem;
    padding: 6px 12px;
  }
}
</style>