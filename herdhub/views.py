from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from .forms import AddCowForm, AddBullForm, AddBreedingForm, AddCalfForm, SendMessageForm
from .models import Cow, Breeding, Calf, Bull, User, Message

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        cows = Cow.objects.filter(user=request.user) 
        bulls = Bull.objects.filter(user=request.user)
        breedings = Breeding.objects.filter(user=request.user)
        calfs = Calf.objects.filter(user=request.user)
        cow_count = cows.count()
        bull_count = bulls.count()
        breeding_count = breedings.count()
        calf_count = calfs.count()
        herd_total = calf_count + bull_count + cow_count
    else:
        cows = None  
        bulls = None
        breedings = None
        calfs = None
        cow_count = 0
        bull_count = 0
        breeding_count = 0
        calf_count = 0
        herd_total = 0

    return render(request, 'index.html', {
        'cows': cows, 
        'bulls': bulls,
        'breedings': breedings,
        'calfs' : calfs,
        'cow_count' : cow_count,
        'bull_count' : bull_count, 
        'breeding_count' : breeding_count,
        'calf_count' : calf_count,
        'herd_total' : herd_total
        })

# Create your views here.
def about(request):

    return render(request, 'about.html')

@login_required
def add_cow(request):
    if request.method == "POST":
        form = AddCowForm(request.POST, request.FILES)
        if form.is_valid():
            new_cow = form.save(commit=False)
            new_cow.user = request.user
            if 'image' in request.FILES:
                new_cow.image_id = request.FILES['image']
            new_cow.save()
            return redirect('index')
    else:
        form = AddCowForm()
    return render(request, 'add_cow.html', {'form': form})

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
        if 'remove_image' in request.POST:
            cow.image_id = None
            cow.save()
            return redirect('edit_cow', cow_id=cow.cow_id)
        
        form = AddCowForm(request.POST, request.FILES, instance=cow)
        if form.is_valid():
            if 'image' in request.FILES:
                cow.image_id = request.FILES['image']
            form.save()
            return redirect('view_cow', cow_id=cow.cow_id)
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
        cows = Cow.objects.filter(user=request.user)
        bulls = Bull.objects.filter(user=request.user)
        not_enough_animals = cows.count() == 0 or bulls.count() == 0
        return render(request, 'add_breeding_event.html', {
        'form': AddBreedingForm(user=request.user), 
        'number_of_animals' : not_enough_animals,
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
    if request.method == 'POST':
        form = AddBullForm(request.POST, request.FILES)
        if form.is_valid():
            bull = form.save(commit=False)
            bull.user = request.user
            if 'image' in request.FILES:
                bull.image_id = request.FILES['image']
            bull.save()
            return redirect('view_bull', bull_id=bull.bull_id)
    else:
        form = AddBullForm()

    return render(request, 'add_bull.html', {'form': form})

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
        if 'remove_image' in request.POST:
            bull.image_id = None  # This will remove the image
            bull.save()
            return redirect('edit_bull', bull_id=bull.bull_id)
        
        form = AddBullForm(request.POST, request.FILES, instance=bull)
        if form.is_valid():
            if 'image' in request.FILES:
                bull.image_id = request.FILES['image']
            form.save()
            return redirect('view_bull', bull_id=bull.bull_id)
    else:
        form = AddBullForm(instance=bull)
    
    return render(request, 'edit_bull.html', {
        'form': form,
        'bull': bull,
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
        form = AddCalfForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            new_calf = form.save(commit=False)
            new_calf.user = request.user
            if 'image' in request.FILES:
                new_calf.image_id = request.FILES['image']
            new_calf.save()
            return redirect('index')
        else:
            print(form.errors)  # Add this line for debugging
    else:
        form = AddCalfForm(user=request.user)
    return render(request, 'add_calf.html', {'form': form})

@login_required
def view_calf(request, calf_id):
    calf = get_object_or_404(Calf, calf_id=calf_id, user=request.user)
    breeding = calf.breeding
    dam = breeding.cow
    sire = breeding.bull

    return render(request, 'view_calf.html', {
        'calf': calf, 
        'dam' : dam,
        'sire' : sire, 
        'bull_id': sire.bull_id if sire else None,
        'cow_id': dam.cow_id if dam else None,
    })

@login_required
def edit_calf(request, calf_id):
    calf = get_object_or_404(Calf, calf_id=calf_id, user=request.user)
    
    if request.method == 'POST':
        if 'remove_image' in request.POST:
            calf.image_id = None  # This will remove the image
            calf.save()
            return redirect('edit_calf', calf_id=calf.calf_id)
        
        form = AddCalfForm(request.POST, request.FILES, instance=calf, user=request.user)
        if form.is_valid():
            if 'image' in request.FILES:
                calf.image_id = request.FILES['image']
            form.save()
            return redirect('view_calf', calf_id=calf.calf_id)
    else:
        form = AddCalfForm(instance=calf, user=request.user)
    
    return render(request, 'edit_calf.html', {
        'form': form,
        'calf': calf,
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