
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('toogle_dark_mode/', views.toogle_dark_mode, name="toogle_dark_mode"),
    path('brand_models/', views.brand_models, name="brand_models"),
    path('brands/', views.brands, name="brands"),
    path('green_score/', views.green_score, name="green_score"),
    path('toogle_favorite/', views.toogle_favorite, name="toogle_favorite"),
]