from BankApplication.MyBankLogin import MybankLogin
from BankApplication.bank_program import MyBank
from CoffeeDatabaseApplication import database
from Leet.lists import WorkingWithDataStructures
from CoffeeDatabaseApplication import app


def main() -> None:
     connection = database.connect()
    # MybankLogin().AccountValidation()
    # MyBank().mainSplash()
    # WorkingWithDataStructures()
     app.menu()



if __name__ == '__main__':
    main()
