from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('chamber/<str:pk>/', views.chamber, name='chamber'),
    path('create-chamber/', views.createChamber, name="create-chamber"),
    path('update-chamber/<str:pk>/', views.updateChamber, name="update-chamber"),

]