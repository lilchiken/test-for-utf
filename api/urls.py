from django.urls import (
    path,
    include
)
from rest_framework import routers

from api.views import FoodCategoryViewSet

v1_router = routers.DefaultRouter()
v1_router.register('foods', FoodCategoryViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]