from conftest import mock_sauce, mock_filling
import pytest
import allure

@allure.suite('Тесты для ингредиентов')
class TestIngredient:

    @allure.title('Получение имени соуса')
    def test_get_name_sauce_success(self, mock_sauce):
        assert mock_sauce.get_name() == "Соус Империи", "Имя соуса не совпадает с ожидаемым"

    @allure.title('Получение имени начинки')
    def test_get_name_filling_success(self, mock_filling):
        assert mock_filling.get_name() == "Филе лунного краба", "Имя начинки не совпадает с ожидаемым"

    @allure.title('Получение цены соуса')
    def test_get_price_sauce_success(self, mock_sauce):
        assert mock_sauce.get_price() == 55, "Цена соуса не совпадает с ожидаемой"

    @allure.title('Получение цены начинки')
    def test_get_price_filling_success(self, mock_filling):
        assert mock_filling.get_price() == 750, "Цена начинки не совпадает с ожидаемой"

    @allure.title('Получение типа соуса')
    def test_get_type_sauce_success(self, mock_sauce):
        assert mock_sauce.get_type() == "sauce", "Тип соуса не совпадает с ожидаемым"

    @allure.title('Получение типа начинки')
    def test_get_type_filling_success(self, mock_filling):
        assert mock_filling.get_type() == "filling", "Тип начинки не совпадает с ожидаемым"