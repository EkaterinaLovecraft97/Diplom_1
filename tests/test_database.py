from data import TestDataBase
from conftest import db
import pytest
import allure

@allure.suite('Тесты для базы данных ингредиентов')
class TestDB:

    @allure.title('Получение списка доступных булок из базы')
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.test_data_base_buns)
    def test_available_buns_db_success(self, db, index_bun, bun_name, bun_price):
        data_buns = db.available_buns()
        assert data_buns[index_bun].get_name() == bun_name, f"Некорректное имя булки с индексом {index_bun}"
        assert data_buns[index_bun].get_price() == bun_price, f"Некорректная стоимость булки с индексом {index_bun}"

    @allure.title('Получение списка доступных ингредиентов из базы')
    @pytest.mark.parametrize(
        'index_i, type_ingredient, name_ingredient, price_ingredient',
        TestDataBase.test_data_base_ingredients
    )
    def test_available_ingredients_db_success(self, db, index_i, type_ingredient, name_ingredient, price_ingredient):
        data_ingredients = db.available_ingredients()
        assert data_ingredients[index_i].get_name() == name_ingredient, f"Ошибка имени ингредиента с индексом {index_i}"
        assert data_ingredients[index_i].get_type() == type_ingredient, f"Ошибка типа ингредиента с индексом {index_i}"
        assert data_ingredients[index_i].get_price() == price_ingredient, f"Ошибка цены ингредиента с индексом {index_i}"