from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import urls as api_urls
# from frontend import urls

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path(r'api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', include(urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
