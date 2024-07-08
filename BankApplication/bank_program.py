import os
from BankApplication.accountdb import connect


class MyBank:
    balance = 15
    is_running = True
    mainMenu = ''

    BANK_PROMPT = """~~~!!~-- Cool Bank Application --~!!~~~
    
        Please Choose from the following options:
    
        1) Show Balance
        2) Make a Deposit
        3) Make a Withdrawal.
        4) Log out of terminal.
        5) Access Super Secret Database info 
    
        Enter your selection number: """

    def show_balance(self):
        print(f"you have ${self.balance} available")
        mainMenu = input("Return to main menu? y or n: ")

        if mainMenu == "y":
            self.mainSplash()
        elif mainMenu == "n":
            self.show_balance()
        else:
            print("\n \n!! please enter a proper input value !! : ")

    def deposit(self):
        deposit_amount = int(input("Enter amount to deposit: "))
        if deposit_amount > 0:
            self.balance += deposit_amount
            print("Your new balance is %s" % self.balance)

            mainMenu = input("\n \nReturn to main menu? y or n: ")
            if mainMenu == "y":
                self.mainSplash()
            else:
                self.deposit()

    def withdraw(self):
        if self.balance >= 0:
            withdrawFunds = input(f"You have {self.balance} would you like to withdrawal funds? y or n: ")
            if withdrawFunds == "y":
                withdraw_amount = int(input("Enter amount to withdrawal: "))
                if self.balance - withdraw_amount >= 0:
                    self.balance -= withdraw_amount
                    print(f"Your new balance is {self.balance}")
                    main_menu = input("\n \nReturn to main menu? y or n: ")
                if self.balance < withdraw_amount:
                    print("\n You cannot withdraw more than you have \n")
                else:
                    print("\n \n!! please enter a proper input value !! : ")
                    self.withdraw()

            main_menu = input("\n Withdrawa3l Complete \n Return to main menu? y or n: ")
            if main_menu == "y":
                self.mainSplash()
            else:
                self.withdraw()

    def mainSplash(self):
        while (user_input := input(self.BANK_PROMPT)) != "5":
            if user_input == '1':
                self.show_balance()

            elif user_input == '2':
                self.deposit()

            elif user_input == '3':
                self.withdraw()

            elif user_input == '4':
                os.system('cls')
                is_running = False

            elif user_input == '5':
                print("you finna access db info!")
                # connect().get_info('account')
                connect().get_info('balance')

            else:
                print("\n !! please enter a proper input value !! : \n")

    def show_balance_prompt1(self):
        pass

    def make_deposit_prompt2(self):
        pass

    def make_withdrawal_prompt3(self):
        pass

    def open_new_account_prompt(self):
        pass
