from django.urls import (
    path,
    include
)
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
