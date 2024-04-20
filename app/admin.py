from django.contrib import admin
from .models import Speciality, MedicalData, OpenDates, Appointment, Document

# Register your models here.
admin.site.register(Speciality)
admin.site.register(MedicalData)
admin.site.register(OpenDates)
admin.site.register(Appointment)
admin.site.register(Document)