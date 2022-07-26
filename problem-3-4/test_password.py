import pytest as pytest
from unittest.mock import MagicMock
from main import NewPerson

# @pytest.mark.parametrize(
#     "num1, num2,expected",
#     [(4,2,6)]
#     )
# # ,("wjsd3",False),("njbjdsbcBJDB",False)
# def test_password(num1,num2,expected):
#     assert suma(num1,num2) == expected

suma = MagicMock(return_value="no es correcta la suma")

#
# @pytest.mark.parametrize(
#     "aw,name, pwd,admin,expected",
#     [("r","estela","Estela150697+",True,True)]
#     )
# # ,("wjsd3",False),("njbjdsbcBJDB",False)
# def test_NewPerson(aw,name, pwd,admin,expected):
#     assert NewPerson(aw,name, pwd,admin) == expected