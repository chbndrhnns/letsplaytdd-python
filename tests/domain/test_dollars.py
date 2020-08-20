from finances.domain.dollars import Dollars


class TestOperations:
    def test_addition(self):
        assert Dollars(10) + Dollars(30) == Dollars(40)

    def test_subtraction(self):
        assert Dollars(10) + Dollars(30) == Dollars(40)
        assert Dollars(10) - Dollars(40) == Dollars(-30)

    def test_subtract_to_zero(self):
        assert Dollars(10).subtract_to_zero(Dollars(5)) == Dollars(5)
        assert Dollars(10).subtract_to_zero(Dollars(40)) == Dollars(0)

    def test_to_int(self):
        assert int(Dollars(10)) == 10


class TestDollarValueObject:
    def test_equality(self):
        dollars1a = Dollars(1)
        dollars1b = Dollars(1)
        dollars2 = Dollars(2)

        assert dollars1a == dollars1b
        assert dollars1a is not None
        assert dollars1a == dollars1a

        assert dollars1a != dollars2

    def test_string(self):
        dollars1a = Dollars(1)
        dollars1b = Dollars(1)
        dollars2 = Dollars(2)

        assert str(dollars1a) == str(dollars1b)
        assert str(dollars1a) != str(dollars2)
