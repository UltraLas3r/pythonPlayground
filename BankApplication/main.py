from BankApplication.MyBankLogin import MybankLogin
from BankApplication.bank_program import MyBank
from CoffeeDatabaseApplication import database


def main() -> None:
    connection = database.connect()

    MybankLogin().AccountValidation()
    MyBank().mainSplash()


if __name__ == '__main__':
    main()
