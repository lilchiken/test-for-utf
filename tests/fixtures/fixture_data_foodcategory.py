"""Фикстуры для тестов отображения FoodCategory & Food.is_publish ."""

import pytest

from food.models import (
    Food,
    FoodCategory
)


@pytest.fixture
def category_wo_foods():
    """Category without foods."""

    return FoodCategory.objects.create(name_ru="category w/o foods")


@pytest.fixture
def category_2f_2p():
    """Category with 2 foods and 2 publish."""

    return FoodCategory.objects.create(name_ru="category 2 foods 2 pub")


@pytest.fixture
def category_2f_1p():
    """Category with 2 foods and 1 publish."""

    return FoodCategory.objects.create(name_ru="category 2 foods 1 pub")


@pytest.fixture
def category_1f_0p():
    """Category with 1 foods and 0 publish."""

    return FoodCategory.objects.create(name_ru="category 1 food 0 pub")


@pytest.fixture
def first_f_for_2f_2p(category_2f_2p):
    """First food in category 2 foods and 2 publish."""

    return Food.objects.create(
        category=category_2f_2p,
        name_ru="first food for 2f 2p",
        code=1,
        internal_code=1,
        cost=1
    )


@pytest.fixture
def second_f_for_2f_2p(category_2f_2p):
    """First food in category 2 foods and 2 publish."""

    return Food.objects.create(
        category=category_2f_2p,
        name_ru="second food for 2f 2p",
        code=2,
        internal_code=2,
        cost=2
    )


@pytest.fixture
def first_f_for_2f_1p(category_2f_1p):
    """First food in category 2 foods and 1 publish (is_publish=True)."""

    return Food.objects.create(
        category=category_2f_1p,
        name_ru="first food for 2f 1p",
        code=3,
        internal_code=3,
        cost=3
    )


@pytest.fixture
def second_f_for_2f_1p(category_2f_1p):
    """First food in category 2 foods and 1 publish (is_publish=False)."""

    return Food.objects.create(
        category=category_2f_1p,
        name_ru="second food for 2f 1p",
        code=4,
        internal_code=4,
        is_publish=False,
        cost=4
    )


@pytest.fixture
def f_for_1f_0p(category_1f_0p):
    """First food in category 1 foods and 0 publish (is_publish=False)."""

    return Food.objects.create(
        category=category_1f_0p,
        name_ru="first food for 2f 1p",
        code=5,
        internal_code=5,
        is_publish=False,
        cost=5
    )
