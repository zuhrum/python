string = str(input("Введите строку из нескольких слов: "))
list_1 = string.split(' ')
for ind, i in enumerate(list_1, 1):
    print(ind, i[0:10])
