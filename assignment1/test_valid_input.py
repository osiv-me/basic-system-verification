from datachecker import DataChecker


class TestClassValidTextField:
    def test_passing_string(self):
        assert DataChecker.check_valid_text_field(
            self, "RandomText", False) == True

    def test_passing_empty_string(self):
        assert DataChecker.check_valid_text_field(self, "", False) == False

    def test_passing_string_empty_not_allowed(self):
        assert DataChecker.check_valid_text_field(
            self, "RandomText", True) == True

    def test_passing_empty_string_empty_not_allowed(self):
        assert DataChecker.check_valid_text_field(self, "", True) == True

    def test_passing_other_than_string(self):
        assert DataChecker.check_valid_text_field(self, [1, 1, 1]) == False
