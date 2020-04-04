def my_calc(arg_1, arg_2, arg_3):
    my_args = [arg_1, arg_2, arg_3]
    my_max = max(my_args)
    my_args.remove(my_max)
    my_max2 = max(my_args)
    my_sum = my_max + my_max2
    return print(my_sum)


my_calc(4, 1, 8)
