from __future__ import annotations

from finances.domain.base_class import FinanceBase


class Year(FinanceBase):
    """Year model"""

    def __init__(self, year: int):
        self._year = year

    @property
    def next_year(self):
        return Year(self._year + 1)

    def number_of_years_inclusive(self, ending_year: Year):
        return int(abs(self._year - ending_year._year) + 1)

    def __int__(self):
        return self._year

    def __add__(self, other):
        if isinstance(other, int):
            return Year(self._year + other)
        if isinstance(other, Year):
            return abs(self._year - other._year)

        raise ValueError('Unsupported operator')

    def __sub__(self, other):
        if isinstance(other, int):
            return Year(self._year - other)
        if isinstance(other, Year):
            return abs(self._year - other._year)

        raise ValueError('Unsupported operator')

    def __eq__(self, other):
        if isinstance(other, Year):
            return self._year == other._year
        raise ValueError('No year')

    def __str__(self):
        return str(self._year)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self._year, )
