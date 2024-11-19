from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    """
    视图类：处理 POST 请求来创建博客文章，处理 GET 请求来获取博客文章列表。
    """
    queryset = Post.objects.all()  # 获取所有博客文章
    serializer_class = PostSerializer  # 使用 PostSerializer 进行序列化

    def perform_create(self, serializer):
        """
        在创建新的 Post 时调用，确保可以处理请求并保存数据。
        """
        serializer.save()  # 调用 save 方法保存新创建的 Post 实例

# 配置 URL 路由来让这个视图可访问
from django.urls import path

# 在你的应用的 urls.py 文件中添加以下路由配置
urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
]
