from finances.dollars import Dollars


class TaxRate:
    def __init__(self, rate_as_percentage: float):
        self._rate: float = rate_as_percentage / 100.0

    def simple_tax_for(self, amount: Dollars) -> int:
        return int(self._rate * amount.amount)

    def compound_tax_for(self, amount: Dollars) -> int:
        return int(amount.amount / (1 - self._rate) - amount.amount)

    def __eq__(self, other):
        if isinstance(other, TaxRate):
            return self._rate == other._rate
        return False

    def __str__(self):
        return f'{int(self._rate * 100)} %'
