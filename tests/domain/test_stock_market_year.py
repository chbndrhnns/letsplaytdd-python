import pytest

from finances.domain.dollars import Dollars
from finances.domain.stock_market_year import StockMarketYear
from tests.conftest import STARTING_BALANCE, INTEREST_RATE, CAPITAL_GAINS_TAX_RATE, year_factory, YEAR

STARTING_PRINCIPAL = Dollars(3000)


class TestStockMarketYear:

    @pytest.fixture
    def year(self, default_year) -> StockMarketYear:
        return default_year(starting_principal=STARTING_PRINCIPAL)

    def test_starting_values(self, year):
        assert year.starting_balance == STARTING_BALANCE
        assert year.interest_rate == INTEREST_RATE
        assert year.starting_principal == STARTING_PRINCIPAL
        assert year.capital_gains_tax_rate == CAPITAL_GAINS_TAX_RATE
        assert year.year == YEAR

    def test_ending_balance(self, year):
        assert year.ending_balance == Dollars(11000), 'ending balance includes interest'
        year.withdraw(Dollars(1000))
        assert year.ending_balance == Dollars(9533), 'ending balance includes withdrawals'

    def test_next_years_values(self, year):
        next_year = year.next_year()
        assert next_year.starting_balance == year.ending_balance
        assert next_year.interest_rate == year.interest_rate
        assert next_year.starting_principal == year.ending_principal
        assert next_year.capital_gains_tax_rate == year.capital_gains_tax_rate
        assert next_year.year == YEAR.next_year

    def test_total_withdrawn_including_capital_gains(self, year):
        year = year_factory(
            starting_balance=STARTING_BALANCE, interest_rate=INTEREST_RATE, starting_principal=Dollars(0)
        )
        year.withdraw(Dollars(1000))
        assert year.capital_gains_tax_incurred == Dollars(333)
        assert year.total_withdrawn == Dollars(1333)

    def test_treat_all_withdrawals_as_subject_to_capital_gains_tax_until_all_sold(self, year):
        capital_gains = STARTING_BALANCE - STARTING_PRINCIPAL
        assert Dollars(7000) == capital_gains

        year.withdraw(Dollars(500))
        assert Dollars(
            167) == year.capital_gains_tax_incurred, 'pay tax on all withdrawal'
        year.withdraw(capital_gains)
        assert Dollars(
            2333) == year.capital_gains_tax_incurred, 'pay tax on all withdrawal until all capital gains are withdrawn'
        year.withdraw(Dollars(1000))
        assert Dollars(2333) == year.capital_gains_tax_incurred, 'pay no more tax once all capital gains withdrawn'

    def test_ending_principal(self, year):
        year.withdraw(Dollars(500))
        assert year.ending_principal == STARTING_PRINCIPAL, 'withdrawals less then capital gains do not reduce ' \
                                                            'principal'
        year.withdraw(Dollars(6500))

        total_withdrawn = Dollars(9333)
        capital_gains = Dollars(7000)
        principal_reduced_by = total_withdrawn - capital_gains
        expected_principal = STARTING_PRINCIPAL - principal_reduced_by
        assert year.ending_principal == expected_principal, \
            'principal is reduced by difference of total withdrawals and capital gains'

        year.withdraw(Dollars(1000))
        assert year.ending_principal == Dollars(-333), 'principal goes negative if overdrawn'

    def test_capital_gains_tax(self, year):
        year.withdraw(Dollars(4000))
        assert year.capital_gains_tax_incurred == Dollars(
            1333), 'tax includes tax on withdrawals to cover capital gains'
        assert year.total_withdrawn == Dollars(5333), 'includes capital gains tax'

    def test_interest_earned(self, year):
        assert year.appreciation == Dollars(1000), 'basic interest earned'
        year.withdraw(Dollars(2000))
        assert year.appreciation == Dollars(733), 'withdrawals do not earn interest'
