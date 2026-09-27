
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newPost", views.newPost, name="newPost"),
    path("profile/<int:profile_id>", views.profile, name="profile"),
    path("followProfile/<int:profile_id>", views.followProfile, name="followProfile"),
    path("likePost/<int:post_id>", views.likePost, name="likePost"),
    path("editPost/<int:post_id>", views.editPost, name="editPost"),
    path("followingPost", views.followingPost, name="followingPost"),
]
