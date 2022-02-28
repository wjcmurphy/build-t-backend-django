from django.urls import path
from .views import ClientView, AuthView, RegisterView

urlpatterns = [
    path('clients/', ClientView.as_view(), name='clients_list'),
    path('client/<int:id>', ClientView.as_view(), name='client_process'),
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', AuthView.as_view(), name='login'),
    path('auth/logout', AuthView.as_view(), name='logout'),
]
