from BankApplication.MyBankLogin import MybankLogin
from BankApplication.bank_program import MyBank
from CoffeeDatabaseApplication import database
from Leet.lists import WorkingWithLists


def main() -> None:
    connection = database.connect()
    MybankLogin().AccountValidation()
    MyBank().mainSplash()
    WorkingWithLists()


if __name__ == '__main__':
    main()
