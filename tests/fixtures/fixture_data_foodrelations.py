"""Фикстуры для тестов отображения объектов Food & FoodRelationship ."""

import pytest

from food.models import(
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
def first_food_first_category(first_category):
    return Food.objects.create(
        category=first_category,
        name_ru="first food in first category",
        code=10,
        internal_code=10
    )


@pytest.fixture
def first_food_second_category(second_category, first_food_first_category):
    obj = Food.objects.create(
        category=second_category,
        name_ru=(
            "first food in second category with"
            " rel on first food in first category"
        ),
        code=20,
        internal_code=20
    )
    obj.additional.add(first_food_first_category)
    return obj


@pytest.fixture
def second_food_second_category(
    second_category,
    first_food_first_category,
    first_food_second_category
):
    obj = Food.objects.create(
        category=second_category,
        name_ru=(
            "first food in second category with"
            " rel on first food in first category"
            " and first food in second category"
        ),
        code=25,
        internal_code=25
    )
    obj.additional.add(first_food_first_category)
    obj.additional.add(first_food_second_category)
    return obj


@pytest.fixture
def second_food_first_category(
    second_category,
    first_food_first_category,
    first_food_second_category,
    second_food_second_category
):
    obj = Food.objects.create(
        category=second_category,
        name_ru=(
            "first food in first category with"
            " rel on first food in first category"
            " and first food in second category"
            " and second food in second category"
        ),
        code=15,
        internal_code=15
    )
    obj.additional.add(first_food_first_category)
    obj.additional.add(first_food_second_category)
    obj.additional.add(second_food_second_category)
    return obj
