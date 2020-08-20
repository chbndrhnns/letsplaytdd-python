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

    def test_percentage(self):
        assert Dollars(20) == Dollars(100).percentage(20)
        assert Dollars(4) == Dollars(9).percentage(50)

    def test_equals_ignores_pennies(self):
        assert Dollars(10) == Dollars(10.1), 'should round down'
        assert Dollars(10) == Dollars(9.90), 'should round up'
        assert Dollars(10) == Dollars(10.5), 'should round down'
        assert Dollars(12) == Dollars(11.5), 'should round up'

    def test_to_string_ignores_pennies(self):
        assert str(Dollars(10.1)) == "$10.00", 'should round down'
        assert str(Dollars(9.9)) == "$10.00", 'should round up'
        assert str(Dollars(10.5)) == "$10.00", 'should round down'
        assert str(Dollars(11.5)) == "$12.00", 'should round up'


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

    def test_hash(self):
        dollars1a = Dollars(1)
        dollars1b = Dollars(1)
        dollars2 = Dollars(2)

        assert hash(dollars1a) == hash(dollars1b)
        assert hash(dollars1a) != hash(dollars2)
