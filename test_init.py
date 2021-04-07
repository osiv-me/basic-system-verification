from datachecker import DataChecker
from unittest.mock import patch
from unittest import mock
import sqlite3


class Mock:
    def cursor(self):
        return True

class TestClass:
    @mock.patch('sqlite3.connect')
    def test___init__(self, mock):
        sqlite3.connect.return_value = Mock()
        DataChecker.__init__(self)
        assert self.cursor == True
        assert self.conn != None 