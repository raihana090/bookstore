from django.urls import path
from . import views

urlpatterns=[

    path('register/',views.Register_user,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logOut,name='logout'),
    path('home/',views.HomePage,name='home')


]