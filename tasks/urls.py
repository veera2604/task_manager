from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_task/', views.add_task, name='add_task'),
    path('my_task/', views.my_task, name='my_task'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('', views.index, name='index'),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
]
