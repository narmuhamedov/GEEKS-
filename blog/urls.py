from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.message, name='message'),
    path('emodji/', views.emodji, name='emodji'),
]