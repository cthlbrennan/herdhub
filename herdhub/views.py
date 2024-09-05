from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddCowForm
from .models import Cow, Breeding, Calf, Bull, User, Message
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def add_cow(request):
    if request.method == "POST":
        form = AddCowForm(request.POST)
        if form.is_valid():
            new_cow = Cow(
                user=request.user,  
                registration_number=form.cleaned_data['registration_number'],
                dob=form.cleaned_data['dob'],
                breed=form.cleaned_data['breed'],
                health_status=form.cleaned_data['health_status'],
                pregnancy_status=form.cleaned_data['pregnancy_status'],
                number_of_calvings=form.cleaned_data['number_of_calvings'],
                last_calving_date=form.cleaned_data['last_calving_date'],
                milk_production=form.cleaned_data['milk_production'],
                comments=form.cleaned_data['comments']
            )
            new_cow.save()
            
            return redirect('index')  
        else:
            return render(request, 'add_cow.html', {
                'form': form,
            })
    else:
        return render(request, 'add_cow.html', {
            'form': AddCowForm()
        })