from django import forms
from .models import BreedChoices

class AddCowForm(forms.Form):
    registration_number = forms.CharField(label='Registration Number')
    dob = forms.DateField(label='Date of Birth')
    breed = forms.ChoiceField(label='Breed', choices=BreedChoices.choices)