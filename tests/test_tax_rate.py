import pytest


class TaxRate:
    def __init__(self, rate_as_percentage: float):
        self._rate: float = rate_as_percentage / 100.0

    def simple_tax_for(self, amount: int):
        return int(amount * self._rate)

    def compound_tax_for(self, amount: int):
        return int(amount / (1 - self._rate) - amount)


class TestTaxRate:
    @pytest.mark.parametrize(
        'rate, amount, expected', [
            (0, 1000, 0),
            (25, 1000, 250),
            # (25, 10, 2.5)
        ]
    )
    def test_simple_tax_is_applied_to_amount(self, rate, amount, expected):
        rate = TaxRate(rate)
        assert rate.simple_tax_for(amount) == expected

    def test_compound_tax_includes_tax_on_tax(self):
        rate = TaxRate(25)
        assert rate.compound_tax_for(1000) == 333
