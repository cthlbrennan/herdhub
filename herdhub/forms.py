from django import forms
from .models import BreedChoices, HealthChoices, PregnancyStatus, Cow, Bull, Calf, Breeding

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

class EditCowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['registration_number', 'dob', 'breed', 'health_status', 
                  'pregnancy_status', 'number_of_calvings', 'last_calving_date', 
                  'milk_production', 'comments']
    
class AddBullForm(forms.Form):
    registration_number = forms.CharField(label='Registration Number')
    dob = forms.DateField(label='Date of Birth')
    breed = forms.ChoiceField(label='Breed', choices=BreedChoices.choices)
    health_status = forms.ChoiceField(label='Health Status', choices=HealthChoices.choices)    
    comments = forms.CharField(label='Comments')

class EditBullForm(forms.ModelForm):
    class Meta:
        model = Bull
        fields = ['registration_number', 'dob', 'breed', 'health_status', 'comments']

class AddBullForm(forms.Form):
    registration_number = forms.CharField(label='Registration Number')
    dob = forms.DateField(label='Date of Birth')
    breed = forms.ChoiceField(label='Breed', choices=BreedChoices.choices)
    health_status = forms.ChoiceField(label='Health Status', choices=HealthChoices.choices)    
    comments = forms.CharField(label='Comments')

class EditBullForm(forms.ModelForm):
    class Meta:
        model = Bull
        fields = ['registration_number', 'dob', 'breed', 'health_status', 'comments']

class AddBreedingForm(forms.ModelForm):
    class Meta:
        model = Breeding
        fields = ['bull', 'cow', 'breeding_date', 'breeding_method', 'resulting_pregnancy', 'comments']
        widgets = {
            'breeding_date': forms.DateInput(attrs={'type': 'date'}),
        }