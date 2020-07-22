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
        self.capital_gains_tax_rate = capital_gains_tax_rate

        self._starting_principal = starting_principal
        self._capital_gains_amount = starting_balance - starting_principal
        self.total_withdrawals = 0

    @property
    def starting_principal(self):
        return self._starting_principal

    @property
    def starting_capital_gains(self):
        return self._capital_gains_amount

    @property
    def ending_balance(self):
        modified_start = self.starting_balance - self.total_withdrawn
        return modified_start + self.interest_earned

    @property
    def ending_capital_gains(self):
        return self._capital_gains_amount + self.interest_earned - self.capital_gains_tax_incurred

    @property
    def ending_principal(self):
        result = self.starting_principal - self.total_withdrawals
        return max(0, result)

    @property
    def total_withdrawn(self):
        return self.total_withdrawals + self.capital_gains_tax_incurred

    @property
    def interest_earned(self):
        return int((self.starting_balance - self.total_withdrawn) * self.interest_rate / 100)

    @property
    def capital_gains_withdrawn(self):
        result = -1 * (self.starting_principal - self.total_withdrawals)
        return max(0, result)

    @property
    def capital_gains_tax_incurred(self):
        return int(self.capital_gains_withdrawn / (100 - self.capital_gains_tax_rate) * self.capital_gains_tax_rate)

    def next_year(self):
        result = SavingsAccountYear(self.ending_balance, interest_rate=self.interest_rate)
        return result

    def withdraw(self, amount):
        self.total_withdrawals += amount
