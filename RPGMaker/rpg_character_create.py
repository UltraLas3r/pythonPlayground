main_class_array = ["melee", "caster", "ranged"]
sub_class_array = [["warrior", "brawler", "barbarian", "rogue"],
                   ["mage", "wizard", "cleric"],
                   ["hunter", "sniper", "ranger"]]


class rpg_maker:
    def __init__(self):
        pass

    def __getitem__(self, item_index):
        return self.num_array[item_index]


def pick_main_class():
    pass


def pick_sub_class(main_class_choice):
    if main_class_choice == "melee":
        pass

    if main_class_choice == "caster":
        pass

    if main_class_choice == "ranged":
        pass