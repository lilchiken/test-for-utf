from django.contrib import admin

from food.models import (
    Food,
    FoodCategory
)
from food.models.food import FoodRelationship


class FoodAdditionalAdminInline(admin.TabularInline):
    model = FoodRelationship
    fk_name = "frm"
    verbose_name = "Additional"
    verbose_name_plural = "Additional"


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'is_publish')
    list_editable = ('is_publish',)
    search_fields = ('name_ru',)
    empty_value_display = '-'
    inlines = (FoodAdditionalAdminInline,)


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'order_id',)
    list_editable = ('order_id',)
    search_fields = ('name_ru',)
    empty_value_display = '-'
