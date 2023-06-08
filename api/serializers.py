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
        exclude = ( 'created', 'modified', 'category', 'id') # 'is_publish',


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(
        source='food',
        many=True,
        read_only=True
    )

    class Meta:
        model = FoodCategory
        exclude = ('created', 'modified')
