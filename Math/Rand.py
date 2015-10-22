__author__ = 'asdis'

from random import *

table = []
minimum = 9
maximum = 0
i = 0
for i in range(0, 9, 1):
    table.append(randrange(10))
print(table)

i = 0
while i < table.__len__():
    if table[i] > maximum:
        maximum = table[i]
    if table[i] < minimum:
        minimum = table[i]
    i += 1

max2 = 0
table.remove(maximum)
for i in table:
    if table[i] > max2:
        max2 = table[i]

print(minimum)
print(maximum)
print (max2)
