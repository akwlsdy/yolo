from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理后台路径
    path('api_root/', include('photoblogserver.urls')),  # 将路由转发给 photoblogserver app
]
