import random


my_list = [random.randint(0, 20) for el in range(10)]
my_new_list = []
for j in range(len(my_list)-1):
    if my_list[j] < my_list[j + 1]:
        my_new_list.append(my_list[j + 1])
print(my_list)
print(my_new_list)
