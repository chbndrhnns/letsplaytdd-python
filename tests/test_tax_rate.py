class TaxRate:
    def __init__(self, rate_as_percentage: float):
        self._rate: float = rate_as_percentage / 100.0

    def tax_for(self, amount: int):
        return int(amount * self._rate)


class TestTaxRate:
    def test_zero_rate(self):
        rate = TaxRate(0)
        assert rate.tax_for(1000) == 0

    def test_simple_tax(self):
        rate = TaxRate(25)
        assert rate.tax_for(1000) == 250
