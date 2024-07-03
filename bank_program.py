import os
from accountdb import AccessDB


class MyBank:
    balance = 15
    is_running = True
    mainMenu = ''

    # if input() == "p":
    #     print({balance})

    def show_balance(self):
        print(f"you have ${self.balance} available")
        mainMenu = input("Return to main menu? y or n")

        if mainMenu == "y":
            self.mainSplash()
        else:
            self.show_balance()

        # else:
        #     print ("That is an invalid choice")

    def deposit(self):
        deposit_amount = int(input("Enter amount to deposit: "))
        if deposit_amount > 0:
            self.balance += deposit_amount
            print("Your new balance is %s" % self.balance)

            mainMenu = input("Return to main menu? y or n")
            if mainMenu == "y":
                self.mainSplash()
            else:
                self.deposit()

    def withdraw(self):
        if self.balance >= 0:
            withdrawFunds = input(f"You have {self.balance} would you like to withdrawal funds? y or n")
            if withdrawFunds == "y":
                withdraw_amount = int(input("Enter amount to withdrawal: "))
                if self.balance - withdraw_amount >= 0:
                    self.balance -= withdraw_amount
                    print(f"Your new balance is {self.balance}")
                    mainMenu = input("Return to main menu? y or n: ")
                else:
                    print("You cannot withdraw more than you have")

            else:
                print("please enter a proper input value")
                self.withdraw()

            if mainMenu == "y":
                self.mainSplash()
            else:
                self.withdraw()

    def mainSplash(self):
        print("~~~~~> Banking Program <~~~~~~")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("5. access db")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            self.show_balance()

        elif choice == '2':
            self.deposit()

        elif choice == '3':
            self.withdraw()

        elif choice == '4':
            os.system('cls')
            is_running = False

        elif choice == '5':
            AccessDB()

        else:
            print("That is an invalid choice")
