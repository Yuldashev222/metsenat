from django.urls import path, include, re_path

from . import routers, views



urlpatterns = [
    path('<str:year>/<str:month>/', views.FilterSponsorsInDateAPIView.as_view({'get': 'list'})),
    path('count/', views.CountSponsors.as_view({'get': 'list'})),
    path('', include(routers.SPONSOR_CRUD_ROUTER.urls)),
]
