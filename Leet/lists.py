class WorkingWithDataStructures:
    list_work = ["item0", "item1", "item2", "item3"]
    set_work = {1, 2, 3, 4, 5}
    dict_work = {"name": "Alice", "age": 30, "city": "New York"}
    tuple_work = (1, 2, 3, 4, 5)

    def lists(self):
        for items in self.list_work:
            print(items)

    def sets(self):
        pass

    def tuples(self):
        pass

    def dictionaries(self):
        for keys in self.dict_work.keys():
            print("Keys ==> : ", keys)
        for values in self.dict_work.values():
            print("Values ==> : ", values)

    # my_data = WorkingWithDataStructures()
    # my_data.dictionaries()

    def dictionary_keys(self, dictionary):
        for key in list(dictionary.keys()):
            print(key)

    #
    # my_keys = WorkingWithDataStructures()
    # my_keys.dictionary_keys(my_keys.dict_work)

    def remove_value_from_dict(self, dictionary, value):
        for keys in dictionary.keys():
            if dictionary[keys] == value:
                del dictionary[value]


my_data = WorkingWithDataStructures()
print("Before remove:::: > ", my_data.dict_work)
my_data.remove_value_from_dict(my_data.dict_work, "New York")
print("After remove ::> ", my_data.dict_work)
