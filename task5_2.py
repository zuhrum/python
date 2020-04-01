my_list = [1, 21, 3, 1, 21, 23, 21, 12, 3]
rating = int(input("введите рейтинг: "))
my_list.append(rating)
my_list.sort(reverse=True)
print(my_list)
