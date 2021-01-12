from django.urls import path
from .views import (
    PostListView, 
    TagListView, 
    PostDetailView, 
    TagDetailView, 
    PostCreateView, 
    TagCreateView)


urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:post_id>/', PostDetailView.as_view()),
    path('tags/', TagListView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('tag/create/', TagCreateView.as_view()),
    path('tags/<int:tag_id>/', TagDetailView.as_view())
]