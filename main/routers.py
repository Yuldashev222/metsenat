from rest_framework import routers

from . import views, models



AGREEMENT_CRUD_ROUTER = routers.SimpleRouter()
AGREEMENT_CRUD_ROUTER.register('', views.AgreementAPIViewSet)


ADMIN_CRUD_ROUTER = routers.SimpleRouter()
ADMIN_CRUD_ROUTER.register('', views.AdminAPIViewSet)