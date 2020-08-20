from finances.domain.year import Year


class TestYear:
    def test_equals(self):
        year1a = Year(2000)
        year1b = Year(2000)
        year2 = Year(1998)

        assert year1a == year1b
        assert year1a != year2

    def test_hash(self):
        year1a = Year(2000)
        year1b = Year(2000)
        year2 = Year(1998)

        assert hash(year1a) == hash(year1b)
        assert hash(year1a) != hash(year2)

    def test_str(self):
        year = Year(2000)
        assert str(year) == '2000'

    def test_repr(self):
        year = Year(2001)
        assert repr(year) == '2001'

    def test_add(self):
        assert Year(2000) + 5 == Year(2005)
        assert Year(2020) + Year(2030) == 10

    def test_number_of_years_inclusive(self):
        assert Year(2020).number_of_years_inclusive(Year(2050)) == 31

    def test_sub(self):
        assert Year(1998) - 5 == Year(1993)
        assert Year(2002) - Year(1998) == 4
        assert Year(1998) - Year(2002) == 4

    def test_next_year(self):
        year = Year(2020)
        assert year.next_year == Year(2021)
