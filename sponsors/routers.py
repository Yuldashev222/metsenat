from rest_framework import routers

from . import views, models


SPONSOR_CRUD_ROUTER = routers.SimpleRouter()

SPONSOR_CRUD_ROUTER.register('', views.SponsorAPIViewSet)