start_distance = int(input("Введите значение с которого спортсмен начнёт тренировку: "))
finish_distance = int(input("Введите на котором спортсмен закончит тренировку: "))
day = 1
while start_distance < finish_distance:
    start_distance = start_distance * 1.1
    day = day + 1
print(f"на {day}-й день спортсмен достиг результата — не менее {finish_distance} км")
