from django.db import models

from sponsors.models import Sponsor



from . import enums


from phonenumber_field import modelfields



class Univer(models.Model):
    name = models.CharField(max_length=400, unique=True)
    contract_amount = models.IntegerField(help_text='so\'m da kiriting.')


class Student(models.Model):
    univer = models.ForeignKey(Univer, on_delete=models.CASCADE)
    sponsors = models.ManyToManyField(Sponsor, related_name='students', blank=True)
    
    
    full_name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=enums.StudentType.choices())
    phone_number = modelfields.PhoneNumberField()
    allocated_amount = models.IntegerField(help_text='so\'m da kiriting.', default=0)


    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
