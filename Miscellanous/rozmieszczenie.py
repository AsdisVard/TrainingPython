__author__ = 'asdis'
# masz slowo i masz znalezc w nim dana litere. Ale funkcja ma zwracac pozycje danej litery w stringu do tablicy np.: word = 'M' sentence = 'mama': [0, 2]
def placement (letter = "z", sentence = 'abrakadarba'):
    i = 0
    table = []
    while i < sentence.__len__():
        if letter == sentence[i]:
            table.append(i)
        i += 1
    if table.__len__() == 0:
        return None
    return table
print(placement())

