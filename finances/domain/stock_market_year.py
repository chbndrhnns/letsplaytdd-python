from typing import TypeVar

from finances.domain.base_class import FinanceBase
from finances.domain.dollars import Dollars
from finances.domain.interest_rate import InterestRate
from finances.domain.tax_rate import TaxRate
from finances.domain.year import Year

StockMarketYearT = TypeVar('StockMarketYearT', bound='StockMarketYear')  # noqa


class StockMarketYear(FinanceBase):
    def __init__(
            self,
            *,
            starting_balance: Dollars,
            year: Year,
            interest_rate: InterestRate,
            starting_principal: Dollars,
            capital_gains_tax_rate: TaxRate
    ):
        self.starting_balance = starting_balance
        self.interest_rate = interest_rate
        self.capital_gains_tax_rate: TaxRate = capital_gains_tax_rate

        self._year: Year = year
        self._starting_principal = starting_principal
        self._capital_gains_amount = starting_balance - starting_principal
        self.total_withdrawals = Dollars(0)

    @property
    def year(self):
        return self._year

    @property
    def starting_principal(self) -> Dollars:
        return self._starting_principal

    @property
    def ending_balance(self) -> Dollars:
        return self.starting_balance - self.total_withdrawn + self.appreciation

    @property
    def ending_principal(self) -> Dollars:
        return self.starting_principal.subtract_to_zero(self.total_withdrawals)

    @property
    def total_withdrawn(self) -> Dollars:
        return self.total_withdrawals + self.capital_gains_tax_incurred

    @property
    def appreciation(self) -> Dollars:
        return self.interest_rate.interest_on(self.starting_balance - self.total_withdrawn)

    @property
    def capital_gains_tax_incurred(self) -> Dollars:
        return self.capital_gains_tax_rate.compound_tax_for(self._capital_gains_withdrawn())

    def next_year(self) -> StockMarketYearT:
        return StockMarketYear(
            starting_balance=self.ending_balance,
            year=self._year.next_year,
            interest_rate=self.interest_rate,
            starting_principal=self.ending_principal,
            capital_gains_tax_rate=self.capital_gains_tax_rate
        )

    def withdraw(self, amount) -> None:
        self.total_withdrawals += Dollars(amount)

    def _capital_gains_withdrawn(self) -> Dollars:
        return self.total_withdrawals.subtract_to_zero(self.starting_principal)
