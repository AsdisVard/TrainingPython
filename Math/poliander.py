__author__ = 'asdis'

a = "kotencjon"
b = ""
i = 0
while i < a.__len__():
    b = b + a[a.__len__() - 1 - i]
    i += 1
print (b)

slowo = "abcde"
nowe = ""

i = 0
while i < slowo.__len__():
    nowe = nowe + slowo[slowo.__len__() - 1 - i]
    i += 1

if slowo == nowe:
    print ("jest poliander")
else:
    print ("nie jest")
