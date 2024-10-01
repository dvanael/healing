import os, sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

from app.models import Speciality

specialities = [
    "Dermatologista",
    "Pediatra",
    "Cardiologista",
    "Oftalmologista",
    "Ortopedista",
    "Neurologista",
    "Ginecologista",
    "Psiquiatra",
    "Endocrinologista",
    "Urologista"
]

def create_specialities():
    for speciality_name in specialities:
        speciality, created = Speciality.objects.get_or_create(name=speciality_name)
        if created:
            print(f"Speciality '{speciality_name}' has created.")
        else:
            print(f"Speciality '{speciality_name}' alredy exists.")

if __name__ == "__main__":
    create_specialities()
