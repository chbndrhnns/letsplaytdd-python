class Dollar:
    SYMBOL = 'USD'

    def __init__(self, amount):
        self._amount = amount

    def __add__(self, other):
        if isinstance(other, Dollar):
            return Dollar(self._amount + other._amount)

    def __sub__(self, other):
        if isinstance(other, Dollar):
            return Dollar(self._amount - other._amount)

    def __eq__(self, other):
        if isinstance(other, Dollar):
            return self._amount == other._amount

    def __str__(self):
        return f'{self._amount} {self.SYMBOL}'