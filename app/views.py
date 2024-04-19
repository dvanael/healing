from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .utils import is_medic
from .forms import UserRegisterForm, MedicRegisterForm, UserLoginForm, OpenDateForm
from .models import MedicalData, OpenDates, Speciality, Appointment

from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    template_name = 'index.html'

    doctors = MedicalData.objects.all()
    specialities = Speciality.objects.all()
    
    if request.method == 'GET':
        doctor_filter = request.GET.get('search', '')
        spec_filter = request.GET.getlist('specialities', [])

        if doctor_filter:
            doctors = doctors.filter(name__icontains=doctor_filter)

        if spec_filter:
            doctors = doctors.filter(speciality_id__in=spec_filter)
        if not spec_filter:
            spec_filter = []

    context = {
        'doctors': doctors,
        'specialities': specialities,
        'search': doctor_filter,
        'spec_filter': spec_filter,
    }
    return render(request, template_name, context)

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
                messages.add_message(request, constants.DEBUG, "Sua conta foi criada com sucesso.")
                return redirect('index')

    return render(request, template_name, context)

def login_view(request):
    template_name = 'registration/login.html'
    context = {}

    if request.user.is_authenticated:
        messages.add_message(request, constants.WARNING, "Você não pode acessar essa página")
        return redirect('index')


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
        context['form'] = form
        form.instance.user = user
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, "Cadastro Médico realizado com sucesso!")
            return redirect('index')

    return render(request, template_name, context)

@login_required
def create_date(request):
    template_name = 'medic/open-date.html'
    context = {}
    user = request.user

    if not is_medic(user):
        messages.add_message(request, constants.WARNING, "Você não pode acessar essa página")
        return redirect('index')
    
    if request.method == 'GET':
        form = OpenDateForm()
        medic_data = get_object_or_404(MedicalData, user=user)
        open_dates = OpenDates.objects.filter(doctor__user=user)
        
        context['medic_data'] = medic_data
        context['dates'] = open_dates
        context['form'] = form
        return render(request, template_name, context)

    if request.method == 'POST':
        form = OpenDateForm(request.POST)
        context['form'] = form

        if form.is_valid():
            if form.instance.date <= timezone.now():
                messages.add_message(request, constants.ERROR, "A data deve ser hoje ou apartir de hoje")
                return redirect('open-date')
        
            doctor = get_object_or_404(MedicalData, user=user)
            form.instance.doctor = doctor
            form.save()

            messages.add_message(request, constants.SUCCESS, "Horário cadastrado com sucesso!")
            return redirect('open-date')
        
def delete_date(request, pk):
    date = get_object_or_404(OpenDates, pk=pk)
    date.delete()
    messages.add_message(request, constants.WARNING, "Horário deletado com sucesso!")
    return redirect('open-date')

def view_date(request, pk):
    template_name = 'patient/choose-time.html'
    context = {}

    if request.method == 'GET':
        doctor = get_object_or_404(MedicalData, pk=pk)
        open_dates = OpenDates.objects.filter(doctor=doctor, status=False).filter(date__gt=timezone.now())
        context['doctor'] = doctor
        context['open_dates'] = open_dates

    return render(request, template_name, context)

def create_appointment(request, pk):
    if request.method == 'GET':
        open_date = get_object_or_404(OpenDates, pk=pk)

        appointment = Appointment(patient=request.user, open_date=open_date)
        appointment.save()

        open_date.status = True
        open_date.save()

        messages.add_message(request, constants.SUCCESS, "Horário agendado com sucesso!")
        return redirect('appointment-list')
    
    return render(request)

def appointment_list(request):
    template_name = 'patient/appointment-list.html'
    user = request.user
    
    appointments = Appointment.objects.filter(patient=user)

    if request.method == 'GET':
        doctors_filter = request.GET.get('search', '')
        date_filter = request.GET.get('date', '')

    if doctors_filter:
        appointments = appointments.filter(open_date__doctor__name__icontains=doctors_filter)
    
    if date_filter:
        appointments = appointments.filter(open_date__date__date=date_filter)

    
    context = {
        'appointments': appointments,
        'date': date_filter,
        'search': doctors_filter,
    }

    return render(request, template_name, context)

def medic_appointment_list(request):
    template_name = 'medic/appointment-list.html'
    user = request.user

    if not is_medic(user):
        messages.add_message(request, constants.WARNING, "Você não pode acessar essa página")
        return redirect('appointment-list')
    
    appointments = Appointment.objects.filter(open_date__doctor__user=user)

    today = timezone.localdate()
    today_appointments = appointments.filter(open_date__date__date=today)

    context = {
        'appointments': appointments,
        'today': today_appointments,
    }

    return render(request, template_name, context)