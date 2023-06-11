"""Фикстуры для тестов отображения объектов Food & FoodRelationship ."""

import pytest

from food.models import (
    Food,
    FoodCategory
)


@pytest.fixture
def first_category():
    return FoodCategory.objects.create(name_ru="first category")


@pytest.fixture
def second_category():
    return FoodCategory.objects.create(name_ru="second category")


@pytest.fixture
def f_food_f_category(first_category):
    """First food in first category."""

    return Food.objects.create(
        category=first_category,
        name_ru="first food in first category",
        code=10,
        internal_code=10,
        cost=10
    )


@pytest.fixture
def f_food_s_category(second_category, f_food_f_category):
    """First food in second category."""

    obj = Food.objects.create(
        category=second_category,
        name_ru=(
            "first food in second category with"
            " rel on first food in first category"
        ),
        code=20,
        internal_code=20,
        cost=20
    )
    obj.additional.add(f_food_f_category)
    return obj


@pytest.fixture
def s_food_s_category(
    second_category,
    f_food_f_category,
    f_food_s_category
):
    """Second food in second category."""

    obj = Food.objects.create(
        category=second_category,
        name_ru=(
            "second food in second category with"
            " rel on first food in first category"
            " and first food in second category"
        ),
        code=25,
        internal_code=25,
        cost=25
    )
    obj.additional.add(f_food_f_category)
    obj.additional.add(f_food_s_category)
    return obj


@pytest.fixture
def s_food_f_category(
    first_category,
    f_food_f_category,
    f_food_s_category,
    s_food_s_category
):
    """Second food in first category."""

    obj = Food.objects.create(
        category=first_category,
        name_ru=(
            "second food in first category with"
            " rel on first food in first category"
            " and first food in second category"
            " and second food in second category"
        ),
        code=15,
        internal_code=15,
        cost=15
    )
    obj.additional.add(f_food_f_category)
    obj.additional.add(f_food_s_category)
    obj.additional.add(s_food_s_category)
    return obj
