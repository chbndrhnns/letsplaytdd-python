import typer

from finances.stock_market_year import StockMarketYear


def main():
    account = StockMarketYear(10000, interest_rate=10)

    for year in range(60):
        typer.echo(f'Year {year}: {account.ending_balance}')
        account = account.next_year()


if __name__ == '__main__':
    typer.run(main)
