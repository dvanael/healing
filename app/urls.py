from django.urls import path
from .views import register, index, medic_register, login_view, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('cadastro-medico/', medic_register, name='medic-register'),
]
