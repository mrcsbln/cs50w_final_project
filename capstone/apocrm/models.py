from django.db import models

class Patient(models.Model):
    DEPARTMENT_CHOICES = [
        ('ON', 'Onkologie'),
        ('NE', 'Neurologie'),
        ('HV', 'HV'),
        ('RE', 'Rezeptur'),
        ('SL', 'Sterillabor'),
        ('OP', 'Ophthalmologie'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    street = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    department = models.CharField(
        max_length=2, 
        choices=DEPARTMENT_CHOICES,
        default='ON',
    )
    case_description = models.TextField(max_length=1000)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
