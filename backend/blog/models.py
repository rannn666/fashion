from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BlogPost(models.Model):
    """博客文章模型"""
    CONTENT_TYPES = (
        ('text', '文字'),
        ('video', '视频'),
        ('image', '图片'),
        ('mixed', '混合内容'),
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES, default='text')
    
    # 文件上传字段
    video_file = models.FileField(upload_to='blog_videos/', blank=True, null=True)
    image_files = models.ManyToManyField('MediaFile', blank=True, related_name='blog_images')
    
    # 其他字段
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['author', '-created_at']),
        ]
    
    def __str__(self):
        return self.title
    
    @property
    def likes_count(self):
        return self.likes.count()
    
    @property
    def comments_count(self):
        return self.comments.count()

class Comment(models.Model):
    """评论模型"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['post', 'created_at']),
        ]
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

class MediaFile(models.Model):
    """媒体文件模型"""
    FILE_TYPES = (
        ('image', '图片'),
        ('video', '视频'),
        ('document', '文档'),
    )
    
    file = models.FileField(upload_to='blog_media/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_media')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.file.name} ({self.file_type})"

class UserProfile(models.Model):
    """用户资料扩展模型"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
