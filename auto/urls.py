from django.urls import path
from . import views

app_name = 'auto'

urlpatterns = [
    path('cars/', views.auto_view, name='auto'),
]