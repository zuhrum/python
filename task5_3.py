def my_sum():
    my_line = (input("Ведите числа для сложения, через пробел, если хотите завершить программу введите Y: "))
    my_new_line = my_line.split(' ')
    count = 0
    while count < len(my_new_line):
        my_new_line[count] = int(my_new_line[count])
        count += 1
    my_sum = sum(my_new_line)
    print(my_sum)


my_sum()
