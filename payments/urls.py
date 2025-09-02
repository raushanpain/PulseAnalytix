from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('history/', views.payment_history, name='payment_history'),
]