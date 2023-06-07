from rest_framework import serializers

from food.models import (
    Food,
    FoodCategory
)


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='internal_code'
    )

    class Meta:
        model = Food
        fields = '__all__'

class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(
        source='food',
        many=True,
        read_only=True
    )

    class Meta:
        model = FoodCategory
        fields = '__all__'
