__author__ = 'asdis'
def ascending (table):

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