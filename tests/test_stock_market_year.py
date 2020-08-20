import pytest

from finances.dollars import Dollars
from finances.stock_market_year import StockMarketYear
from tests.conftest import STARTING_BALANCE, INTEREST_RATE, CAPITAL_GAINS_TAX_RATE, year_factory, YEAR

STARTING_PRINCIPAL = Dollars(3000)


class TestStockMarketYear:

    @pytest.fixture
    def year(self, default_year) -> StockMarketYear:
        return default_year()

    def test_starting_values(self, year):
        assert 10000, year.starting_balance
        assert year.interest_rate == INTEREST_RATE
        assert year.starting_principal == STARTING_PRINCIPAL
        assert year.capital_gains_tax_rate == CAPITAL_GAINS_TAX_RATE
        assert year.year == YEAR

    def test_ending_balance(self, year):
        assert year.ending_balance == Dollars(11000), 'ending balance includes interest'
        year.withdraw(1000)
        assert year.ending_balance == Dollars(9900), 'ending balance includes withdrawals'
        year.withdraw(3000)
        assert year.ending_balance == Dollars(6233), 'ending balance includes capital gains tax withdrawals'

    def test_next_years_values(self, year):
        next_year = year.next_year()
        assert next_year.starting_balance == year.ending_balance
        assert next_year.interest_rate == year.interest_rate
        assert next_year.starting_principal == year.ending_principal
        assert next_year.capital_gains_tax_rate == year.capital_gains_tax_rate
        assert next_year.year == YEAR + 1

    def test_ending_principal(self, year):
        year.withdraw(1000)
        assert year.ending_principal == Dollars(9000), 'considers withdrawals'
        year.withdraw(2000)
        assert year.ending_principal == Dollars(7000), 'considers totals of multiple withdrawals'
        year.withdraw(8000)
        assert year.ending_principal == Dollars(0), 'never goes below zero'

    def test_total_withdrawn_including_capital_gains(self, year):
        year = year_factory(
            start=STARTING_BALANCE, interest_rate=INTEREST_RATE, starting_principal=Dollars(0)
        )
        year.withdraw(1000)
        assert year.capital_gains_tax_incurred == Dollars(333)
        assert year.total_withdrawn == Dollars(1333)

    def test_capital_gains_tax(self, year):
        year.withdraw(4000)
        capital_gains_tax = year.capital_gains_tax_rate.simple_tax_for(Dollars(1000))
        additional_withdrawals_to_cover_tax = Dollars(83)
        assert year.capital_gains_tax_incurred == additional_withdrawals_to_cover_tax + capital_gains_tax
        assert year.total_withdrawn == Dollars(4000) + capital_gains_tax + additional_withdrawals_to_cover_tax

    def test_interest_earned(self, year):
        assert year.appreciation == Dollars(1000), 'basic interest earned'
        year.withdraw(2000)
        assert year.appreciation == Dollars(800), 'withdrawals do not earn interest'
        year.withdraw(2000)
        assert year.appreciation == Dollars(566), 'capital gains taxes do not earn interest'
