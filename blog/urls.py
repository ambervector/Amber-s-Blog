from django.urls import path

from . import views

urlpatterns = [
    path("", views.blogpage, name="blog-home-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="single-post-page")
]
