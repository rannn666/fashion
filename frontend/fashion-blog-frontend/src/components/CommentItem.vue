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
.comment-item {
  padding: 20px;
  border-bottom: 1px solid #333;
  position: relative;
}

.comment-item:last-child {
  border-bottom: none;
}

.comment-item.has-replies {
  border-left: 3px solid #ff69b4;
  margin-left: 20px;
  padding-left: 17px;
}

.comment-main {
  display: flex;
  gap: 15px;
}

.comment-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(45deg, #ff69b4, #ff1493);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: bold;
  flex-shrink: 0;
}

.comment-content {
  flex: 1;
}

.comment-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.comment-author {
  margin: 0;
  font-size: 1rem;
  color: #fff;
  font-weight: 600;
}

.comment-date {
  color: #888;
  font-size: 0.85rem;
}

.comment-text {
  color: #ccc;
  line-height: 1.6;
  margin-bottom: 12px;
}

.comment-actions {
  display: flex;
  gap: 10px;
}

.reply-btn {
  background: none;
  border: none;
  color: #ff94d2;
  cursor: pointer;
  font-size: 0.9rem;
  transition: color 0.3s;
}

.reply-btn:hover, .reply-btn.active {
  color: #b388eb;
}

.reply-form {
  margin-top: 15px;
  margin-left: 55px;
  background: transparent;
  padding: 15px;
  border-radius: 10px;
  border: 1px solid rgba(74, 60, 92, 0.3);
}

.reply-input {
  width: 100%;
  padding: 10px;
  border: 1px solid rgba(74, 60, 92, 0.3);
  border-radius: 8px;
  background: transparent;
  color: #fff;
  font-size: 0.9rem;
  line-height: 1.4;
  resize: vertical;
  margin-bottom: 10px;
}

.reply-input:focus {
  outline: none;
  border-color: #ff94d2;
}

.reply-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.cancel-btn {
  padding: 6px 12px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 15px;
  background: transparent;
  color: #fff;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.3s;
}

.cancel-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
}

.submit-reply-btn {
  padding: 6px 12px;
  border: 1px solid rgba(74, 60, 92, 0.3);
  border-radius: 15px;
  background: linear-gradient(45deg, #c67bb4, #8b76b8);
  color: #fff;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.3s;
}

.submit-reply-btn:hover:not(:disabled) {
  transform: translateY(-2px);
}

.submit-reply-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.replies {
  margin-top: 15px;
  margin-left: 55px;
  border-left: 2px solid rgba(255, 255, 255, 0.3);
  padding-left: 20px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .comment-main {
    gap: 10px;
  }
  
  .comment-avatar {
    width: 35px;
    height: 35px;
  }
  
  .reply-form {
    margin-left: 45px;
    padding: 12px;
  }
  
  .replies {
    margin-left: 45px;
    padding-left: 15px;
  }
}
</style>