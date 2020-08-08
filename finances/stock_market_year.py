from finances.dollars import Dollars
from finances.interest_rate import InterestRate
from finances.tax_rate import TaxRate


class StockMarketYear:

    def __init__(
            self,
            starting_balance: Dollars,
            *,
            interest_rate: InterestRate,
            starting_principal: Dollars,
            capital_gains_tax_rate: TaxRate
    ):
        self.starting_balance = starting_balance
        self.interest_rate = interest_rate
        self.capital_gains_tax_rate: TaxRate = capital_gains_tax_rate

        self._starting_principal = starting_principal
        self._capital_gains_amount = starting_balance - starting_principal
        self.total_withdrawals = Dollars(0)

    @property
    def starting_principal(self) -> Dollars:
        return self._starting_principal

    @property
    def ending_balance(self) -> Dollars:
        return self.starting_balance - self.total_withdrawn + self.interest_earned

    @property
    def ending_principal(self) -> Dollars:
        return self.starting_balance.subtract_to_zero(self.total_withdrawals)

    @property
    def total_withdrawn(self) -> Dollars:
        return self.total_withdrawals + self.capital_gains_tax_incurred

    @property
    def interest_earned(self):
        return Dollars(self.interest_rate.interest_on(self.starting_balance.amount - self.total_withdrawn.amount))

    @property
    def capital_gains_tax_incurred(self) -> Dollars:
        return Dollars(self.capital_gains_tax_rate.compound_tax_for(self._capital_gains_withdrawn().amount))

    def next_year(self):
        result = StockMarketYear(
            self.ending_balance,
            interest_rate=self.interest_rate,
            starting_principal=self.ending_principal,
            capital_gains_tax_rate=self.capital_gains_tax_rate
        )
        return result

    def withdraw(self, amount):
        self.total_withdrawals += Dollars(amount)

    def _capital_gains_withdrawn(self) -> Dollars:
        return self.total_withdrawals.subtract_to_zero(self.starting_principal)
