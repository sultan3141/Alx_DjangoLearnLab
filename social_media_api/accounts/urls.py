from django.urls import path
from django.views.generic import RedirectView
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView

urlpatterns = [
    path("", RedirectView.as_view(url="login/", permanent=False)),  # 👈 redirect /accounts/ → /accounts/login/
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"), 
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
]

