from django.contrib import admin
from django.urls import path, include

from . import routers, views



urlpatterns = [
    path('students/count/', views.CountStudents.as_view({'get': 'list'})),
    path('students/', include(routers.STUDENT_CRUD_ROUTER.urls)),
    path('univers/count/', views.CountUnivers.as_view({'get': 'list'})),
    path('univers/', include(routers.UNIVER_CRUD_ROUTER.urls)),
]
