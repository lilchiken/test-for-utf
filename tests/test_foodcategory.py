import pytest


@pytest.mark.django_db(transaction=True)
class TestFoodCategoryAPI:

    api_url = "/api/v1/foods/"

    def test_fields(self, client, category_2f_1p, first_f_for_2f_1p):

        fields_root = (
            "id",
            "name_ru",
            "name_en",
            "name_ch",
            "foods"
        )
        fields_foods = (
            "internal_code",
            "code",
            "name_ru",
            "description_ru",
            "description_en",
            "description_ch",
            "is_vegan",
            "is_special",
            "cost",
            "additional"
        )

        response = client.get(self.api_url)
        json = response.json()

        assert len(json) == 1, (
            "root JSON содержит объекты, которых не должно быть"
            "(должен быть list с одним объектом)"
        )

        category = json[0]

        assert category.keys() == dict.fromkeys(fields_root).keys(), (
            "Убедитесь, что foodcategory JSON response включает такие поля:\n"
            + ", ".join(fields_root)
        )

        assert len(category['foods']) == 1, (
            "foods JSON содержит объекты, которых не должно быть"
            "(должен быть list с одним объектом)"
        )

        food = category['foods'][0]

        assert food.keys() == dict.fromkeys(fields_foods).keys(), (
            "Убедитесь, что food JSON response включает такие поля:\n"
            + ", ".join(fields_foods)
        )

    def test_get_foodcategory_wo_foods(
        self,
        client,
        category_wo_foods
    ):

        response = client.get(self.api_url)

        assert len(response.json()) == 0, (
            "Убедитесь, что FoodCategory без Food не попадает в выдачу."
        )

    def test_get_foodcategory_with_1_unpub(
        self,
        client,
        category_1f_0p,
        f_for_1f_0p
    ):

        response = client.get(self.api_url)

        assert len(response.json()) == 0, (
            "Убедитесь, что FoodCategory без опубликованных Food не попадает в выдачу."
        )

    def test_get_foodcategory_with_1_pub_and_1_unpub(
        self,
        client,
        category_2f_1p,
        first_f_for_2f_1p,
        second_f_for_2f_1p
    ):

        response = client.get(self.api_url)
        json = response.json()

        assert len(json) == 1, (
            "root JSON содержит объекты, которых не должно быть"
            "(должен быть list с одним объектом)"
        )

        category = json[0]

        assert len(category['foods']) == 1, (
            "foods JSON содержит объекты, которых не должно быть"
            "(должен быть list с одним объектом, "
            "проверь флаг is_publish в выдаче)"
        )

    def test_get_foodcategory_with_2_pub(
        self,
        client,
        category_2f_2p,
        first_f_for_2f_2p,
        second_f_for_2f_2p
    ):

        response = client.get(self.api_url)
        json = response.json()

        assert len(json) == 1, (
            "root JSON содержит объекты, которых не должно быть"
            "(должен быть list с одним объектом)"
        )

        category = json[0]

        assert len(category['foods']) == 2, (
            "foods JSON содержит объекты, которых не должно быть"
            "(должен быть list с двумя объектами, "
            "проверь флаг is_publish в выдаче)"
        )
    
    def test_get_all_foodcategory(
        self,
        client,
        category_1f_0p,
        category_2f_1p,
        category_2f_2p,
        category_wo_foods,
        f_for_1f_0p,
        first_f_for_2f_1p,
        second_f_for_2f_1p,
        first_f_for_2f_2p,
        second_f_for_2f_2p
    ):
        
        response = client.get(self.api_url)
        json = response.json()
        
        assert len(json) == 2, (
            "Проверь, что в JSON попадают категории, у "
            "которых есть foods"
        )

        first_category = json[0]
        second_category = json[1]

        assert len(first_category['foods']) == 1, (
            "Проверь, что в JSON попадают категории, у "
            "которых есть foods"
        )

        assert len(second_category['foods']) == 2, (
            "Проверь, что в JSON попадают категории, у "
            "которых есть foods"
        )

        food_f_category_i_code = first_category['foods'][0]['internal_code']
        f_food_s_category_i_code = second_category['foods'][0]['internal_code']
        s_food_s_category_i_code = second_category['foods'][1]['internal_code']

        check_correct_objs = {
            first_f_for_2f_1p.internal_code: food_f_category_i_code,
            first_f_for_2f_2p.internal_code: f_food_s_category_i_code,
            second_f_for_2f_2p.internal_code: s_food_s_category_i_code,
        }

        for key, val in check_correct_objs.items():

            assert key == val, (
                "Проверь, что Food's правильно передаются в FoodCategory's."
            )
