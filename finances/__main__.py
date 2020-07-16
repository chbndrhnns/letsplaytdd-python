import typer

from finances.savings_account import SavingsAccount


def main():
    account = SavingsAccount(10000)

    for year in range(60):
        typer.echo(f'Year {year}: {account.balance}')
        account = account.next_year(10)


if __name__ == '__main__':
    typer.run(main)
