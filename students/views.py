from django.shortcuts import render


from . import models, serializers as sponsor_serializers, enums, services


from rest_framework import viewsets, response, status


class StudentAPIViewSet(viewsets.ModelViewSet):
    
    queryset = models.Student.objects.all()
    serializer_class = sponsor_serializers.StudentSerializer
    
    

class UniverAPIViewSet(viewsets.ModelViewSet):
    
    queryset = models.Univer.objects.all()
    serializer_class = sponsor_serializers.UniverSerializer



class CountStudents(viewsets.ViewSet):


    def list(self, request):
        cnt = models.Student.objects.all().count()
        return response.Response({'count': cnt}, status=status.HTTP_200_OK)    
    



class CountUnivers(viewsets.ViewSet):


    def list(self, request):
        cnt = models.Univer.objects.all().count()
        return response.Response({'count': cnt}, status=status.HTTP_200_OK)    
    