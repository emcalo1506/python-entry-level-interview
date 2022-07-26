
import main
from unittest.mock import patch
from unittest import TestCase



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