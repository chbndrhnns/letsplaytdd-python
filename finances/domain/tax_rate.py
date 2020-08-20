from finances.domain.base_class import FinanceBase
from finances.domain.dollars import Dollars


class TaxRate(FinanceBase):
    def __init__(self, rate_as_percentage: float):
        assert rate_as_percentage > 0, f'Tax rate must be positive, non-zero. Got: {rate_as_percentage}'
        self._rate_as_percentage: float = rate_as_percentage

    def simple_tax_for(self, amount: Dollars) -> Dollars:
        return amount.percentage(self._rate_as_percentage)

    def compound_tax_for(self, amount: Dollars) -> Dollars:
        compound_rate = (100.0 / (100.0 - self._rate_as_percentage))
        return amount.percentage(compound_rate * 100.0)

    def __eq__(self, other):
        if isinstance(other, TaxRate):
            return self._rate_as_percentage == other._rate_as_percentage
        return False

    def __str__(self):
        return f'{int(self._rate_as_percentage)} %'
