from __future__ import annotations

from typing import Union

from finances.domain.base_class import FinanceBase


class Dollars(FinanceBase):
    SYMBOL = '$'

    def __init__(self, amount: Union[int, float]):
        self._amount = amount

    @property
    def rounded_amount(self):
        """Round to full Dollar"""
        return round(self._amount)

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
            return self.rounded_amount == other.rounded_amount

    def __str__(self):
        return f'{self.SYMBOL}{self.rounded_amount:.2f}'

    def percentage(self, percent: float) -> Dollars:
        return Dollars(self._amount * percent / 100.0)
