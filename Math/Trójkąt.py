__author__ = 'asdis'
from math import *

a = 3
b = 4
c = 5

alpha = 30
beta = 90
gamma = 60

if alpha + beta + gamma == 180:
    print ("Bedzie z tego trojkat")

if a + b > c and b + c > a and a + c > b:
            print ("Może być trójkąt")
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    print ("Jest nawet prostokątny")

#if fabs(b-c) < a and a < (b+c):
    #print ("Może być trójkąt")
