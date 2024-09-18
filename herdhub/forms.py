from django import forms
from .models import BreedChoices, HealthChoices, PregnancyStatus, Cow, Bull, Calf, Breeding, Message
from cloudinary.forms import CloudinaryFileField

class AddCowForm(forms.ModelForm):
    image = CloudinaryFileField(
        options = {
            'folder': 'cows',
            'allowed_formats': ['jpg', 'png'],
            'public_id': None,
        },
        required=False
    )
    class Meta:
        model = Cow
        fields = ['registration_number', 'dob', 'breed', 'health_status', 
                  'pregnancy_status', 'number_of_calvings', 'last_calving_date', 
                  'milk_production', 'comments', 'image']

        labels = {
            'registration_number': 'Registration Number',
            'dob': 'Date of Birth',
            'breed': 'Breed',
            'health_status': 'Health Status',
            'pregnancy_status': 'Pregnancy Status',
            'number_of_calvings': 'Number of Previous Calvings',
            'last_calving_date': 'Last Calving Date',
            'milk_production': 'Milk Production (litres per annum)',
            'comments': 'Comments',
            'image': 'Upload Image'
        }
        
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'last_calving_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
class AddBullForm(forms.ModelForm):
    image = CloudinaryFileField(
        options = {
            'folder': 'bulls',
            'allowed_formats': ['jpg', 'png'],
            'public_id': None,
        },
        required=False
    )    
    
    class Meta:
        model = Bull
        fields = ['registration_number', 'dob', 'breed', 'health_status', 'comments', 'image']
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
    image = CloudinaryFileField(
        options = {
            'folder': 'calves',  # Changed from 'calfs' to 'calves' for consistency
            'allowed_formats': ['jpg', 'png'],
            'public_id': None,
        },
        required=False
    )
    
    class Meta:
        model = Calf
        fields = ['registration_number', 'dob', 'breeding', 'sex', 'calving_method', 'comments', 'image']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddCalfForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['breeding'].queryset = Breeding.objects.filter(user=user)

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']