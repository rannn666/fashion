<template>
  <div class="comment-item" :class="{ 'has-replies': comment.replies && comment.replies.length > 0 }">
    <!-- 主评论 -->
    <div class="comment-main">
      <div class="comment-avatar">{{ comment.author.username.charAt(0).toUpperCase() }}</div>
      <div class="comment-content">
        <div class="comment-header">
          <h4 class="comment-author">{{ comment.author.username }}</h4>
          <span class="comment-date">{{ formatDate(comment.created_at) }}</span>
        </div>
        <p class="comment-text">{{ comment.content }}</p>
        <div class="comment-actions">
          <button 
            @click="toggleReplyForm" 
            class="reply-btn"
            :class="{ active: showReplyForm }"
          >
            💬 回复
          </button>
        </div>
      </div>
    </div>

    <!-- 回复表单 -->
    <div v-if="showReplyForm" class="reply-form">
      <textarea 
        v-model="replyContent"
        @keydown.ctrl.enter="submitReply"
        placeholder="写下你的回复... (Ctrl+Enter 发送)"
        class="reply-input"
        rows="2"
      ></textarea>
      <div class="reply-actions">
        <button @click="cancelReply" class="cancel-btn">取消</button>
        <button @click="submitReply" :disabled="!replyContent.trim()" class="submit-reply-btn">
          回复
        </button>
      </div>
    </div>

    <!-- 子评论 -->
    <div v-if="comment.replies && comment.replies.length > 0" class="replies">
      <CommentItem 
        v-for="reply in comment.replies" 
        :key="reply.id"
        :comment="reply"
        :is-reply="true"
        @reply="$emit('reply', $event)"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CommentItem',
  props: {
    comment: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      localComment: { ...this.comment },
      showReplyForm: false,
      replyContent: ''
    };
  },
  watch: {
    comment: {
      handler(newComment) {
        this.localComment = { ...newComment };
      },
      deep: true
    }
  },
  computed: {
    isReply() {
      return !!this.comment.parent;
    }
  },
  methods: {
    toggleReplyForm() {
      this.showReplyForm = !this.showReplyForm;
      if (!this.showReplyForm) {
        this.replyContent = '';
      }
    },

    cancelReply() {
      this.showReplyForm = false;
      this.replyContent = '';
    },

    async submitReply() {
      if (!this.replyContent.trim()) return;
      
      try {
        const response = await axios.post('/api/comments/', {
          post: this.comment.post,
          content: this.replyContent,
          parent: this.comment.id
        });
        
        // 将新回复添加到评论的replies数组中
        if (!this.localComment.replies) {
          this.localComment.replies = [];
        }
        this.localComment.replies.push(response.data);
        
        this.replyContent = '';
        this.showReplyForm = false;
        this.$emit('reply', response.data);
        this.$toast?.success('回复发表成功');
      } catch (error) {
        console.error('发表回复失败:', error);
        this.$toast?.error('发表回复失败，请登录后再试');
      }
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
    }
  }
};
</script>

<style scoped>
.comment {
  display: flex;
  gap: 15px;
  padding: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  transition: all 0.3s ease;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment:hover {
  background: rgba(255, 255, 255, 0.05);
  transform: translateY(-2px);
}

.comment:last-child {
  border-bottom: none;
}

.comment-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(45deg, #ff69b4, #ff1493);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: white;
  flex-shrink: 0;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-content {
  flex: 1;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-author {
  font-weight: bold;
  color: #ff94d2;
  font-size: 1rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-date {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.6);
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-text {
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.6;
  margin-bottom: 12px;
  font-size: 0.9rem;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.comment-actions {
  display: flex;
  gap: 15px;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  padding: 6px 12px;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  font-family: 'Poppins', 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

.action-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #ff94d2;
}

.reply-btn {
  color: rgba(161, 138, 255, 0.8);
}

.reply-btn:hover {
  color: #a18aff;
}

.delete-btn {
  color: rgba(255, 107, 107, 0.8);
}

.delete-btn:hover {
  color: #ff6b6b;
}

.replies {
  margin-top: 15px;
  padding-left: 30px;
  border-left: 2px solid rgba(255, 255, 255, 0.1);
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
}

@media (max-width: 768px) {
  .comment {
    gap: 12px;
    padding: 15px;
  }
  
  .comment-avatar {
    width: 40px;
    height: 40px;
    font-size: 0.9rem;
  }
  
  .comment-author {
    font-size: 0.9rem;
  }
  
  .comment-date {
    font-size: 0.8rem;
  }
  
  .comment-text {
    font-size: 0.85rem;
  }
  
  .action-btn {
    font-size: 0.8rem;
    padding: 4px 8px;
  }
  
  .replies {
    padding-left: 20px;
  }
}
</style>