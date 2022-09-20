from django.urls import path, include, re_path

from . import routers, views



urlpatterns = [
    path('<str:year>/<str:month>/', views.FilterSponsorsInDateAPIView.as_view()),
    path('count/', views.CountSponsors.as_view()),
    path('', include(routers.SPONSOR_CRUD_ROUTER.urls)),
]
