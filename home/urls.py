from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout')
]
