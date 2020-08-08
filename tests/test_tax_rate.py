import pytest

from finances.dollars import Dollars
from finances.tax_rate import TaxRate


class TestTaxRate:
    @pytest.mark.parametrize(
        'rate, amount, expected', [
            (0, Dollars(1000), Dollars(0)),
            (25, Dollars(1000), Dollars(250)),
            # (25, 10, 2.5)
        ]
    )
    def test_simple_tax_is_applied_to_amount(self, rate, amount, expected):
        rate = TaxRate(rate)
        assert rate.simple_tax_for(amount) == expected

    def test_compound_tax_includes_tax_on_tax(self):
        rate = TaxRate(25)
        assert rate.compound_tax_for(Dollars(1000)) == Dollars(333)

    def test_value_object(self):
        rate_1a = TaxRate(25)
        rate_1b = TaxRate(25)
        rate_2 = TaxRate(33)

        assert rate_1a == rate_1b
        assert rate_1a != rate_2

    def test_string(self):
        rate_1a = TaxRate(25)
        rate_1b = TaxRate(25)
        rate_2 = TaxRate(33)

        assert str(rate_1a) == '25 %'
        assert str(rate_1a) == str(rate_1b)
        assert str(rate_1a) != str(rate_2)
