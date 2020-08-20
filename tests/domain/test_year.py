from finances.domain.year import Year


class TestYear:
    def test_equals(self):
        year1a = Year(2000)
        year1b = Year(2000)
        year2 = Year(1998)

        assert year1a == year1b
        assert year1a != year2

    def test_str(self):
        year = Year(2000)
        assert str(year) == '2000'

    def test_repr(self):
        year = Year(2001)
        assert repr(year) == '2001'

    def test_next_year(self):
        year = Year(2020)
        assert year.next_year == Year(2021)
