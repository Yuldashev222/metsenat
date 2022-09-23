from django.shortcuts import render

from datetime import datetime, timedelta

from . import models, serializers as sponsor_serializers, enums
from django_filters import rest_framework as rest_filters, NumberFilter

from rest_framework import viewsets, response, status, views, generics, serializers, filters


class SponsorDateFilter(rest_filters.FilterSet):
    year = NumberFilter(field_name='date_created', lookup_expr="year")
    month = NumberFilter(field_name='date_created', lookup_expr="month")
    day = NumberFilter(field_name='date_created', lookup_expr="day")

    class Meta:
        model = models.Sponsor
        fields = ('date_created',)


class SponsorAPIViewSet(viewsets.ModelViewSet):
    
    queryset = models.Sponsor.objects.all()
    serializer_class = sponsor_serializers.SponsorSerializer
    filterset_class = SponsorDateFilter
    
    def create(self, request, *args, **kwargs):
        sponsor_type = request.data.get('type')
        organization = request.data.get('organization')
        if sponsor_type == enums.SponsorType.y.name and not organization:
            return response.Response(data={'organization': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
    

class CountSponsors(views.APIView):


    def get(self, request, *args, **kwargs):
        cnt = models.Sponsor.objects.all().count()
        return response.Response({'count': cnt}, status=status.HTTP_200_OK)    




class FilterSponsorsInDateAPIView(views.APIView):


    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')

        if len(year) != 4 or len(month) != 2:
            return response.Response(data={'year or month': 'length error'})

        else:
            try:
                year = int(year)
                month = int(month)
                result = models.Sponsor.objects.filter(date_created__year=year, date_created__month=month).values()
                return response.Response(data={'sponsors': list(result)})
            except:
                return response.Response(data={'year or month': 'None type int'})
        

