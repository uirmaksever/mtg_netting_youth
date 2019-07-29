from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('users/new', views.create_profile, name="profile-create"),
    path('users/<int:pk>/followed_problems', views.FollowedProblemList.as_view(), name="user-problems-list"),
    path('problem/', views.ProblemList.as_view(), name="problem-list"),
    path('problem/<int:pk>', views.ProblemDetail.as_view(), name="problem-detail"),
    path('problem/<int:pk>/up', views.problem_vote_up, name="problem-vote-up")

]
