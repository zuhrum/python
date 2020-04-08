import random


my_list = [random.randint(0, 5) for el in range(10)]
print(my_list)
my_list1 = [el for el in my_list if my_list.count(el) == 1]
print(my_list1)
