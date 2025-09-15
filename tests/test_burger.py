
import pytest 
from unittest.mock import Mock
from praktikum.burger import Burger
from data import TestDataBun, TestDataIngredient


class TestBurger:

    def test_set_bun(self):

        mock_bun = Mock()
        mock_bun = TestDataBun.Bun_0
        
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient(self):

        mock_ingredients = Mock()
        mock_ingredients = TestDataIngredient.ingredient_1

        burger = Burger()
        burger.add_ingredient(mock_ingredients)

        assert burger.ingredients == [mock_ingredients]


    def test_remove_ingredient(self):
        
        mock_ingredients = Mock()
        mock_ingredients = TestDataIngredient.ingredient_0

        burger = Burger()
        burger.add_ingredient(mock_ingredients)
        burger.remove_ingredient(0)

        assert burger.ingredients == []


    def test_move_ingredient(self):

        mock_ingredients1 = Mock()
        mock_ingredients1 = TestDataIngredient.ingredient_0

        mock_ingredients2 = Mock()
        mock_ingredients2 = TestDataIngredient.ingredient_1

        burger = Burger()
        burger.add_ingredient(mock_ingredients1)
        burger.add_ingredient(mock_ingredients2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredients2, mock_ingredients1]


    def test_get_price_burger(self):

        mock_bun = Mock()
        mock_bun = TestDataBun.Bun_0

        mock_ingredients = Mock()
        mock_ingredients = TestDataIngredient.ingredient_0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients)

        expected_price = mock_bun.get_price() * 2
        for _ in burger.ingredients:
            expected_price += mock_ingredients.get_price()
        
        assert burger.get_price() == expected_price


    def test_get_receipt(self):

        mock_bun = Mock()
        mock_bun = TestDataBun.Bun_1

        mock_ingredients = Mock()
        mock_ingredients = TestDataIngredient.ingredient_1

        burger = Burger()

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients)

        expected_receipt = ('(==== white bun ====)\n'
                            '= filling sausage =\n'
                            '(==== white bun ====)\n'
                            '\nPrice: 701.8')
        
        assert burger.get_receipt() == expected_receipt







    
    