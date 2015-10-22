__author__ = 'asdis'
step = 10
i = 1
a = 0
b = 1
while i < step:
    c = a + b
    a = b
    b = c
    i +=1
print (c)