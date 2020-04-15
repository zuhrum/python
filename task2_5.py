fail = open('fail.txt')
lines = fail.readlines()
my_count_1 = 0
for i in lines:
    my_count_2 = 0
    for j in i:
        if j == '\n' or j == ' ':
            continue
        my_count_2 += 1
    my_count_1 += 1
    print(f"количество символов в {my_count_1} строке равно:{my_count_2}")
print(f"количество строк равно: {my_count_1}")
fail.close()
