from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.ourLoginPage, name="loginpage"),
    path('logout/', views.logoutUser, name="logoutuser"),
    path('register/', views.registerPage, name="register"),


    path('', views.home, name='homepage'),
    path('chamber/<str:pk>/', views.chamber, name='chamber'),
    path('create-chamber/', views.createChamber, name="create-chamber"),
    path('update-chamber/<str:pk>/', views.updateChamber, name="update-chamber"),
    path('delete-chamber/<str:pk>/', views.deleteChamber, name="delete-chamber"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),


]