from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AddCowForm, AddBullForm, AddBreedingForm, AddCalfForm, SendMessageForm
from .models import Cow, Breeding, Calf, Bull, User, Message
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        cows = Cow.objects.filter(user=request.user) 
        bulls = Bull.objects.filter(user=request.user)
        breedings = Breeding.objects.filter(user=request.user)
        calfs = Calf.objects.filter(user=request.user)

    else:
        cows = None  
        bulls = None
        breedings = None
        calfs = None

    return render(request, 'index.html', {
        'cows': cows, 
        'bulls': bulls,
        'breedings': breedings,
        'calfs' : calfs,
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
        form = AddCowForm(request.POST, instance=cow)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = AddCowForm(instance=cow)
    
    return render(request, 'edit_cow.html', {'form': form, 'cow': cow})

@login_required
@require_POST
def delete_cow(request, cow_id):
    cow = get_object_or_404(Cow, cow_id=cow_id, user=request.user)
    cow.delete()
    return redirect('index') 

@login_required
def add_breeding_event(request):
    if request.method == 'POST':
        form = AddBreedingForm(request.POST, user=request.user)
        if form.is_valid():
            new_breeding = Breeding(
                user=request.user,  
                bull=form.cleaned_data['bull'],
                cow=form.cleaned_data['cow'],
                breeding_date=form.cleaned_data['breeding_date'],
                breeding_method=form.cleaned_data['breeding_method'],
                resulting_pregnancy=form.cleaned_data['resulting_pregnancy'],
                comments=form.cleaned_data['comments']
            )
            new_breeding.save()
            return redirect('index')
        else:
            return render(request, 'add_breeding_event.html', {
                'form' : form,
            })
    else:
        return render(request, 'add_breeding_event.html', {
        'form': AddBreedingForm(user=request.user)
    })

@login_required
def view_breeding(request, breeding_id):
    breeding = get_object_or_404(Breeding, breeding_id=breeding_id, user=request.user)
    return render(request, 'view_breeding.html', {
        'breeding': breeding
    })

@login_required
def edit_breeding(request, breeding_id):
    breeding = get_object_or_404(Breeding, breeding_id=breeding_id, user=request.user)
    
    if request.method == 'POST':
        form = AddBreedingForm(request.POST, instance=breeding)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = AddBreedingForm(instance=breeding)
    
    return render(request, 'edit_breeding.html', {'form': form, 'breeding': breeding})

@login_required
@require_POST
def delete_breeding(request, breeding_id):
    breeding = get_object_or_404(Breeding, breeding_id=breeding_id, user=request.user)
    breeding.delete()
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
        form = AddBullForm(request.POST, instance=bull)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = AddBullForm(instance=bull)
    
    return render(request, 'edit_bull.html', {'form': form,
        'bull' : bull,
    })

@login_required
@require_POST
def delete_bull(request, bull_id):
    bull = get_object_or_404(Bull, bull_id=bull_id, user=request.user)
    bull.delete()
    return redirect('index') 





@login_required
def add_calf(request):
    if request.method == "POST":
        form = AddCalfForm(request.POST)
        if form.is_valid():
            new_calf = Calf(
                user = request.user,
                registration_number=form.cleaned_data['registration_number'],
                dob=form.cleaned_data['dob'],
                breeding=form.cleaned_data['breeding'],
                sex=form.cleaned_data['sex'], 
                calving_method=form.cleaned_data['calving_method'], 
                comments=form.cleaned_data['comments']
            )
            new_calf.save()
            
            return redirect('index')  
        else:
            return render(request, 'add_calf.html', {
                'form': form,
            })
    else:
        return render(request, 'add_calf.html', {
            'form': AddCalfForm()
        })

@login_required
def view_calf(request, calf_id):
    calf = get_object_or_404(Calf, calf_id=calf_id, user=request.user)
    return render(request, 'view_calf.html', {
        'calf': calf
    })

@login_required
def edit_calf(request, calf_id):
    calf = get_object_or_404(Calf, calf_id=calf_id, user=request.user)
    if request.method == 'POST':
        form = AddCalfForm(request.POST, instance=calf)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = AddCalfForm(instance=calf)
    
    return render(request, 'edit_calf.html', {'form': form,
        'calf' : calf,
    })

@login_required
@require_POST
def delete_calf(request, calf_id):
    calf = get_object_or_404(Calf, calf_id=calf_id, user=request.user)
    calf.delete()
    return redirect('index') 

@login_required
def send_message(request):
    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            now = timezone.now()
            now_formatted = now.strftime("%H:%M %d/%m/%Y")
            new_message = Message(
                user_profile=request.user,
                sent_on=now_formatted,
                message=form.cleaned_data['message']
            )
            new_message.save()
            
            return redirect('index')  
        else:
            return render(request, 'send_message.html', {
                'form': form,
            })
    else:
        return render(request, 'send_message.html', {
            'form': SendMessageForm()
        })