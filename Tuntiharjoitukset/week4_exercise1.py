#Kirjoita funktio, joka ottaa parametrina määrittämättömän määrän numeroita ja 
#kertoo ne yhteen. Funktio palauttaa tuloksen paluuarvona.

def multiply(list):
    returnnumber = list[0]
    for number in list:
        returnnumber = returnnumber * number
    return returnnumber

test = [1, 2, 3, 4, 5]
print(multiply(test))