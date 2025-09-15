import pytest 
from praktikum.bun import Bun

from data import TestDataBun

class TestBun: 

    
    @pytest.mark.parametrize('buns', [TestDataBun.Bun_0, TestDataBun.Bun_1])
    def test_get_name_bun(self, buns):
        
        bun = buns
    
        assert bun.get_name() == bun.name

  
    @pytest.mark.parametrize('buns', [TestDataBun.Bun_0, TestDataBun.Bun_1])
    def test_get_price_bun(self, buns):
        
        bun = buns
        
        assert bun.get_price() == bun.price




