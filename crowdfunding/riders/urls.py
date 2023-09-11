from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('riders/', views.RiderList.as_view()),
    path('rider/<int:pk>/', views.RiderDetail.as_view()),
    path('updates/', views.RiderUpdatesList.as_view()),
    path('rider/<int:pk>/updates/', views.RiderUpdatesList.as_view()),
    path('donations/', views.DonationList.as_view()),
    path('donation/<int:pk>', views.DonationList.as_view()),
]

urlpatters = format_suffix_patterns(urlpatterns)