from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    phone=models.CharField(max_length=15)

    

class Appointment(models.Model):

    TIME_SLOT_CHOICES = [

        ('10:00-10:30','10:00 AM - 10:30 AM'),
        ('10:30-11:00','10:30 AM - 11:00 AM'),
        ('11:00-11:30','11:00 AM - 11:30 AM'),
        ('11:30-12:00','11:30 AM - 12:00 PM'),
        ('12:00-12:30','12:00 PM - 12:30 PM'),
        ('12:30-1:00','12:30 PM - 1:00 PM'),
         #1-2 LUNCH BREAK
        ('2:00-2:30','2:00 PM - 2:30 PM'),
        ('2:30-3:00','2:30 PM - 3:00 PM'),
        ('3:00-3:30','3:00 PM - 3:30 PM'),
        ('3:30-4:00','3:30 PM - 4:00 PM'),
        ('4:00-4:30','4:00 PM - 4:30 PM'),
        ('4:30-5:00','4:30 PM - 5:00 PM'),
    ]

    name=models.CharField(max_length=100)

    phone_number=models.CharField(max_length=15)

    date=models.DateField()

    time_slot=models.CharField(max_length=20,choices=TIME_SLOT_CHOICES)

    created_at=models.DateTimeField(auto_now_add=True)

    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='appointments')

    # class Meta:

    #     unique_together=['date','time_slot']

    def __str__(self):
        return f"{self.name} - {self.date} - {self.time_slot}"



