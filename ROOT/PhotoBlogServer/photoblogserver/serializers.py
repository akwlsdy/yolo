from rest_framework import serializers
from .models import Post
from django.conf import settings

class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()  # 添加一个用于返回图片完整 URL 的字段

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'created_date', 'published_date', 'image', 'image_url']  # 包括新的 image_url 字段

    def get_image_url(self, obj):
        """返回图片的完整 URL"""
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None  # 如果没有图片，则返回 None

    def validate_image(self, value):
        """图片字段的验证函数，可根据需要扩展"""
        # 这里可以添加图片大小限制，格式验证等
        if value.size > 5 * 1024 * 1024:  # 限制图片大小为 5MB
            raise serializers.ValidationError("图片大小不能超过 5MB")
        return value
