from django.db.models import Prefetch
from rest_framework import permissions
from rest_framework.response import Response

from api.serializers import FoodListSerializer
from api.mixins import ListModelViewSet
from food.models import (
    Food,
    FoodCategory
)
from core.utils.foodsquery import TRAIN_QUERY


DEFER_FIELDS = ('created', 'modified',)


class FoodCategoryViewSet(ListModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # query_food = Food.objects.prefetch_related(
        #     Prefetch(
        #         'additional',
        #         queryset=Food.objects.filter(
        #             is_publish=True
        #         ).order_by('pk').only(
        #             'internal_code'
        #         )
        #     )
        # ).defer(*DEFER_FIELDS).filter(is_publish=True).order_by('pk')

        # queryset = FoodCategory.objects.prefetch_related(
        #     Prefetch(
        #         'food',
        #         queryset=query_food,
        #     )
        # ).defer(*DEFER_FIELDS).filter(food__is_publish=True).distinct().order_by('pk')

        queryset = set(FoodCategory.objects.raw(
            TRAIN_QUERY
        ))

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # data = [d for d in data if len(d['foods']) > 0]

        return Response(data)
