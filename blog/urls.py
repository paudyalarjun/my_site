from . import views
from django.urls import path

urlpatterns = [
    path('', views.starting_page, name="starting-page"),
    path('posts/', views.posts, name="posts-page"),
    path('posts/<slug:slug>', views.posts_detail, name="post-detail-page")
]