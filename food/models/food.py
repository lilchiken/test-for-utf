from django.db import models

from food.models.foodcategory import FoodCategory
from core.models import NamedTimeStampedModel
from core.fields import (
    CustomCharField,
    NamedCharField
)


class FoodRelationship(models.Model):
    """Модель для связи m2m Food's."""

    frm = models.ForeignKey(
        "Food",
        on_delete=models.CASCADE,
        related_name='to_food_id',
        db_column='from_food_id',
    )
    to = models.ForeignKey(
        "Food",
        verbose_name='Дополнительные товары',
        on_delete=models.CASCADE,
        related_name='from_food_id',
        db_column='to_food_id',
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(frm=models.F("to")),
                name='self_additional'
            ),
            models.UniqueConstraint(
                fields=['frm', 'to'],
                name='unique_additional'
            )
        ]
        db_table = 'food_food_additional'

    def __str__(self) -> str:
        """Изменяем, чтобы в админке было более понятнее."""

        return self.to.name_ru


class Food(NamedTimeStampedModel):
    category = models.ForeignKey(
        FoodCategory,
        verbose_name='Раздел меню',
        related_name='food',
        on_delete=models.CASCADE
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

    is_vegan = models.BooleanField(
        verbose_name='Вегетарианское меню',
        default=False
    )
    is_special = models.BooleanField(
        verbose_name='Специальное предложение',
        default=False
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
        through=FoodRelationship,
        symmetrical=False,
        blank=True,
    )
