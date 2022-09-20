from django.db import models


from students.models import Student
from sponsors.models import Sponsor



class Agreement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT)

    amount = models.IntegerField()
    