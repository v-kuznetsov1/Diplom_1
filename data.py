
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDataBun: 
    
    buns_name = ['black bun', 'white bun', 'red bun']
    buns_price = [100.50, 200.99, 300.90]
    
    Bun_0 = Bun(buns_name[0], buns_price[1])
    Bun_1 = Bun(buns_name[1], buns_price[2])

class TestDataIngredient:

    ingredient_types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    sauce_name = ['hot sauce', 'sour cream', 'chili sauce']
    filling_name = ['cutlet', 'dinosaur', 'sausage']
    ingredient_price = [100, 200.99, 300.50]

    ingredient_0 = Ingredient(ingredient_types[0],
                              sauce_name[1],
                              ingredient_price[2])

    ingredient_1 = Ingredient(ingredient_types[1],
                              filling_name[2],
                              ingredient_price[0])
    

class TestDataDataBase:

    expected_buns = ['black bun', 'white bun', 'red bun']
    expected_ingredients = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]