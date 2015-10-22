__author__ = 'asdis'
from random import *
from ascending import *
from descending import *

table = []
for i in range (0, 50):
    table.append(randrange(0, 99))
print (table)

choice = int(input("wybierz sortowanie rosnace (1) lub malejace (2): "))
if choice == 1:
    print (ascending(table))
elif choice == 2:
    print(descending(table))
else:
    print("You've chosen wrong number")
