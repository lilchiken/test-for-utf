from http import HTTPStatus

import pytest


@pytest.mark.django_db
class TestAPI:

    api_url = "/api/v1/foods/"
    methods_not_allowed = ('post', 'put', 'patch', 'delete')

    def test_foods_get(self, client):

        response = client.get(self.api_url)

        assert response.status_code == HTTPStatus.OK, (
            "Нет такого эндпойнта '{}'".format(self.api_url)
        )

        assert isinstance(response.json(), list), (
            "Корень ответа должен быть в формате list"
        )

        assert len(response.json()) == 0, (
            "Содержит объекты, которых не должно быть"
            "(должен быть пустой list)"
        )

    @pytest.mark.parametrize('http_method', methods_not_allowed)
    def test_foods_not_allowed_methods(self, client, http_method):

        request_func = getattr(client, http_method)
        response = request_func(self.api_url)

        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            "Только методы GET, HEAD, OPTIONS должны быть доступны на "
            "эндпойнт {}".format(self.api_url)
        )
