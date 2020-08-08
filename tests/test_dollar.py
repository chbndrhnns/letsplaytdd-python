from finances.dollar import Dollar


class TestDollarValueObject:
    def test_equality(self):
        dollar1a = Dollar(1)
        dollar1b = Dollar(1)
        dollar2 = Dollar(2)

        assert dollar1a == dollar1b
        assert dollar1a != dollar2

    def test_string(self):
        dollar1a = Dollar(1)
        dollar1b = Dollar(1)
        dollar2 = Dollar(2)

        assert str(dollar1a) == str(dollar1b)
        assert str(dollar1a) != str(dollar2)
