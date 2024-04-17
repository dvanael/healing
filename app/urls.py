from django.urls import path
from .views import register, index, medic_register

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('cadastro-medico/', medic_register, name='medic-register'),
]
