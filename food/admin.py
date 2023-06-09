from django.contrib import admin

from food.models import (
    Food,
    FoodCategory
)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'is_publish',)
    list_editable = ('is_publish',)
    search_fields = ('name_ru',)
    empty_value_display = '-'


@admin.register(FoodCategory)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'order_id',)
    list_editable = ('order_id',)
    search_fields = ('name_ru',)
    empty_value_display = '-'
