import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Speciality(models.Model):
    name = models.CharField(max_length=100, verbose_name='Especialidade')
    icon = models.ImageField(upload_to="icones", null=True, blank=True, verbose_name='Ícone')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

class MedicalData(models.Model):
    CHOICES = (
        ('masc', 'Masculino'),
        ('fem', 'Feminino'),
        ('nb', 'Não Binário'),
        ('none', 'Prefiro não informar'),
    )

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    gender = models.CharField(max_length=10, choices=CHOICES, default='none', verbose_name='Gênero')
    speciality = models.ForeignKey(Speciality, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Especialidade')
    name = models.CharField(max_length=100, verbose_name='Nome Completo')
    profile_pic = models.ImageField(upload_to="profile_pic/", verbose_name='Foto de Perfil')
    street = models.CharField(max_length=100, verbose_name='Rua')
    district = models.CharField(max_length=100, verbose_name='Bairro')
    number = models.IntegerField(verbose_name='Número')
    crm = models.CharField(max_length=30, verbose_name='CRM')
    cep = models.CharField(max_length=15, verbose_name='CEP')
    rg = models.ImageField(upload_to=".rg/", verbose_name='RG')
    cim = models.ImageField(upload_to='.cim/', verbose_name='Cedula Identidade Médica')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    consult_price = models.DecimalField(max_digits=10, decimal_places=2, default=100, verbose_name='Valor da Consulta')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Medical Data'
        verbose_name_plural = 'Medical Data'
        ordering = ['-pk']

    @property
    def next_date(self):
        next_date = OpenDates.objects.filter(doctor__user=self.user).filter(date__gt=timezone.now()).filter(status=False).order_by('date').first()
        if next_date:
            next_date = next_date.date.strftime("%d/%m/%y %H:%M")
        return next_date

class OpenDates(models.Model):
    date = models.DateTimeField(verbose_name="Data e Horário")
    doctor = models.ForeignKey(MedicalData, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.doctor} - {self.date.date()}'

    class Meta:
        verbose_name = 'Open Dates'
        verbose_name_plural = 'Open Dates'
        ordering = ['date']

class Appointment(models.Model):
    CHOICES = (
        ('A', 'Agendada'),
        ('F', 'Finalizada'),
        ('C', 'Cancelada'),
        ('I', 'Iniciada')
    )

    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    open_date = models.ForeignKey(OpenDates, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=CHOICES, default='A')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.patient.get_full_name()} ({self.patient.username}) - {self.open_date.doctor.name}' 
    
    class Meta:
        ordering = ['open_date__date'] 

class Document(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING, verbose_name='Consulta')
    title = models.CharField(max_length=30, verbose_name='Título')
    document = models.FileField(upload_to='.documents/', verbose_name='Documento')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pk']