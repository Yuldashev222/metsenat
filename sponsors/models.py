from django.db import models



from . import enums


from phonenumber_field import modelfields




class Sponsor(models.Model):
    full_name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=enums.SponsorType.choices())
    phone_number = modelfields.PhoneNumberField()
    organization = models.CharField(max_length=255, blank=True, null=True)
    payment_amount = models.IntegerField(help_text='so\'m da kiriting.')
    spent_amount = models.IntegerField(help_text='so\'m da kiriting.', default=0)

    status = models.CharField(max_length=15, choices=enums.SponsorStatus.choices(), default=enums.SponsorStatus.new.value)
    
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)




    
    