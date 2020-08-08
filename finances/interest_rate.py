class InterestRate:
    def __init__(self, rate_as_percentage):
        self._rate = rate_as_percentage

    def interest_on(self, amount: int) -> float:
        return float(self._rate * amount / 100)

    def __eq__(self, other):
        if isinstance(other, InterestRate):
            return self._rate == other._rate

    def __str__(self):
        return f'{self._rate} %'

    def __repr__(self):
        return self.__str__()