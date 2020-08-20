from finances.dollars import Dollars
from finances.interest_rate import InterestRate
from finances.stock_market_year import StockMarketYear
from finances.tax_rate import TaxRate


class StockMarketAccount(object):
    def __init__(self, *, starting_year, ending_year, starting_principal: Dollars, starting_balance: Dollars,
                 interest_rate: InterestRate,
                 capital_gains_tax_rate: TaxRate):
        self.starting_year = starting_year
        self.ending_year = ending_year
        self.years: StockMarketYear = [None] * self.number_of_years

        self._populate_years(
            starting_balance=starting_balance,
            starting_principal=starting_principal,
            interest_rate=interest_rate,
            capital_gains_tax_rate=capital_gains_tax_rate
        )

    @property
    def number_of_years(self) -> int:
        return self.ending_year - self.starting_year + 1

    def get_year_offset(self, offset: int) -> StockMarketYear:
        return self.years[offset]

    def _populate_years(self, *, starting_balance, starting_principal, interest_rate, capital_gains_tax_rate):
        self.years[0] = StockMarketYear(
            year=self.starting_year,
            starting_balance=starting_balance,
            starting_principal=starting_principal,
            capital_gains_tax_rate=capital_gains_tax_rate,
            interest_rate=interest_rate
        )

        for i in range(1, self.number_of_years):
            self.years[i] = self.years[i - 1].next_year()
