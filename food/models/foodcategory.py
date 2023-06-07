from django.db import models

from core.models import NamedTimeStampedModel
from core.fields import (
    CustomCharField,
    NamedCharField
)


class FoodCategory(NamedTimeStampedModel):
    name_ru = NamedCharField(unique=True)

    name_en = CustomCharField(
        verbose_name='Название на английском',
        unique=True
    )
    name_ch = CustomCharField(
        verbose_name='Название на китайском',
        unique=True
    )
    order_id = models.SmallIntegerField(
        default=10,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Раздел меню'
        verbose_name_plural = 'Разделы меню'
        ordering = ('name_ru', 'order_id')
