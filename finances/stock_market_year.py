from finances.interest_rate import InterestRate
from finances.tax_rate import TaxRate


class StockMarketYear(object):

    def __init__(
            self,
            starting_balance: int,
            *,
            interest_rate: InterestRate,
            starting_principal: int,
            capital_gains_tax_rate: TaxRate
    ):
        self.starting_balance = starting_balance
        self.interest_rate = interest_rate
        self.capital_gains_tax_rate: TaxRate = capital_gains_tax_rate

        self._starting_principal = starting_principal
        self._capital_gains_amount = starting_balance - starting_principal
        self.total_withdrawals = 0

    @property
    def starting_principal(self):
        return self._starting_principal

    @property
    def ending_balance(self):
        return self.starting_balance - self.total_withdrawn + self.interest_earned

    @property
    def ending_principal(self):
        result = self.starting_principal - self.total_withdrawals
        return max(0, result)

    @property
    def total_withdrawn(self):
        return self.total_withdrawals + self.capital_gains_tax_incurred

    @property
    def interest_earned(self):
        return self.interest_rate.interest_on(self.starting_balance - self.total_withdrawn)

    @property
    def capital_gains_tax_incurred(self):
        return self.capital_gains_tax_rate.compound_tax_for(self._capital_gains_withdrawn())

    def next_year(self):
        result = StockMarketYear(
            self.ending_balance,
            interest_rate=self.interest_rate,
            starting_principal=self.ending_principal,
            capital_gains_tax_rate=self.capital_gains_tax_rate
        )
        return result

    def withdraw(self, amount):
        self.total_withdrawals += amount

    def _capital_gains_withdrawn(self):
        result = -1 * (self.starting_principal - self.total_withdrawals)
        return max(0, result)
