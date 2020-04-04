def my_fractionally():
    arg_1 = int(input("Введите числитель: "))
    arg_2 = int(input("Введите знаменатель: "))
    while True:
        if arg_2 == 0:
            arg_2 = int(input("Знаменатель не может быть равен 0, введите другое число: "))
        else:
            break
    fractionally = arg_1 / arg_2
    return print(fractionally)


my_fractionally()
