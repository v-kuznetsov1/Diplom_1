import pytest 
from praktikum.database import Database
from data import TestDataDataBase

class TestDataBase:

    def test_available_buns(self):

        database = Database()
        available_buns = database.available_buns()
        actual_result = [bun.get_name() for bun in available_buns]
        
        assert TestDataDataBase.expected_buns == actual_result
        

    def test_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        actual_result = [ingredient.get_name() for ingredient in available_ingredients]

        assert TestDataDataBase.expected_ingredients == actual_result

