__author__ = 'asdis'
from random import *

table = []
for i in range (0, 50):
    table.append(randrange(0, 99))
print (table)

i=0
flag = True  #flaga oznacza, ze byla zmiana
while flag == True:
    flag = False
    i = 0
    while i < table.__len__()-1:
        if table[i] > table[i+1]:
            a = table[i+1]
            table[i + 1] = table[i]
            table[i] = a
            flag = True
        i += 1

print(table)

i=0
flag = True  #flaga oznacza, ze byla zmiana
while flag == True:
    flag = False
    i = 0
    while i < table.__len__()-1:
        if table[i] < table[i+1]:
            a = table[i+1]
            table[i + 1] = table[i]
            table[i] = a
            flag = True
        i += 1

print(table)

