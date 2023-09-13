from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('user/create/', views.CustomUserCreate.as_view()),
    path('user/<int:pk>/', views.CustomUserDetail.as_view()),
]

