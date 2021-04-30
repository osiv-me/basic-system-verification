from datachecker import DataChecker


class TestClass(object):
    def test_number(self):
        dc = DataChecker()
        assert dc.check_valid_age(10) == True

    def test_passing_other_than_int(self):
        dc = DataChecker()
        assert dc.check_valid_age('tio') == False

    def test_passing_negative_number(self):
        dc = DataChecker()
        assert dc.check_valid_age(-1) == False

    def test_passing_zero(self):
        dc = DataChecker()
        assert dc.check_valid_age(0) == True

    def test_passing_decimal(self):
        dc = DataChecker()
        assert dc.check_valid_age((7/5)) == True

    def test_passing_max_age(self):
        dc = DataChecker()
        assert dc.check_valid_age(201) == False

    def test_passing_boolean(self):
        dc = DataChecker()
        assert dc.check_valid_age(True) == False
