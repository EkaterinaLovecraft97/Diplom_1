from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class Data1:
    bun_name = 'Булка с маком Парадокс'
    bun_price = 945

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус Острый Вулкан'
    sauce_price = 45

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Вяленое мясо степных бизонов'
    filling_price = 1200

    burger_final_cost = bun_price * 2 + sauce_price + filling_price

class Data2:
    bun_name = 'Булка Туманного Альбиона'
    bun_price = 1325

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус Черничная Буря'
    sauce_price = 75

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Сыр "Альпийская прохлада"'
    filling_price = 3900

    burger_final_cost = bun_price * 2 + sauce_price + filling_price

class TestDataBase:
    test_data_base_buns = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

    test_data_base_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]
    ]