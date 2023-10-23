
from django.urls import path

from . import views

urlpatterns = [
    path('toto/', views.toto, name="toto"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
]
