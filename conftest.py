from praktikum.database import Database
from unittest.mock import Mock
from data import Data1, Data2
import pytest

@pytest.fixture
def mock_bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = Data1.bun_name
    bun_mock.get_price.return_value = Data1.bun_price
    return bun_mock

@pytest.fixture
def mock_bun_2():
    bun_mock_2 = Mock()
    bun_mock_2.get_name.return_value = Data2.bun_name
    bun_mock_2.get_price.return_value = Data2.bun_price
    return bun_mock_2

@pytest.fixture
def mock_ingredient(request):
    ingredient_mock = Mock()
    ingredient_mock.get_name.return_value = request.param.get('name')
    ingredient_mock.get_price.return_value = request.param.get('price')
    ingredient_mock.get_type.return_value = request.param.get('type')
    return ingredient_mock

@pytest.fixture
def mock_sauce():
    mock_for_sauce = Mock()
    mock_for_sauce.get_name.return_value = "Соус Империи"
    mock_for_sauce.get_price.return_value = 55
    mock_for_sauce.get_type.return_value = "sauce"
    return mock_for_sauce

@pytest.fixture
def mock_filling():
    mock_for_filling = Mock()
    mock_for_filling.get_name.return_value = "Филе лунного краба"
    mock_for_filling.get_price.return_value = 750
    mock_for_filling.get_type.return_value = "filling"
    return mock_for_filling

@pytest.fixture
def db():
    return Database()