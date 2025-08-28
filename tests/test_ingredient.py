import pytest
from praktikum.ingredient import Ingredient
from data import TestDataIngredient

class TestIngredient:


    @pytest.mark.parametrize('ingredients', [TestDataIngredient.ingredient_0, 
                                             TestDataIngredient.ingredient_1])
    def test_get_price_ingredient(self, ingredients):
        
        ingredient = ingredients
        assert ingredient.get_price() == ingredient.price

    
    @pytest.mark.parametrize('ingredients', [TestDataIngredient.ingredient_0,
                                             TestDataIngredient.ingredient_1])
    def test_get_name_ingredient(self, ingredients):
        
        ingredient = ingredients
        assert ingredient.get_name() == ingredient.name

    
    @pytest.mark.parametrize('ingredients', [TestDataIngredient.ingredient_1,
                                             TestDataIngredient.ingredient_0])
    def test_get_type_ingredient(self, ingredients):
        
        ingredient = ingredients
        assert ingredient.get_type() == ingredient.type



    