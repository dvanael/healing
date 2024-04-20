from .models import MedicalData
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants


# Crie suas funcões aqui
def is_medic(user):
    return MedicalData.objects.filter(user=user).exists()

def secure_redirect(request):
    messages.add_message(request, constants.WARNING, "Você não pode acessar essa página")
    return redirect('index')
