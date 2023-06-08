from django.db.models import Prefetch
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from food.models import (
    Food,
    FoodCategory
)
from api.serializers import (
    FoodListSerializer,
    FoodSerializer
)
from api.mixins import ListModelViewSet


class FoodCategoryViewSet(ListModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        query_food = Food.objects.prefetch_related(
            Prefetch(
                'additional',
                queryset=Food.objects.filter(is_publish=True)
            )
        ).filter(is_publish=True)

        queryset = FoodCategory.objects.prefetch_related(
            Prefetch(
                "food",
                queryset=query_food
                # to_attr='foods'
            )
        ).filter(food__is_publish=True).distinct().order_by('pk')

        # queryset = FoodCategory.objects.prefetch_related('food', 'food__additional').filter(
        #     food__is_publish=True
        # ).distinct().order_by('pk')

        return queryset


    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()

    #     serializer = self.get_serializer(queryset, many=True)
    #     data = serializer.data

    #     # Drop food categories without published food
    #     categories = [d for d in data if len(d['foods']) > 0]

    #     return Response(categories)
