import random
import trickycounter


def hello_world(text: str) -> None:
    print(text)


def main() -> None:
    # trickycounter.tricky_counter_method()
    hello_world("this is just a cool new thing")


if __name__ == '__main__':
    main()

# #
# # for i in {1, 2, 3, 4, 5}:
# #     a = i + 5
# #     if a > 7:
# #         print(f'hello friend ')
# #     else:
# #         print(a)
# #
#
#
# # Define the prefix for the keys
# prefix = 'a'
#
# # Define an empty dictionary to hold the results
# ip_dict = {}
#
# # Generate 11 keys with random IP addresses
# for i in range(11):
#     key = prefix + str(i)
#     ip = '.'.join([str(random.randint(0, 255)) for _ in range(4)])
#     ip_dict[key] = ip
#
# ## to print the key value pair as a tuple
# for i in ip_dict.items():
#     print(i)
# ## OR... if you just want to print the string value of the key and the value held for each key
# for key, value in ip_dict.items():
#     print(key, value)
# ## to print just the values of the dictionary
# # for i in ip_dict.values():
# #     print(i)
#
