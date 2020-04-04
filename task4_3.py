def exponentiation(x, y):
    temporary_variable = x
    while y < -1:
        temporary_variable_2 = temporary_variable * x
        temporary_variable = temporary_variable_2
        y += 1
    return print(1 / temporary_variable)


def exponentiation_2(x, y):
    return print(x ** y)


exponentiation_2(2, -6)
exponentiation(2, -5)
