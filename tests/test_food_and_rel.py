import pytest


@pytest.mark.django_db(transaction=True)
class TestFoodRelAPI:

    api_url = "/api/v1/foods/"

    def test_get_food_additional(
        self,
        client,
        first_category,
        second_category,
        first_food_first_category,
        first_food_second_category,
        second_food_second_category,
        second_food_first_category
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

        foods_first_category = json_first_category['foods']
        foods_second_category = json_second_category['foods']

        assert len(foods_first_category) == 2, (
            "Проверь, что при создании FoodRel попадают только объекты "
            " указаной категории"
        )

        assert len(foods_second_category) == 2, (
            "Проверь, что при создании FoodRel попадают только объекты "
            " указаной категории"
        )

        check_i_code_objs = {
            foods_first_category[0]['internal_code']: first_food_first_category.internal_code,
            foods_first_category[1]['internal_code']: second_food_first_category.internal_code,
            foods_second_category[0]['internal_code']: first_food_second_category.internal_code,
            foods_second_category[1]['internal_code']: second_food_second_category.internal_code,
        }

        for key, val in check_i_code_objs.items():

            assert key == val, (
                "Проверь, что internal_code объектов не изменяется"
            )
        
        check_additional_objs = {
            tuple(foods_first_category[0]['additional']): (),
            tuple(foods_first_category[1]['additional']): (10, 20, 25),
            tuple(foods_second_category[0]['additional']): (10,),
            tuple(foods_second_category[1]['additional']): (10, 20),
        }

        for key, val in check_additional_objs.items():

            assert key == val, (
                "Проверь, что additional объектов не изменяется"
            )
