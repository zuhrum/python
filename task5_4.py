from functools import reduce


def my_fun(num_1, num_2):
    my_sum = num_1 * num_2
    return my_sum


my_list = [el for el in range(100, 1001, 1) if el % 2 == 0]
print(my_list)
print(reduce(my_fun, my_list))
