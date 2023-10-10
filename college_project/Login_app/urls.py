from django.urls import path
from . import views
app_name='Login_app'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form',views.form,name='form'),
    ]