from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from main.views import TotalAmount, TotalAmountNeeded, TotalAmountDue
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
schema_view = get_schema_view(
    openapi.Info(
        title="UIC API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    
    path('sponsors/', include('sponsors.urls')),
    path('agreements/', include('main.urls')),
    path('', include('students.urls')),
    
    
    path('total-amount/', TotalAmount.as_view({'get': 'list'})),
    path('total-amount-needed/', TotalAmountNeeded.as_view({'get': 'list'})),
    path('amount-due/', TotalAmountDue.as_view({'get': 'list'})),

    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
