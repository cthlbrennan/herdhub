from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AddCowForm, EditCowForm, AddBullForm, EditBullForm
from .models import Cow, Breeding, Calf, Bull, User, Message
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        cows = Cow.objects.filter(user=request.user) 
        bulls = Bull.objects.filter(user=request.user) 
    else:
        cows = None  
        bulls = None

    return render(request, 'index.html', {
        'cows': cows, 
        'bulls': bulls,
        })

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

@login_required
def view_cow(request, cow_id):
    cow = get_object_or_404(Cow, cow_id=cow_id, user=request.user)
    return render(request, 'view_cow.html', {
        'cow': cow
    })

@login_required
def edit_cow(request, cow_id):
    cow = get_object_or_404(Cow, cow_id=cow_id, user=request.user)
    
    if request.method == 'POST':
        form = EditCowForm(request.POST, instance=cow)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = EditCowForm(instance=cow)
    
    return render(request, 'edit_cow.html', {'form': form, 'cow': cow})

@login_required
@require_POST
def delete_cow(request, cow_id):
    cow = get_object_or_404(Cow, cow_id=cow_id, user=request.user)
    cow.delete()
    return redirect('index') 










@login_required
def add_bull(request):
    if request.method == "POST":
        form = AddBullForm(request.POST)
        if form.is_valid():
            new_bull = Bull(
                user = request.user,
                registration_number=form.cleaned_data['registration_number'],
                dob=form.cleaned_data['dob'],
                breed=form.cleaned_data['breed'],
                health_status=form.cleaned_data['health_status'],   
                comments=form.cleaned_data['comments']
            )
            new_bull.save()
            
            return redirect('index')  
        else:
            return render(request, 'add_bull.html', {
                'form': form,
            })
    else:
        return render(request, 'add_bull.html', {
            'form': AddBullForm()
        })

@login_required
def view_bull(request, bull_id):
    bull = get_object_or_404(Bull, bull_id=bull_id, user=request.user)
    return render(request, 'view_bull.html', {
        'bull': bull
    })

@login_required
def edit_bull(request, bull_id):
    bull = get_object_or_404(Bull, bull_id=bull_id, user=request.user)
    
    if request.method == 'POST':
        form = EditBullForm(request.POST, instance=bull)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = EditBullForm(instance=bull)
    
    return render(request, 'edit_bull.html', {'form': form,
        'bull' : bull,
    })

@login_required
@require_POST
def delete_bull(request, bull_id):
    bull = get_object_or_404(Bull, bull_id=bull_id, user=request.user)
    bull.delete()
    return redirect('index') 