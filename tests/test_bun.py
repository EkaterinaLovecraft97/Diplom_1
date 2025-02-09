import allure
from conftest import mock_bun, mock_bun_2

@allure.suite('Тесты для булок')
class TestBun:

    @allure.title('Получение названия первой булки')
    def test_get_name_bun_success(self, mock_bun):
        assert mock_bun.get_name() == 'Булка с маком Парадокс', "Название булки некорректное"

    @allure.title('Получение стоимости второй булки')
    def test_get_price_bun_success(self, mock_bun_2):
        assert mock_bun_2.get_price() == 1325, "Стоимость булки некорректная"