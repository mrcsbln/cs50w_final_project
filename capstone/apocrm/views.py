from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient
from .forms import PatientForm as AddPatinetRecord
from django.db.models import Q
from datetime import datetime


def index(request):
    patients = Patient.objects.all()
    # check to see if loggin in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login user
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('index')
        else:
            messages.success(request, ("Error logging in - Please try again"))
            return redirect('index')
    else:
        return render(request, 'apocrm/index.html', {'patients': patients})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('index')

def patient_record(request, pk):
    if request.user.is_authenticated:
        patient_record = Patient.objects.get(pk=pk)
        return render(request, 'apocrm/patient_record.html', {'patient_record': patient_record})
    else:
        messages.success(request, ("Please login"))
        return redirect('index')
    
def delete_patient_record(request, pk):
    if request.user.is_authenticated:
        delete_patient_record = Patient.objects.get(pk=pk)
        delete_patient_record.delete()
        messages.success(request, ("Patient record has been deleted"))
        return redirect('index')
    else:
        messages.success(request, ("Please login"))
        return redirect('index')
    
def add_patient_record(request):
    form = AddPatinetRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_patient_record = form.save()
                messages.success(request, ("Patient record has been added"))
                return redirect('index')
        return render(request, 'apocrm/add_patient_record.html', {'form': form})
    else:
        messages.success(request, ("Please login"))
        return redirect('index')
   
    
def edit_patient_record(request, pk):
    if request.user.is_authenticated:
        patient_record = Patient.objects.get(pk=pk)
        form = AddPatinetRecord(request.POST or None, instance=patient_record)
        if form.is_valid():
            form.save()
            messages.success(request, ("Patient record has been edited"))
            return redirect('index')
        return render(request, 'apocrm/edit_patient_record.html', {'form': form})
    else:
        messages.success(request, ("Please login"))
        return redirect('index')
    

def search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST['searched']
            
            # Versuch, das gesuchte als Datum zu interpretieren
            try:
                searched_date = datetime.strptime(searched, '%d.%m.%Y').date()
            except ValueError:
                searched_date = None
            
            # Erstellen von Q-Objekten für die Abfrage, einschließlich eines Q-Objekts für das Geburtsdatum, wenn die Datumskonvertierung erfolgreich war
            query = Q(first_name__icontains=searched) | Q(last_name__icontains=searched)
            if searched_date:
                query |= Q(date_of_birth=searched_date)
            
            # Durchführen der Abfrage
            patients = Patient.objects.filter(query)
            
            # Weiterleitung basierend auf der Anzahl der Ergebnisse
            if patients.count() == 1:
                patient = patients.first()
                return redirect('patient_record', pk=patient.pk)
            else:
                return render(request, 'apocrm/search.html', {'searched': searched, 'patients': patients})
        else:
            return render(request, 'apocrm/search.html', {})
    else:
        messages.success(request, ("Please login"))
        return redirect('index')

