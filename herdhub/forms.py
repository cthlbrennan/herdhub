from django import forms
from .models import BreedChoices, HealthChoices, PregnancyStatus

class AddCowForm(forms.Form):
    registration_number = forms.CharField(label='Registration Number')
    dob = forms.DateField(label='Date of Birth')
    breed = forms.ChoiceField(label='Breed', choices=BreedChoices.choices)
    health_status = forms.ChoiceField(label='Health Status', choices=HealthChoices.choices)    
    pregnancy_status = forms.ChoiceField(label='Pregnancy Status', choices=PregnancyStatus.choices)
    number_of_calvings = forms.IntegerField(label='Number of Times Calved')
    last_calving_date = forms.DateField(label='Last Calving Date')
    milk_production = forms.IntegerField(label='Milk Produced Per Annum')
    comments = forms.CharField(label='Comments')