from typing import List, Optional

from finances.domain.base_class import FinanceBase
from finances.domain.dollars import Dollars
from finances.domain.interest_rate import InterestRate
from finances.domain.stock_market_year import StockMarketYear
from finances.domain.tax_rate import TaxRate
from finances.domain.year import Year


class StockMarketAccount(FinanceBase):
    def __init__(self, *, starting_year, ending_year, starting_principal: Dollars, starting_balance: Dollars,
                 interest_rate: InterestRate,
                 capital_gains_tax_rate: TaxRate):
        self.starting_year: Year = starting_year
        self.ending_year: Year = ending_year
        self.years: List[StockMarketYear] = [None] * self.number_of_years  # type: ignore

        self._populate_years(
            starting_balance=starting_balance,
            starting_principal=starting_principal,
            interest_rate=interest_rate,
            capital_gains_tax_rate=capital_gains_tax_rate
        )

    @property
    def number_of_years(self) -> int:
        return self.starting_year.number_of_years_inclusive(self.ending_year)

    def get_year_offset(self, offset: int) -> StockMarketYear:
        assert 0 <= offset < self.number_of_years, f'Offset needs to be between 0 and {self.number_of_years}'
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
