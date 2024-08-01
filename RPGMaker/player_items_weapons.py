class PlayerItems:
    def __getclassitem__(self, item_index):
        return self.get_class_array[item_index]

    def __getsubclassitem__(self, item_index):
        return self.get_sub_class_array[item_index]


class PlayerWeapons:
    pass


