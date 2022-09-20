from django.shortcuts import render

from sponsors.models import Sponsor
from students.models import Student



from . import models, serializers as main_serializers


from rest_framework import viewsets, response, status, views, generics



class AgreementAPIViewSet(viewsets.ModelViewSet):
    
    queryset = models.Agreement.objects.all()
    serializer_class = main_serializers.AgreementSerializer
    
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class TotalAmount(views.APIView):
    
    def get(self, request, *args, **kwargs):
        if Sponsor.objects.all():
            total_amount = sum(list(map(lambda dct: dct[0], Sponsor.objects.all().values_list('payment_amount'))))
        
        else:
            total_amount = 0
        
        return response.Response({'total_amount': total_amount}, status=status.HTTP_200_OK)    


class TotalAmountNeeded(views.APIView):
    
    
    def get(self, request, *args, **kwargs):
        total_amount_needed = sum(list(map(lambda dct: dct[0], Student.objects.all().values_list('univer__contract_amount'))))
        return response.Response({'total_amount_needed': total_amount_needed}, status=status.HTTP_200_OK)    


class TotalAmountDue(views.APIView):
    
    
    def get(self, request, *args, **kwargs):
        total_amount_needed = sum(list(map(lambda dct: dct[0], Student.objects.all().values_list('univer__contract_amount'))))
        amount_paid = sum(list(map(lambda dct: dct[0], Student.objects.all().values_list('allocated_amount'))))

        total_amount_due = total_amount_needed - amount_paid
        
        return response.Response({'total_amount_due': total_amount_due}, status=status.HTTP_200_OK)    