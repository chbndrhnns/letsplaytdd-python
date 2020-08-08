from finances.dollar import Dollar


class TestOperations:
    def test_addition(self):
        assert Dollar(10) + Dollar(30) == Dollar(40)

    def test_subtraction(self):
        assert Dollar(10) + Dollar(30) == Dollar(40)
        assert Dollar(10) - Dollar(40) == Dollar(-30)

    def test_subtract_to_zero(self):
        assert Dollar(10).subtract_to_zero(Dollar(5)) == Dollar(5)
        assert Dollar(10).subtract_to_zero(Dollar(40)) == Dollar(0)


class TestDollarValueObject:
    def test_equality(self):
        dollar1a = Dollar(1)
        dollar1b = Dollar(1)
        dollar2 = Dollar(2)

        assert dollar1a == dollar1b
        assert dollar1a is not None
        assert dollar1a == dollar1a

        assert dollar1a != dollar2

    def test_string(self):
        dollar1a = Dollar(1)
        dollar1b = Dollar(1)
        dollar2 = Dollar(2)

        assert str(dollar1a) == str(dollar1b)
        assert str(dollar1a) != str(dollar2)
