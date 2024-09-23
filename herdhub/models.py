from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator
from cloudinary.models import CloudinaryField

# Create your models here.


class BreedChoices(models.TextChoices):
    """
    Choices for cattle breeds.
    """
    HOLSTEIN = 'Holstein', 'Holstein'
    JERSEY = 'Jersey', 'Jersey'
    ANGUS = 'Angus', 'Angus'
    OTHER = 'Other', 'Other'
    HEREFORD = 'Hereford', 'Hereford'
    SIMMENTAL = 'Simmental', 'Simmental'
    LIMOUSIN = 'Limousin', 'Limousin'
    CHAROLAIS = 'Charolais', 'Charolais'


class HealthChoices(models.TextChoices):
    """
    Choices for animal health status.
    """
    POOR = "Poor", 'Poor'
    GOOD = "Good", 'Good'
    EXCELLENT = "Excellent", 'Excellent'


class PregnancyStatus(models.TextChoices):
    """
    Choices for cow pregnancy status.
    """
    NOT_PREGNANT = "Not Pregnant", "Not Pregnant"
    PREGNANT = "Pregnant", "Pregnant"
    IN_HEAT = "In Heat", "In Heat"
    DRY = "Dry", "Dry"
    LACTATING = "Lactating", "Lactating"
    FRESH = 'Fresh', "Fresh"
    CALVING = "Calving", "Calving"


class CalfSex(models.TextChoices):
    """
    Choices for calf sex.
    """
    MALE = "Male", "Male"
    FEMALE = "Female", "Female"


class BreedingMethod(models.TextChoices):
    """
    Choices for breeding methods.
    """
    NATURAL_SERVICE = "Natural Service", "Natural Service"
    ARTIFICIAL_INSEMINATION = "Artificial Insemination",
    "Artificial Insemination"


class CalvingMethod(models.TextChoices):
    """
    Choices for calving methods.
    """
    NATURAL_UNASSISTED = 'Natural Unassisted', 'Natural Unassisted'
    ASSISTED = 'Assisted', 'Assisted'
    C_SECTION = 'C-Section', 'C-Section'
    INDUCTION = 'Induction', 'Induction'
    EMERGENCY_ASSISTANCE = 'Emergency Assistance', 'Emergency Assistance'


class Message(models.Model):
    """
    Model representing messages which can be
    submitted by users directly to the admin.
    """
    message_id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_on = models.CharField()
    message = models.TextField(max_length=3000)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.user_profile}"


class Bull(models.Model):
    """
    Model representing a bull in the herd.
    """
    bull_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = CloudinaryField('image', blank=True, default='')
    registration_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9]+$',
                message=(
                    'Registration number must be alphanumeric only, '
                    '10 characters max.'
                ),
            )
        ]
    )
    dob = models.DateField()
    breed = models.CharField(
        choices=BreedChoices.choices,
        default=BreedChoices.HOLSTEIN,
    )
    health_status = models.CharField(
        choices=HealthChoices.choices,
        default=HealthChoices.GOOD,
    )
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Bull {self.registration_number}: Breed {self.breed}"


class Cow(models.Model):
    """
    Model representing a cow in the herd.
    """
    cow_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = CloudinaryField('image', blank=True, default='')
    registration_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9]+$',
                message=(
                    'Registration number must be alphanumeric only, '
                    '10 characters max.'
                ),
            )
        ]
    )
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
        choices=PregnancyStatus.choices,
        default=PregnancyStatus.NOT_PREGNANT
    )
    number_of_calvings = models.IntegerField(
        null=False,
        blank=False,
        default='0',
        validators=[MinValueValidator(0)]
        )
    last_calving_date = models.DateField(
        null=True, 
        blank=True
    )
    milk_production = models.IntegerField(
        null=False,
        blank=False,
        default='2000',
        validators=[MinValueValidator(0)]
        )
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Cow {self.registration_number}: Breed {self.breed}"


class Breeding(models.Model):
    """
    Model representing a breeding event.
    """
    breeding_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bull = models.ForeignKey(Bull, on_delete=models.CASCADE)
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    breeding_date = models.DateField()
    breeding_method = models.CharField(
        choices=BreedingMethod.choices,
        default=BreedingMethod.NATURAL_SERVICE,
    )
    resulting_pregnancy = models.BooleanField()
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return (
            f"Bull {self.bull.registration_number} x "
            f"Cow {self.cow.registration_number}"
        )


class Calf(models.Model):
    """
    Model representing a calf in the herd.
    """
    calf_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = CloudinaryField('image', blank=True, default='')
    registration_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9]+$',
                message=(
                    'Registration number must be alphanumeric only, '
                    '10 characters max.'
                ),
            )
        ]
    )
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
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Calf: {self.registration_number}"
