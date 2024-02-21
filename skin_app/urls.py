from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('home/', views.dashboard, name='dashboard')

]