from CoffeeDatabaseApplication import database

MENU_PROMPT = """~~~!!~-- Coffee Bean Application --~!!~~~

Please Choose from the following options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See best preparation methods for a bean.
5) Exit.

Enter your selection number: 
"""


def menu():
    print(MENU_PROMPT)
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            prompt_add_new_bean(connection)

        elif user_input == "2":
            prompt_see_all_beans(connection)

        elif user_input == "3":
            prompt_find_bean_by_name(connection)

        elif user_input == "4":
            prompt_see_best_preparation_methods_for_a_bean(connection)

        else:
            print("Invalid input, please try again!")


def prompt_add_new_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter how you prepared your coffee: ")
    rating = int(input("Enter your rating score: "))

    database.add_bean(connection, name, method, rating)


def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_bean_by_name(connection):
    name = input("Enter bean name to find info: ")
    beans = database.get_beans_by_name(connection, name)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_see_best_preparation_methods_for_a_bean(connection):
    name = input("Enter bean name for preparation information: ")
    method = database.get_best_preparation_for_bean(connection, name)

    print(f"The best preparation method for {name} is the {method[2]} method.")


menu()
