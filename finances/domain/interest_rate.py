from finances.domain.base_class import FinanceBase
from finances.domain.dollars import Dollars


class InterestRate(FinanceBase):
    def __init__(self, rate_as_percentage: float):
        assert rate_as_percentage > 0, f'Interest rate must be positive and non-zero. Got: {rate_as_percentage}'
        self._rate_as_percentage = rate_as_percentage

    def interest_on(self, amount: Dollars) -> Dollars:
        return amount.percentage(self._rate_as_percentage)

    def __eq__(self, other):
        if isinstance(other, InterestRate):
            return self._rate_as_percentage == other._rate_as_percentage
        return False

    def __str__(self):
        return f'{self._rate_as_percentage} %'

    def __hash__(self):
        return hash(self._rate_as_percentage, )

    def __repr__(self):
        return self.__str__()
