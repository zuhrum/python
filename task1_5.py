file = open('new_fail.txt', 'w')
while True:
    my_line = (input("Ведите строку для записи, для остановки записи оставте пустую строку:"))
    file.writelines(my_line + '\n')
    if my_line == '':
        break
file.close()
