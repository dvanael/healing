from .models import DadosMedico

# Crie suas funcões aqui
def is_medic(user):
    return DadosMedico.objects.filter(user=user).exists()