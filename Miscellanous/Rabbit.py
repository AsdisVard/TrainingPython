__author__ = 'asdis'

sentence = "The White Rabbit in The Forest"

tab = sentence.split(" ")

tabmain = []

for word in tab:
    table = []

    a = word.upper()
    b = word.lower()
    c = word.__len__()

    table.append(a)
    table.append(b)
    table.append(c)

    tabmain.append(table)
    
print(tabmain)