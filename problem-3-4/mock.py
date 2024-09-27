
import main
from unittest.mock import patch,MagicMock
from unittest import TestCase

main.password= MagicMock(return_value=True)
main.password("Estela150697+", True, key='value')

main.nickname= MagicMock(return_value=True)
main.nickname("estela", True, key='value')

main.isadmin= MagicMock(return_value=True)
main.isadmin("y", True,True, key='value')

main.password.assert_called_with("Estela150697+", True, key='value')

class TestPaswword(TestCase):
    @patch('main.password', return_value=True)
    def test_password(self, password):
        self.assertEqual(main.password("Estela150697+"), True)


class Testnickname(TestCase):
    @patch('main.nickname', return_value=True)
    def test_nickname(self, nickname):
        self.assertEqual(main.nickname("estela"), True)

class Testisadmin(TestCase):
    @patch('main.isadmin', return_value= True)
    def test_isadmin(self, isadmin):
        self.assertEqual(main.isadmin("y"), True,True)