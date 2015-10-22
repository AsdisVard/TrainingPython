__author__ = 'asdis'
# np. Wyraz: ABAB, Klucz: 3 ==> DEDE
table = []
word = "zabc"
key = 140
rest = key % 25
b = ""

for i in word:
    if ord(i) + rest <= 122:
        table.append (chr(ord(i) + rest))
    else:
        table.append (chr(rest - (ord('z') - ord(i)) + ord('a')))
for i in table:
    b = b + i
print(b)



