from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, CommentViewSet, MediaFileViewSet, UserProfileViewSet

# 创建路由器并注册ViewSet
router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='blogpost')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'media', MediaFileViewSet, basename='mediafile')
router.register(r'profiles', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('api/', include(router.urls)),
]