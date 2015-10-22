__author__ = 'asdis'

password = 'Ala_ma_kota'

while password.__len__() % 4 != 0:
    password = password + '*'
print(password)

word = ""
for startPoint in range(0,4,1):
    i = 0
    while i < password.__len__():
        if i == 0 or (i + 4) % 4 == 0:
            word = word + password[startPoint + i]
            i += 4
    word = word + "#"
print(word)



'''
word = ""
i = 0
while i < password.__len__():
    if i == 0 or (i + 4) % 4 == 0:
        word = word + password[i]
        i += 4
word = word + "#"

i = 1
while i < password.__len__():
    if i == 1 or ((i + 4) - 1) % 4 == 0:
        word = word + password[i]
        i += 4
word = word + "#"

i = 2
while i < password.__len__():
    if i == 2 or ((i + 4) - 2) % 4 == 0:
        word = word + password[i]
        i += 4
word = word + "#"

i = 3
while i < password.__len__():
    if i == 3 or ((i + 4) - 3) % 4 == 0:
        word = word + password[i]
        i += 4
word = word + "#"

print(word)
'''

"""
row1 = ''
i = 0
while i < password.__len__():
    row1 = row1 + password[i]
    i += 4
row1 = row1 + '#'
print(row1)

row2 = ''
i = 1
while i < password.__len__():
    row2 = row2 + password[i]
    i += 4
row2 = row2 + '#'
print(row2)

row3 = ''
i = 2
while i < password.__len__():
    row3 = row3 + password[i]
    i += 4
row3 = row3 + '#'
print(row3)

row4 = ''
i = 3
while i < password.__len__():
    row4 = row4 + password[i]
    i += 4
row4 = row4 + '#'
print(row4)

result = row1 + row2 + row3 + row4
print(result)
"""