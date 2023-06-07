from django.db import models

from food.models.foodcategory import FoodCategory
from core.models import NamedTimeStampedModel
from core.fields import (
    CustomCharField,
    NamedCharField
)


class Food(NamedTimeStampedModel):
    category = models.ForeignKey(
        FoodCategory,
        verbose_name='Раздел меню',
        related_name='food',
        on_delete=models.CASCADE
    )

    is_vegan = models.BooleanField(
        verbose_name='Вегетарианское меню',
        default=False
    )
    is_special = models.BooleanField(
        verbose_name='Специальное предложение',
        default=False
    )

    code = models.IntegerField(
        verbose_name='Код поставщика'
    )
    internal_code = models.IntegerField(
        verbose_name='Код в приложении',
        unique=True,
        null=True,
        blank=True
    )

    cost = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2
    )

    is_publish = models.BooleanField(
        verbose_name='Опубликовано',
        default=True
    )

    name_ru = NamedCharField()
    description_ru = CustomCharField(verbose_name='Описание на русском')
    description_en = CustomCharField(verbose_name='Описание на английском')
    description_ch = CustomCharField(verbose_name='Описание на китайском')

    additional = models.ManyToManyField(
        'self',
        verbose_name='Дополнительные товары',
        symmetrical=False,
        related_name='additional_from',
        blank=True
    )
