from finances.domain.base_class import FinanceBase
from finances.domain.dollars import Dollars


class InterestRate(FinanceBase):
    def __init__(self, rate_as_percentage):
        self._rate = rate_as_percentage

    def interest_on(self, amount: Dollars) -> int:
        return int(self._rate * int(amount) / 100)

    def __eq__(self, other):
        if isinstance(other, InterestRate):
            return self._rate == other._rate
        return False

    def __str__(self):
        return f'{self._rate} %'

    def __repr__(self):
        return self.__str__()
