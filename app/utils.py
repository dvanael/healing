from .models import MedicalData

# Crie suas funcões aqui
def is_medic(user):
    return MedicalData.objects.filter(user=user).exists()