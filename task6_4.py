from itertools import count, cycle

for i in cycle(['A', 'B', 'C', 'D']):
    print(i)
first_el = 4
for i in count(first_el):
    print(i)
