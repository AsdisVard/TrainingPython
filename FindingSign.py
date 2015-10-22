__author__ = 'asdis'
# napisz funkcje, ktora ma policzyc ile razy jest dany znak w danym stringu i ZWROCIC ta ilosc

def finding (sign = "#", word = "Ala#ma#kota"):
    i = 0
    count = 0
    while i < word.__len__():
        if word[i] == sign:
            count += 1
        i += 1
    return count

print(finding("k", "m"))
