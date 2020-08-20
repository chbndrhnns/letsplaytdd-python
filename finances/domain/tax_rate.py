from finances.domain.base_class import FinanceBase
from finances.domain.dollars import Dollars


class TaxRate(FinanceBase):
    def __init__(self, rate_as_percentage: float):
        self._rate: float = rate_as_percentage / 100.0

    def simple_tax_for(self, amount: Dollars) -> Dollars:
        return Dollars(int(self._rate * int(amount)))

    def compound_tax_for(self, amount: Dollars) -> Dollars:
        amount = int(amount)
        return Dollars(int(amount / (1 - self._rate) - amount))

    def __eq__(self, other):
        if isinstance(other, TaxRate):
            return self._rate == other._rate
        return False

    def __str__(self):
        return f'{int(self._rate * 100)} %'
