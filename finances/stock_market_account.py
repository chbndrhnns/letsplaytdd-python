from finances.dollars import Dollars
from finances.interest_rate import InterestRate
from finances.stock_market_year import StockMarketYear
from finances.tax_rate import TaxRate


class StockMarketAccount(object):
    def __init__(self, *, starting_year, ending_year, starting_principal: Dollars, starting_balance: Dollars,
                 interest_rate: InterestRate,
                 capital_gains_tax_rate: TaxRate):
        self._starting_principal = starting_principal
        self._interest_rate = interest_rate
        self._starting_balance = starting_balance
        self._capital_gains_tax_rate = capital_gains_tax_rate
        self._starting_year = starting_year
        self._ending_year = ending_year
        self._years = []

    @property
    def number_of_years(self) -> int:
        return self._ending_year - self._starting_year + 1

    def get_year(self, offset: int) -> StockMarketYear:
        year = StockMarketYear(
            starting_balance=self._starting_balance,
            starting_principal=self._starting_principal,
            capital_gains_tax_rate=self._capital_gains_tax_rate,
            interest_rate=self._interest_rate
        )
        for _ in range(offset):
            year = year.next_year()

        return year
