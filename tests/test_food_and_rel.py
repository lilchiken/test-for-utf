"""Проверка отображения "additional" и в целом "foods"."""

import pytest


@pytest.mark.django_db(transaction=True)
class TestFoodRelAPI:

    api_url = "/api/v1/foods/"

    def test_get_food_additional(
        self,
        client,
        first_category,
        second_category,
        f_food_f_category,
        f_food_s_category,
        s_food_s_category,
        s_food_f_category
    ):

        response = client.get(self.api_url)
        json = response.json()

        assert len(json) == 2, (
            "Проверь, что при создании FoodRel не "
            "создаётся дополнительных категорий"
        )

        json_first_category = json[0]
        json_second_category = json[1]

        assert json_first_category.get("foods"), (
            "Проверь, что при создании FoodRel объекты не пропадают из foods"
        )

        assert json_second_category.get("foods"), (
            "Проверь, что при создании FoodRel объекты не пропадают из foods"
        )

        fs_f_ctgr = json_first_category['foods']
        fs_s_ctgr = json_second_category['foods']

        assert len(fs_f_ctgr) == 2, (
            "Проверь, что при создании FoodRel попадают только объекты "
            " указаной категории"
        )

        assert len(fs_s_ctgr) == 2, (
            "Проверь, что при создании FoodRel попадают только объекты "
            " указаной категории"
        )

        check_i_code_objs = {
            fs_f_ctgr[0]['internal_code']: f_food_f_category.internal_code,
            fs_f_ctgr[1]['internal_code']: s_food_f_category.internal_code,
            fs_s_ctgr[0]['internal_code']: f_food_s_category.internal_code,
            fs_s_ctgr[1]['internal_code']: s_food_s_category.internal_code,
        }

        for key, val in check_i_code_objs.items():

            assert key == val, (
                "Проверь, что internal_code объектов не изменяется"
            )

        check_additional_objs = {
            tuple(fs_f_ctgr[0]['additional']): (),
            tuple(fs_f_ctgr[1]['additional']): (10, 20, 25),
            tuple(fs_s_ctgr[0]['additional']): (10,),
            tuple(fs_s_ctgr[1]['additional']): (10, 20),
        }

        for key, val in check_additional_objs.items():

            assert key == val, (
                "Проверь, что additional объектов не изменяется"
            )
