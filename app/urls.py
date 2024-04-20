from django.urls import path
from .views import register, index, medic_register, login_view, logout_view, create_date, delete_date, view_date, create_appointment, appointment_list, medic_appointment_list, detail_appointment, medic_detail_appointment, close_appointment, create_document

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Médico
    path('cadastro/medico/', medic_register, name='medic-register'),
    path('cadastrar/horario/', create_date, name='open-date'),
    path('deletar/<int:pk>/horario/', delete_date, name='delete-date'),
    path('consultas/agendadas/', medic_appointment_list, name='medic-appointment-list'),
    path('consulta/<int:pk>/agendada/', medic_detail_appointment, name='medic-detail-appointment'),
    path('consulta/<int:pk>/finalizar/', close_appointment, name='close-appointment'),
    path('consulta/<int:pk>/documento/', create_document, name='create-document'),
    # Paciente
    path('escolher-horario/<int:pk>/', view_date, name='choose-time'),
    path('agendar-consulta/<int:pk>/', create_appointment, name='create-appointment'),
    path('consulta/<int:pk>/', detail_appointment, name='detail-appointment'),
    path('minhas-consultas/', appointment_list, name='appointment-list'),

]
