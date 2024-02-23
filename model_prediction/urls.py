from django.urls import path
from . import views

urlpatterns = [
    path('diagnose/', views.dashboard, name='prediction-page')
]
