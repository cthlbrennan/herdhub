from django.db import models

# Create your models here.

class BreedChoices(models.TextChoices):
    HOLSTEIN = 'HOL', 'Holstein'
    JERSEY = 'JER', 'Jersey'
    ANGUS = 'ANG', 'Angus'
    OTHER = 'OTH', 'Other'
    HEREFORD = 'HER', 'Hereford'
    SIMMENTAL = 'SIM', 'Simmental'
    LIMOUSIN = 'LIM', 'Limousin'
    CHAROLAIS = 'CHA', 'Charolais'

class HealthChoices(models.TextChoices):
    POOR = "P", 'Poor'
    GOOD = "G", 'Good'
    EXCELLENT = "E", 'Excellent'

class PregnancyStatus(models.TextChoices):
    NOT_PREGNANT = "NP", "Not Pregnant"
    PREGNANT = "PR", "Pregnant"
    IN_HEAT = "IH", "In Heat"
    DRY = "DR", "Dry"
    LACTATING = "LC", "Lactating"
    FRESH = 'FR', "Fresh"
    CALVING = "CV", "Calving"

class CalfSex(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"

class BreedingMethod(models.TextChoices):
    NATURAL_SERVICE = "NS", "Natural Service"  
    ARTIFICIAL_INSEMINATION = "AI", "Artificial Insemination"  

class CalvingMethod(models.TextChoices):
    NATURAL_UNASSISTED = 'NU', 'Natural Unassisted'
    ASSISTED = 'AS', 'Assisted'  
    C_SECTION = 'CS', 'C-Section'  
    INDUCTION = 'IN', 'Induction'  
    EMERGENCY_ASSISTANCE = 'EA', 'Emergency Assistance'  

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=25)
    email = models.EmailField()
    account_created = models.DateField()

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_on = models.DateField()
    message = models.TextField()

class Bull(models.Model):
    bull_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=10)
    dob = models.DateField()
    breed = models.CharField(
        choices=BreedChoices.choices,
        default=BreedChoices.HOLSTEIN,
    )    
    health_status = models.CharField(
        choices=HealthChoices.choices,
        default=HealthChoices.GOOD,
    )   
    comments = models.TextField()


    def __str__(self):
        return f"Bull {self.registration_number}: Breed {self.breed}"

class Cow(models.Model):
    cow_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=10)
    dob = models.DateField()
    breed = models.CharField(
        choices=BreedChoices.choices,
        default=BreedChoices.HOLSTEIN,
    )    
    health_status = models.CharField(
        choices=HealthChoices.choices,
        default=HealthChoices.GOOD,
    )     
    pregnancy_status = models.CharField(
        choices=PregancyStatus.choices,
        default=PregnancyStatus.NOT_PREGNANT
    )
    number_of_calvings = models.IntegerField()
    last_calving_date = models.DateField()
    milk_production = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"Cow {self.registration_number}: Breed {self.breed}"

class Breeding(models.Model):
    breeding_id = models.AutoField(primary_key=True)
    bull = models.ForeignKey(Bull, on_delete=models.CASCADE)
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    breeding_date = models.DateField()
    breeding_method = models.CharField(
        choices=BreedingMethod.choices,
        default=BreedingMethod.NATURAL_SERVICE,
    )
    resulting_pregnancy = models.BooleanField()
    comments = models.TextField()

    def __str__(self):
        return f"Breeding {self.breeding_id}"


class Calf(models.Model):
    calf_id = models.AutoField(primary_key=True)
    registration_number = models.CharField(max_length=10)
    breeding = models.ForeignKey(Breeding, on_delete=models.CASCADE)
    sex = models.CharField(
        choices=CalfSex.choices,
        default=CalfSex.MALE,
    )
    dob = models.DateField()
    calving_method = models.CharField(
        choices=CalvingMethod.choices,
        default=CalvingMethod.NATURAL_UNASSISTED,
    )
    comments = models.TextField()

    def __str__(self):
        return f"Calf: {self.registration_number}"