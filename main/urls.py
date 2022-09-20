from django.urls import path, include

from . import routers, views



urlpatterns = [
    # path('count/', views.AgreementAPIViewSet.as_view({'get': 'list'})),
    
    path('', include(routers.AGREEMENT_CRUD_ROUTER.urls)),
]
