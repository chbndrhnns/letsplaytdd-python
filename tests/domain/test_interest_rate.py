from finances.domain.dollars import Dollars
from finances.domain.interest_rate import InterestRate


class TestInterestRate:
    def test_interest(self):
        rate = InterestRate(10)
        assert rate.interest_on(Dollars(1000)) == Dollars(100)
        assert rate.interest_on(Dollars(1)) == Dollars(0)


class TestValueObject:
    def test_equals(self):
        rate1a = InterestRate(10)
        rate1b = InterestRate(10)
        rate2 = InterestRate(20)

        assert rate1a == rate1b
        assert rate1a != rate2

    def test_string(self):
        rate1a = InterestRate(10)
        rate1b = InterestRate(10)
        rate2 = InterestRate(20)

        assert str(rate1a) == str(rate1b)
        assert str(rate1a) != str(rate2)

    def test_repr(self):
        rate = InterestRate(10)

        assert repr(rate) == '10 %'

    def test_hash(self):
        rate1a = InterestRate(10)
        rate1b = InterestRate(10)
        rate2 = InterestRate(20)

        assert hash(rate1a) != hash(rate2)
        assert hash(rate1a) == hash(rate1b)
