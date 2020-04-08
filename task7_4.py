from itertools import count


def gen():
    for j in count(1):
        i = 1
        factorial = 1
        while i <= j:
            factorial = factorial * i
            i += 1
        yield factorial


my_gen = gen()
my_count = 1
for g in my_gen:
    print(g)
    my_count += 1
    if my_count > 15:
        break
