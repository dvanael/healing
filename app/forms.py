from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import MedicalData

# Cadastro Usuario Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        labels = {
            'username': 'Nome de Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
        }

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email = e).exists():
            raise ValidationError(f"O email {e} já está em uso.") 
        return e
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        username =  self.fields['username']
        email = self.fields['email']
        first_name =  self.fields['first_name']
        last_name =  self.fields['last_name']
        password1 = self.fields['password1']
        password2 = self.fields['password2']

        first_name.widget.attrs={'placeholder': 'Digite seu Primeiro Nome'}
        last_name.widget.attrs={'placeholder': 'Digite seu Sobrenome'}

        username.widget.attrs={'placeholder': 'Digite um nome de usuário'}
        username.help_text = ''
        
        email.widget.attrs={'placeholder': 'Digite seu email'}
        email.help_text = ''
        
        password1.widget.attrs={'placeholder': 'Digite sua senha'}
        password1.help_text = ''

        password2.widget.attrs={'placeholder': 'Confirme sua senha'}
        password2.help_text = ''

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de Usuário')
    class Meta:
        model = User
        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        username =  self.fields['username']
        password = self.fields['password']
        username.widget.attrs={'placeholder': 'Digite seu nome de usuário'}
        password.widget.attrs={'placeholder': 'Digite sua senha'}



class MedicRegisterForm(forms.ModelForm):
    class Meta:
        model = MedicalData
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['placeholder'] = 'Nome Completo . . .'
        self.fields['street'].widget.attrs['placeholder'] = 'Endereço . . .'
        self.fields['district'].widget.attrs['placeholder'] = 'Bairro . . .'
        self.fields['number'].widget.attrs['placeholder'] = 'Número . . .'
        self.fields['crm'].widget.attrs['placeholder'] = 'Seu CRM . . .'
        self.fields['cep'].widget.attrs['placeholder'] = 'Seu CEP . . .'
        self.fields['description'].widget.attrs['placeholder'] = 'Descreva sua vocação . . .'
