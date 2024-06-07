import os


def bank_program():
    def show_balance():
        pass
        print(f"you have ${balance} available")
        # print("Would you like to make a withdrawal?")
        # balance_screen_choice = input("Choose 1 for YES, 2 for NO, go back to main menu")
        #
        # if balance_screen_choice == '1':
        #     amount_withdrawn = input("How much would you like?: ")
        #     new_balance = balance - amount_withdrawn
        # elif balance_screen_choice == '2':
        #     os.system('cls')
        #     is_running == True
        # else:
        #     print ("That is an invalid choice")

    def deposit():
        # deposit_amount = int(input("Enter amount to deposit: "))
        # if deposit_amount > 0:
        #     balance += deposit_amount
        pass

    def withdraw():
        pass

    new_balance = 0
    balance: int = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance()

        elif choice == '2':
            deposit()

        elif choice == '3':
            withdraw()

        elif choice == '4':
            os.system('cls')
            is_running = False

        else:
            print("That is an invalid choice")


print("Thank you. Have a nice day!")
