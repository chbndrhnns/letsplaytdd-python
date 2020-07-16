import typer

from finances.savings_account_year import SavingsAccountYear


def main():
    account = SavingsAccountYear(10000, interest_rate=10)

    for year in range(60):
        typer.echo(f'Year {year}: {account.ending_balance}')
        account = account.next_year()


if __name__ == '__main__':
    typer.run(main)
