from django.contrib import admin
from .models import Speciality, MedicalData, OpenDates

# Register your models here.
admin.site.register(Speciality)
admin.site.register(MedicalData)
admin.site.register(OpenDates)