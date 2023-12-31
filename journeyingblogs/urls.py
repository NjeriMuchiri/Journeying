from django.urls import path
from . import views

#uniform resource locators for routing through our pages
urlpatterns = [
    path('login/', views.ourLoginPage, name="loginpage"),
    path('logout/', views.logoutUser, name="logoutuser"),
    path('register/', views.registerPage, name="register"),


    path('', views.home, name='homepage'),
    path('chamber/<str:pk>/', views.chamber, name='chamber'),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
    path('create-chamber/', views.createChamber, name="create-chamber"),
    path('update-chamber/<str:pk>/', views.updateChamber, name="update-chamber"),
    path('delete-chamber/<str:pk>/', views.deleteChamber, name="delete-chamber"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topic/', views.topicPage, name="topic_page"),
    path('blogreaction/', views.ReactionPage, name="blog_reaction"),
    ]