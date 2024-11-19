from django.contrib import admin
from .models import Post  # 假设有一个 Post 模型

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')  # 自定义显示字段
