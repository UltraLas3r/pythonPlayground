main_class_array = ["melee", "caster", "ranged"]
sub_class_array = [["warrior", "brawler", "barbarian", "rogue"],
                   ["mage", "wizard", "cleric"],
                   ["hunter", "sniper", "ranger"]]


class PlayerStats:
    def __init__(self):
        self.get_class_array = None
        self.get_sub_class_array = None


def create_new_char():
    first_class_choice = int(input("choice>>>>: "))

    pick_main_class(first_class_choice)


def pick_main_class(choice: int):
    user_select = choice
    main_class_map = {
        1: main_class_array[0],
        2: main_class_array[1],
        3: main_class_array[2],
    }

    _choice = main_class_map.get(user_select)

    if choice == 1 or 2 or 3:
        print(f"You choose a strong {_choice} character")
        print("Now, pick a subclass to specialize into!")
        if choice == 1:
            sub_class_choice = choice
            pick_sub_class(sub_class_choice)
        if choice == 2:
            sub_class_choice = choice
            pick_sub_class(sub_class_choice)
        if choice == 3:
            sub_class_choice = choice
            pick_sub_class(sub_class_choice)

    else:
        print("Invalid choice, try again")


def pick_sub_class(choice):
    sub_class_map = {
        "melee": sub_class_array[0]
    }
    if choice == 1:
        print(f"Melee characters can specialize in the following sub classes:\n "
              f"1. {sub_class_array[0][0]}\n",
              f"2. {sub_class_array[0][1]}\n",
              f"3. {sub_class_array[0][2]}\n",
              f"4. {sub_class_array[0][3]}\n")
    if choice == 2:
        print(f"Caster characters can specialize in the following sub classes:\n "
              f"1. {sub_class_array[1][0]}\n",
              f"2. {sub_class_array[1][1]}\n",
              f"3. {sub_class_array[1][2]}\n")
    if choice == 3:
        print(f"Ranged characters can specialize in the following sub classes:\n "
              f"1. {sub_class_array[2][0]}\n",
              f"2. {sub_class_array[2][1]}\n",
              f"3. {sub_class_array[2][2]}\n")