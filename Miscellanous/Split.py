__author__ = 'asdis'
# napisz wlasna prywatna funkcje split
def split (sign = " ", sentence = "Bannik to slowianski bog opiekujacy sie laznia"):
    i = 0
    table = []
    word = ""
    while i < sentence.__len__():
        if sentence[i] == sign:
            table.append(word)
            i += 1
            word = ""
            continue
        else:
            word += sentence[i]
        i += 1
    table.append(word)
    return table
print(split())