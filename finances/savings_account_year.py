class SavingsAccountYear(object):

    def __init__(
            self,
            starting_balance: int = 0,
            *,
            interest_rate: int = 0,
            starting_principal: int = 0,
            capital_gains_tax_rate: int = 25
    ):
        self.starting_balance = starting_balance
        self.interest_rate = interest_rate
        self._starting_principal = starting_principal
        self._capital_gains_amount = starting_balance - starting_principal
        self._total_withdrawn = 0
        self.capital_gains_tax_rate = capital_gains_tax_rate

    @property
    def starting_principal(self):
        return self.starting_balance - self._capital_gains_amount

    @property
    def ending_balance(self):
        modified_start = self.starting_balance - self.total_withdrawals - self.capital_gains_tax_incurred()
        return int(modified_start + (modified_start * self.interest_rate) / 100)

    @property
    def ending_principal(self):
        result = self.starting_principal - self.total_withdrawals
        return max(0, result)

    @property
    def total_withdrawals(self):
        return self._total_withdrawn

    @property
    def capital_gains_withdrawn(self):
        result = -1 * (self.starting_principal - self.total_withdrawals)
        return max(0, result)

    def next_year(self):
        result = SavingsAccountYear(self.ending_balance, interest_rate=self.interest_rate)
        return result

    def withdraw(self, amount):
        self._total_withdrawn += amount

    def capital_gains_tax_incurred(self):
        return int(self.capital_gains_withdrawn / (100 - self.capital_gains_tax_rate) * self.capital_gains_tax_rate)
