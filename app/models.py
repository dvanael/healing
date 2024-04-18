from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    speciality = models.ForeignKey(Speciality, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Especialidade')
    name = models.CharField(max_length=100, verbose_name='Nome')
    profile_pic = models.ImageField(upload_to="profile_pic", verbose_name='Foto de Perfil')
    street = models.CharField(max_length=100, verbose_name='Rua')
    district = models.CharField(max_length=100, verbose_name='Bairro')
    number = models.IntegerField(verbose_name='Número')
    crm = models.CharField(max_length=30, verbose_name='CRM')
    cep = models.CharField(max_length=15, verbose_name='CEP')
    rg = models.ImageField(upload_to="rg", verbose_name='RG')
    cim = models.ImageField(upload_to='cim', verbose_name='Cedula Identidade Médica')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    consult_price = models.FloatField(default=100, verbose_name='Valor da Consulta')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Medical Data'
        verbose_name_plural = 'Medical Data'