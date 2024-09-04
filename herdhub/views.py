from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddCowForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_cow(request):
    return render(request, 'add_cow.html', {
        'form': AddCowForm()
    })