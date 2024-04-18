from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .utils import is_medic
from .forms import UserRegisterForm, MedicRegisterForm, UserLoginForm

from django.contrib.messages import constants
from django.contrib import messages

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}

# Create your views here.
@login_required
def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def register(request):
    template_name = 'registration/register.html'
    context = {}

    if request.method == 'GET':
        form = UserRegisterForm()
        context['form'] = form

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

    return render(request, template_name, context)

def login_view(request):
    template_name = 'registration/login.html'
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form

    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        context['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            
    return render(request, template_name, context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def medic_register(request):
    template_name = 'medic/register.html'
    context = {}
    user = request.user

    if is_medic(user):
        messages.add_message(request, constants.WARNING, "Você já está cadastrado como médico")
        return redirect('index')

    if request.method == 'GET':
        form = MedicRegisterForm()
        context['form'] = form

    if request.method == 'POST':
        form = MedicRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = user
            form.save()

            return redirect('index')

    return render(request, template_name, context)