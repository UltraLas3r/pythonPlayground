main_class_array = ["melee", "caster", "ranged"]
sub_class_array = [["warrior", "brawler", "barbarian", "rogue"],
                   ["mage", "wizard", "cleric"],
                   ["hunter", "sniper", "ranger"]]

print("Choose class melee 1, caster 2, ranged 3")


class Rpg_Maker:

    def __init__(self):
        self.get_class_array = None
        self.get_sub_class_array = None

    def __getclassitem__(self, item_index):
        return self.get_class_array[item_index]

    def __getsubclassitem__(self, item_index):
        return self.get_sub_class_array[item_index]

    def pick_main_class(self, choice: int):
        user_select = choice
        main_class_map = {
            1: main_class_array[0],
            2: main_class_array[1],
            3: main_class_array[2],
        }

        _choice = main_class_map.get(user_select)
        if choice == 1 or 2 or 3:
            print(f"You choose a strong {_choice}")

        else:
            print("Invalid choice, try again")

        return _choice

    def pick_sub_class(self, main_class_choice):
        sub_class_map = {
            "melee": sub_class_array[0]
        }
        if main_class_choice == "melee":
            pass

        if main_class_choice == "caster":
            pass

        if main_class_choice == "ranged":
            pass


create_new_char = Rpg_Maker()

first_class_choice = int(input("choice: "))

class_choice = create_new_char.pick_main_class(first_class_choice)

print(class_choice)
