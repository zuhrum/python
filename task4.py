number = int(input("Введите число: "))
maximum = 0
while number > 0:
    remains_number = number % 10
    number = number // 10
    if remains_number > maximum:
        maximum = remains_number
    else:
        maximum = maximum
print(f"Максимальное цифра в числе будет: {maximum}")
