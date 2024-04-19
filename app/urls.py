from django.urls import path
from .views import register, index, medic_register, login_view, logout_view, create_date, delete_date, view_date, create_appointment, appointment_list, medic_appointment_list

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Médico
    path('cadastro-medico/', medic_register, name='medic-register'),
    path('abrir-horario/', create_date, name='open-date'),
    path('deletar-data/<int:pk>/', delete_date, name='delete-date'),
    path('deletar-data/<int:pk>/', delete_date, name='delete-date'),
    path('minhas-consultas-medicas/', medic_appointment_list, name='medic-appointment-list'),
    # Paciente
    path('escolher-horario/<int:pk>/', view_date, name='choose-time'),
    path('agendar-consulta/<int:pk>/', create_appointment, name='create-appointment'),
    path('minhas-consultas/', appointment_list, name='appointment-list'),

]
