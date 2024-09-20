from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages
from .forms import AddCowForm, AddBullForm, AddBreedingForm, AddCalfForm, SendMessageForm
from .models import Cow, Breeding, Calf, Bull, User, Message

# Create your views here.
def index(request):
    """
    Render the index page with herd statistics if the user is authenticated.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered index page with context data.
    """
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
        'calfs': calfs,
        'cow_count': cow_count,
        'bull_count': bull_count, 
        'breeding_count': breeding_count,
        'calf_count': calf_count,
        'herd_total': herd_total
    })

def about(request):
    """
    Render the about page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered about page.
    """
    return render(request, 'about.html')

@login_required
def add_cow(request):
    """
    Handle the addition of a new cow to the user's herd.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to index on successful addition, or renders the add_cow form.
    """
    if request.method == "POST":
        form = AddCowForm(request.POST, request.FILES)
        if form.is_valid():
            new_cow = form.save(commit=False)
            new_cow.user = request.user
            if 'image' in request.FILES:
                new_cow.image_id = request.FILES['image']
            new_cow.save()
            messages.success(request, 'Cow added successfully!')
            return redirect('index')          
    else:
        form = AddCowForm()
    return render(request, 'add_cow.html', {'form': form})

@login_required
def view_cow(request, cow_id):
    """
    Display details of a specific cow.

    Args:
        request (HttpRequest): The HTTP request object.
        cow_id (int): The ID of the cow to view.

    Returns:
        HttpResponse: Rendered view_cow page with cow details.
    """
    cow = get_object_or_404(Cow, cow_id=cow_id, user=request.user)
    return render(request, 'view_cow.html', {
        'cow': cow
    })

@login_required
def edit_cow(request, cow_id):
    """
    Handle the editing of an existing cow's details.

    Args:
        request (HttpRequest): The HTTP request object.
        cow_id (int): The ID of the cow to edit.

    Returns:
        HttpResponse: Redirects to view_cow on successful edit, or renders the edit_cow form.
    """
    cow = get_object_or_404(Cow, cow_id=cow_id, user=request.user)
    
    if request.method == 'POST':
        if 'remove_image' in request.POST:
            cow.image_id = None
            cow.save()
            messages.success(request, 'Image of Cow removed')
            return redirect('edit_cow', cow_id=cow.cow_id)
        
        form = AddCowForm(request.POST, request.FILES, instance=cow)
        if form.is_valid():
            if 'image' in request.FILES:
                cow.image_id = request.FILES['image']
                messages.success(request, 'Image of Cow added')
            else:
                messages.success(request, f'Cow {cow.registration_number} details updated')
            form.save()
            return redirect('view_cow', cow_id=cow.cow_id)
    else:
        form = AddCowForm(instance=cow)
    
    return render(request, 'edit_cow.html', {'form': form, 'cow': cow})

@login_required
@require_POST
def delete_cow(request, cow_id):
    """
    Handle the deletion of a cow from the user's herd.

    Args:
        request (HttpRequest): The HTTP request object.
        cow_id (int): The ID of the cow to delete.

    Returns:
        HttpResponse: Redirects to index after successful deletion.
    """
    cow = get_object_or_404(Cow, cow_id=cow_id, user=request.user)
    cow.delete()
    messages.success(request, f'Cow {cow.registration_number} deleted successfully')
    return redirect('index') 

@login_required
def add_breeding_event(request):
    """
    Handle the addition of a new breeding event.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to index on successful addition, or renders the add_breeding form.
    """
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
            messages.success(request, 'Breeding event added successfully!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error adding the breeding event')
    else:
        cows = Cow.objects.filter(user=request.user)
        bulls = Bull.objects.filter(user=request.user)
        not_enough_animals = cows.count() == 0 or bulls.count() == 0
        form = AddBreedingForm(user=request.user)
    
    return render(request, 'add_breeding_event.html', {
        'form': form, 
        'number_of_animals': not_enough_animals,
    })

@login_required
def view_breeding(request, breeding_id):
    """
    Display details of a specific breeding event.

    Args:
        request (HttpRequest): The HTTP request object.
        breeding_id (int): The ID of the breeding event to view.

    Returns:
        HttpResponse: Rendered view_breeding page with breeding event details.
    """
    breeding = get_object_or_404(Breeding, breeding_id=breeding_id, user=request.user)
    return render(request, 'view_breeding.html', {
        'breeding': breeding
    })

@login_required
def edit_breeding(request, breeding_id):
    """
    Handle the editing of an existing breeding event's details.

    Args:
        request (HttpRequest): The HTTP request object.
        breeding_id (int): The ID of the breeding event to edit.

    Returns:
        HttpResponse: Redirects to view_breeding on successful edit, or renders the edit_breeding form.
    """
    breeding = get_object_or_404(Breeding, breeding_id=breeding_id, user=request.user)
    
    if request.method == 'POST':
        form = AddBreedingForm(request.POST, instance=breeding)
        if form.is_valid():
            form.save()
            messages.success(request, f'{breeding.bull} x {breeding.cow} event updated successfully!') 
            return redirect('index') 
    else:
        form = AddBreedingForm(instance=breeding)
    
    return render(request, 'edit_breeding.html', {'form': form, 'breeding': breeding})

@login_required
@require_POST
def delete_breeding(request, breeding_id):
    """
    Handle the deletion of a breeding event.

    Args:
        request (HttpRequest): The HTTP request object.
        breeding_id (int): The ID of the breeding event to delete.

    Returns:
        HttpResponse: Redirects to index after successful deletion.
    """
    breeding = get_object_or_404(Breeding, breeding_id=breeding_id, user=request.user)
    breeding.delete()
    messages.success(request, f'{breeding} deleted successfully')
    return redirect('index') 

@login_required
def add_bull(request):
    """
    Handle the addition of a new bull to the user's herd.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to index on successful addition, or renders the add_bull form.
    """
    if request.method == 'POST':
        form = AddBullForm(request.POST, request.FILES)
        if form.is_valid():
            bull = form.save(commit=False)
            bull.user = request.user
            if 'image' in request.FILES:
                bull.image_id = request.FILES['image']
            bull.save()
            messages.success(request, 'Bull added successfully!')
            return redirect('view_bull', bull_id=bull.bull_id)
    else:
        form = AddBullForm()

    return render(request, 'add_bull.html', {'form': form})

@login_required
def view_bull(request, bull_id):
    """
    Display details of a specific bull.

    Args:
        request (HttpRequest): The HTTP request object.
        bull_id (int): The ID of the bull to view.

    Returns:
        HttpResponse: Rendered view_bull page with bull details.
    """
    bull = get_object_or_404(Bull, bull_id=bull_id, user=request.user)
    return render(request, 'view_bull.html', {
        'bull': bull
    })

@login_required
def edit_bull(request, bull_id):
    """
    Handle the editing of an existing bull's details.

    Args:
        request (HttpRequest): The HTTP request object.
        bull_id (int): The ID of the bull to edit.

    Returns:
        HttpResponse: Redirects to view_bull on successful edit, or renders the edit_bull form.
    """
    bull = get_object_or_404(Bull, bull_id=bull_id, user=request.user)
    
    if request.method == 'POST':
        if 'remove_image' in request.POST:
            bull.image_id = None
            bull.save()
            messages.success(request, 'Image of Bull removed')
            return redirect('edit_bull', bull_id=bull.bull_id)
        
        form = AddBullForm(request.POST, request.FILES, instance=bull)
        if form.is_valid():
            if 'image' in request.FILES:
                bull.image_id = request.FILES['image']
                messages.success(request, 'Image of Bull added')
            else:
                messages.success(request, 'Bull details updated')
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
    """
    Handle the deletion of a bull from the user's herd.

    Args:
        request (HttpRequest): The HTTP request object.
        bull_id (int): The ID of the bull to delete.

    Returns:
        HttpResponse: Redirects to index after successful deletion.
    """
    bull = get_object_or_404(Bull, bull_id=bull_id, user=request.user)
    bull.delete()
    messages.success(request, 'Bull deleted successfully')
    return redirect('index') 

@login_required
def add_calf(request):
    """
    Handle the addition of a new calf to the user's herd.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to index on successful addition, or renders the add_calf form.
    """
    if request.method == "POST":
        form = AddCalfForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            new_calf = form.save(commit=False)
            new_calf.user = request.user
            if 'image' in request.FILES:
                new_calf.image_id = request.FILES['image']
            new_calf.save()
            messages.success(request, 'Calf added successfully!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error adding the calf.')
    else:
        form = AddCalfForm(user=request.user)
    return render(request, 'add_calf.html', {'form': form})

@login_required
def view_calf(request, calf_id):
    """
    Display details of a specific calf.

    Args:
        request (HttpRequest): The HTTP request object.
        calf_id (int): The ID of the calf to view.

    Returns:
        HttpResponse: Rendered view_calf page with calf details.
    """
    calf = get_object_or_404(Calf, calf_id=calf_id, user=request.user)
    breeding = calf.breeding
    dam = breeding.cow
    sire = breeding.bull

    return render(request, 'view_calf.html', {
        'calf': calf, 
        'dam': dam,
        'sire': sire, 
        'bull_id': sire.bull_id if sire else None,
        'cow_id': dam.cow_id if dam else None,
    })

@login_required
def edit_calf(request, calf_id):
    """
    Handle the editing of an existing calf's details.

    Args:
        request (HttpRequest): The HTTP request object.
        calf_id (int): The ID of the calf to edit.

    Returns:
        HttpResponse: Redirects to view_calf on successful edit, or renders the edit_calf form.
    """
    calf = get_object_or_404(Calf, calf_id=calf_id, user=request.user)
    
    if request.method == 'POST':
        if 'remove_image' in request.POST:
            calf.image_id = None
            calf.save()
            messages.success(request, 'Image of Calf removed')
            return redirect('edit_calf', calf_id=calf.calf_id)
        
        form = AddCalfForm(request.POST, request.FILES, instance=calf, user=request.user)
        if form.is_valid():
            if 'image' in request.FILES:
                calf.image_id = request.FILES['image']
                messages.success(request, 'Image of Calf added')
            else:
                messages.success(request, 'Calf details updated')
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
    """
    Handle the deletion of a calf from the user's herd.

    Args:
        request (HttpRequest): The HTTP request object.
        calf_id (int): The ID of the calf to delete.

    Returns:
        HttpResponse: Redirects to index after successful deletion.
    """
    calf = get_object_or_404(Calf, calf_id=calf_id, user=request.user)
    calf.delete()
    messages.success(request, 'Calf deleted successfully')
    return redirect('index') 

@login_required
def send_message(request):
    """
    Handle the sending of a message through the contact form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to index on successful message send, or renders the send_message form.
    """
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
            messages.success(request, 'Message sent successfully!')
            return redirect('index')  
        else:
            messages.error(request, 'There was an error sending the message')
    else:
        form = SendMessageForm()
    
    return render(request, 'send_message.html', {'form': form})

def show404page(request, exception):
    """
    Handles 404 errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that was raised.

    Returns:
        HttpResponse: Redirects user to custom 404.html page 
    """
    return render(request, '404.html', status=404)
    
def show500page(request, exception):
    """
    Handles 500 errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that was raised.

    Returns:
        HttpResponse: Redirects user to custom 500.html page
    """
    return render(request, '500.html', status=500)
