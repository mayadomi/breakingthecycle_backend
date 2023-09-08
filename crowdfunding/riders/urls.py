from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('riders/', views.RiderList.as_view()),
    path('riders/<int:pk>/', views.RiderDetail.as_view()),
    path('donations/', views.DonationList.as_view()),
    path('donations/<int:pk>', views.DonationDeletionView.as_view()),
    path('updates/', views.RiderUpdatesList.as_view()),
    path('riders/<int:pk>/updates/', views.RiderUpdatesList.as_view())
]

urlpatters = format_suffix_patterns(urlpatterns)