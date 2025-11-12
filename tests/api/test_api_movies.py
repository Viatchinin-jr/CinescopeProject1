import pytest
import requests
from custom_requester.custom_requester import CustomRequester
from API.api_manager import ApiManager
from API.movies_api import MoviesAPI

class TestMoviesAPI:
    def test_get_all_movies(self, api_manager):
        response = api_manager.movies_api.get_list_movies()
        assert response.status_code == 200, "Ожидается статус код 200"

        # проверка структуры ответа
        body = response.json()
        assert isinstance(body, dict), "Ответ должен быть словарем"
        assert "movies" in body , "В ответе должно быть поле 'movies'"
        assert isinstance(body["movies"], list), "'movies' должен быть списком "

    def test_post_movie(self, api_manager, admin_auth, movie_payload):
        response = api_manager.movies_api.create_movie(movie_payload)
        assert response.status_code == 201
        body = response.json()
        assert body["name"] == movie_payload["name"]
        api_manager.movies_api.delete_movie(body["id"], expected_status=200)


    def test_get_by_id(self, api_manager):
        response = api_manager.movies_api.get_movie_by_id(1)
        assert response.status_code == 200, "Ожидается статус код 200"
        body = response.json()


    def test_delete_by_id(self, api_manager, admin_auth, movie_payload):
        # сначала создать фильм
        create_response = api_manager.movies_api.create_movie(movie_payload)
        assert create_response.status_code == 201, "Фильм не создался"
        created_movie = create_response.json()
        movie_id = created_movie["id"]

        # сам процесс удаления
        del_response = api_manager.movies_api.delete_movie(movie_id, expected_status=200)
        assert del_response.status_code == 200, "Фильм не удалился"

        body = del_response.json()
        assert body["id"] == movie_id, "ID удаленного фильма не совпадает"
        assert body["name"] == movie_payload["name"]

    def test_put_by_id(self, api_manager, admin_auth):

