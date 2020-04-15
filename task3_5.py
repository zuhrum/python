with open('salary.txt') as fail:
    salaries = []
    lines = fail.readlines()
    for line in lines:
        name, salary = line.split(' - ')
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
    print('\nсредяя заработная плата:', sum(salaries) / len(salaries))