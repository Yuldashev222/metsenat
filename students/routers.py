from rest_framework import routers

from . import views, models


STUDENT_CRUD_ROUTER = routers.SimpleRouter()
STUDENT_CRUD_ROUTER.register('', views.StudentAPIViewSet)

UNIVER_CRUD_ROUTER = routers.SimpleRouter()
UNIVER_CRUD_ROUTER.register('', views.UniverAPIViewSet)