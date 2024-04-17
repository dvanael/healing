from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import DadosMedico

# Cadastro Usuario Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email = e).exists():
            raise ValidationError(f"O email {e} já está em uso.") 
        return e

class MedicRegisterForm(forms.ModelForm):
    class Meta:
        model = DadosMedico
        fields = ('crm', 'nome', 'cep', 'rua', 'bairro', 'numero', 'rg', 'cedula_identidade_medica', 'foto', 'descricao', 'especialidade', 'valor_consulta',)
