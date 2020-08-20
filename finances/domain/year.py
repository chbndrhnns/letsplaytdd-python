class Year:
    """Year model"""

    def __init__(self, year: int):
        self._year = year

    @property
    def next_year(self):
        return Year(self._year + 1)

    def __eq__(self, other):
        if isinstance(other, Year):
            return self._year == other._year
        raise ValueError('No year')

    def __str__(self):
        return str(self._year)

    def __repr__(self):
        return self.__str__()
