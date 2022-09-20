from django.urls import path, include

from . import routers, views



urlpatterns = [
    path('', include(routers.AGREEMENT_CRUD_ROUTER.urls)),
]
