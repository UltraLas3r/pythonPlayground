from BankApplication.MyBankLogin import MybankLogin
from BankApplication.bank_program import MyBank



def main() -> None:
    MybankLogin().AccountValidation()
    MyBank().mainSplash()


if __name__ == '__main__':
    main()