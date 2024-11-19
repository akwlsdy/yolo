from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  # 文章标题，最大长度为 100
    text = models.TextField()  # 文章内容
    created_date = models.DateTimeField(auto_now_add=True)  # 创建日期，自动设置为当前时间
    published_date = models.DateTimeField(auto_now=True)  # 发布时间，自动设置为当前时间，每次更新时都会自动修改
    image = models.ImageField(upload_to='posts/', null=True, blank=True)  # 图片字段，允许为空，用于存储文章的图片，保存在 'posts/' 目录中

    def __str__(self):
        return self.title  # 返回文章标题作为模型的表示

    class Meta:
        ordering = ['-created_date']  # 按照创建日期降序排列（最新的文章排在最前面）
