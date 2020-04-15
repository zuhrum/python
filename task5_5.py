with open('5.txt', 'w') as f:
    nums = input('Введите числа через пробел: ')
    f.write('числа: ' + nums + '\n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f.write('сумма: ' + str(sum_nums))
    print('сумма чисел:', sum_nums)
