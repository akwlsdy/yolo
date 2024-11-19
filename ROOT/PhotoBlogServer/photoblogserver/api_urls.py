from django.urls import path
from . import views

urlpatterns = [
    path('Post/', views.PostListCreateView.as_view(), name='post-list-create'),
]
