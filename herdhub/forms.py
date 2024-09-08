from django import forms
from .models import BreedChoices, HealthChoices, PregnancyStatus, Cow, Bull, Calf, Breeding, Message

class AddCowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['registration_number', 'dob', 'breed', 'health_status', 
                  'pregnancy_status', 'number_of_calvings', 'last_calving_date', 
                  'milk_production', 'comments']
    
class AddBullForm(forms.ModelForm):
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

class AddCalfForm(forms.ModelForm):
    class Meta:
        model = Calf
        fields = ['registration_number', 'dob', 'breeding', 'sex', 'calving_method', 'comments']

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']