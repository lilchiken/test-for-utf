from django.urls import (
    path,
    include
)
from django.conf import settings


urlpatterns = [
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
