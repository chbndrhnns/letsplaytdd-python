class TaxRate:
    def __init__(self, rate_as_percentage: float):
        self._rate: float = rate_as_percentage / 100.0

    @property
    def rate(self) -> int:
        # TODO: delete me
        return int(self._rate * 100)

    def simple_tax_for(self, amount: int):
        return int(amount * self._rate)

    def compound_tax_for(self, amount: int):
        return int(amount / (1 - self._rate) - amount)

    def __eq__(self, other):
        if isinstance(other, TaxRate):
            return self._rate == other._rate
        return False

    def __str__(self):
        return f'{int(self._rate * 100)} %'
