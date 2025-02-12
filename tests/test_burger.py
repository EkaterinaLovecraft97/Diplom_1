import pytest
import allure
from conftest import mock_bun
from praktikum.burger import Burger
from data import Data1, Data2

@allure.suite('Тесты для сборки бургера')
class TestBurger:

    @allure.title('Добавление булки в бургер')
    def test_set_buns_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, "Булка не была добавлена в бургер"

    @allure.title('Добавление ингредиентов в бургер')
    @pytest.mark.parametrize(
        'ingredient_data',
        [
            {"name": Data1.sauce_name, "type": Data1.sauce_type, "price": Data1.sauce_price},
            {"name": Data2.filling_name, "type": Data2.filling_type, "price": Data2.filling_price}
        ]
    )
    def test_add_ingredient_success(self, ingredient_data):
        burger = Burger()
        mock_ingredient = self._create_mock_ingredient(ingredient_data)
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient], "Ингредиент не добавлен или добавлен некорректно"

    @allure.title('Удаление ингредиента из бургера')
    def test_remove_ingredient_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_bun)  # Булка добавлена как тестовый ингредиент
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0, "Ингредиент не был удалён"

    @allure.title('Перемещение ингредиентов внутри бургера')
    def test_move_ingredient_success(self, mock_bun):
        burger = Burger()
        burger.add_ingredient(mock_bun)
        burger.add_ingredient(mock_bun)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_bun, "Ингредиенты не были перемещены корректно"

    @allure.title('Проверка стоимости бургера')
    def test_get_price_burger_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == mock_bun.get_price() * 2, "Стоимость бургера рассчитана некорректно"

    @staticmethod
    def _create_mock_ingredient(data):
        from unittest.mock import Mock
        mock = Mock()
        mock.get_name.return_value = data["name"]
        mock.get_type.return_value = data["type"]
        mock.get_price.return_value = data["price"]
        return mock