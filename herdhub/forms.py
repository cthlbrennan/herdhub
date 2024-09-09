from django import forms
from .models import BreedChoices, HealthChoices, PregnancyStatus, Cow, Bull, Calf, Breeding, Message

class AddCowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['registration_number', 'dob', 'breed', 'health_status', 
                  'pregnancy_status', 'number_of_calvings', 'last_calving_date', 
                  'milk_production', 'comments']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
        widgets = {
            'last_calving_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
class AddBullForm(forms.ModelForm):
    class Meta:
        model = Bull
        fields = ['registration_number', 'dob', 'breed', 'health_status', 'comments']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class AddBreedingForm(forms.ModelForm):
    class Meta:
        model = Breeding
        fields = ['bull', 'cow', 'breeding_date', 'breeding_method', 'resulting_pregnancy', 'comments']
        widgets = {
            'breeding_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        # Expecting the user to be passed as a keyword argument
        user = kwargs.pop('user', None)
        super(AddBreedingForm, self).__init__(*args, **kwargs)

        if user:
            # Limit bull queryset to the bulls and cows owned by the current user
            self.fields['bull'].queryset = Bull.objects.filter(user=user)
            self.fields['cow'].queryset = Cow.objects.filter(user=user)

class AddCalfForm(forms.ModelForm):
    class Meta:
        model = Calf
        fields = ['registration_number', 'dob', 'breeding', 'sex', 'calving_method', 'comments']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']