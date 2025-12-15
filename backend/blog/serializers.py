from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost, Comment, MediaFile, UserProfile

class UserSerializer(serializers.ModelSerializer):
    """用户序列化器"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    """用户资料序列化器"""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'avatar', 'bio', 'website', 'location']
        read_only_fields = ['user']

class MediaFileSerializer(serializers.ModelSerializer):
    """媒体文件序列化器"""
    uploaded_by = UserSerializer(read_only=True)
    
    class Meta:
        model = MediaFile
        fields = ['id', 'file', 'file_type', 'uploaded_by', 'created_at']
        read_only_fields = ['uploaded_by', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    """评论序列化器"""
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at', 'parent', 'replies']
        read_only_fields = ['author', 'created_at', 'updated_at']
    
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True, context=self.context).data
        return []

class BlogPostSerializer(serializers.ModelSerializer):
    """博客文章序列化器"""
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(source='comments.filter', many=True, read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    image_files = MediaFileSerializer(many=True, read_only=True)
    liked_by_user = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'author', 'title', 'content', 'content_type',
            'video_file', 'image_files', 'created_at', 'updated_at',
            'is_published', 'likes', 'likes_count', 'comments_count',
            'comments', 'liked_by_user'
        ]
        read_only_fields = [
            'author', 'created_at', 'updated_at', 'likes', 
            'likes_count', 'comments_count', 'comments', 'liked_by_user'
        ]
    
    def get_liked_by_user(self, obj):
        user = self.context.get('request').user
        return user.is_authenticated and user in obj.likes.all()
    
    def create(self, validated_data):
        # 处理图片文件
        image_files = self.context.get('request').FILES.getlist('image_files') if 'request' in self.context else []
        media_files = []
        
        for file in image_files:
            media_file = MediaFile.objects.create(
                file=file,
                file_type='image',
                uploaded_by=self.context.get('request').user
            )
            media_files.append(media_file)
        
        # 创建博客文章
        post = BlogPost.objects.create(
            **validated_data
        )
        
        # 关联图片文件
        for media_file in media_files:
            post.image_files.add(media_file)
        
        return post