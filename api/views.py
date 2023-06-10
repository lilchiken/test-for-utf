from django.db.models import Prefetch
from django.conf import settings
from rest_framework import permissions
from rest_framework.response import Response

from api.serializers import FoodListSerializer
from api.mixins import ListModelViewSet
from food.models import (
    Food,
    FoodCategory
)

if settings.RAW_QUERY:
    from core.utils import QUERY_LIST_FOOD


class FoodCategoryViewSet(ListModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        query_food_additional = Food.objects.only(
            'id',
            'internal_code'
        ).filter(
            is_publish=True,
            internal_code__isnull=False
        ).order_by('id')

        query_food = Food.objects.prefetch_related(
            Prefetch(
                'additional',
                queryset=query_food_additional
            )
        ).defer(*settings.DEFER_FIELDS, 'is_publish').filter(
            is_publish=True
        ).order_by('id')

        queryset = FoodCategory.objects.prefetch_related(
            Prefetch(
                'food',
                queryset=query_food,
            )
        ).defer(*settings.DEFER_FIELDS).filter(
            food__is_publish=True
        ).distinct().order_by('id')

        return queryset


if settings.RAW_QUERY:

    class FoodCategoryViewSet(FoodCategoryViewSet):

        def get_queryset(self):
            queryset = set(
                FoodCategory.objects.raw(
                    QUERY_LIST_FOOD
                )
            )

            return queryset
        
        def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()

            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

            data = [d for d in data if len(d['foods']) > 0]

            return Response(data)
