from finances.savings_account import SavingsAccount


def run():
    account = SavingsAccount(10000)

    for year in range(60):
        print(f'Year {year}: {account.balance}')
        account = account.next_year(10)


if __name__ == '__main__':
    run()
