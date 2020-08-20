from __future__ import annotations

from finances.domain.base_class import FinanceBase


class Dollars(FinanceBase):
    SYMBOL = 'USD'

    def __init__(self, amount: int):
        self._amount = amount

    def subtract_to_zero(self, other):
        if isinstance(other, Dollars):
            return max(Dollars(0), self - other)

    def __add__(self, other):
        if isinstance(other, Dollars):
            return Dollars(self._amount + other._amount)
        raise ValueError('Can only compare to Dollar')

    def __sub__(self, other):
        if isinstance(other, Dollars):
            return Dollars(self._amount - other._amount)
        raise ValueError('Can only compare to Dollar')

    def __lt__(self, other):
        if isinstance(other, Dollars):
            return self._amount < other._amount
        raise ValueError('Can only compare to Dollar')

    def __gt__(self, other):
        if isinstance(other, Dollars):
            return self._amount > other._amount
        raise ValueError('Can only compare to Dollar')

    def __eq__(self, other):
        if isinstance(other, Dollars):
            return self._amount == other._amount

    def __str__(self):
        return f'{self._amount} {self.SYMBOL}'

    def percentage(self, percent: float) -> Dollars:
        return Dollars(int(self._amount * percent / 100.0))
