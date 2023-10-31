from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('chamber/<str:pk>/', views.chamber, name='chamber'),
]