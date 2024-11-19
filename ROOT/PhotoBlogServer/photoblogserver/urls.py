from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Make sure this import includes all necessary views

# Correct the home view reference and ensure it exists in views.py
urlpatterns = [
    path('', views.home, name='home'),  # The root URL goes to the home view
    path('admin/', admin.site.urls),
    path('api_root/', include('photoblogserver.api_urls')),
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),  # Ensure this view exists and is correctly imported
]

# Add media file configurations to serve during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
