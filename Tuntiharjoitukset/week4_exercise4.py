#Kirjoita funktio, joka laskee parametrina välitetyn positiivisen kokonaisluvun
#kertoman. Toteuta myös virheiden käsittely.
#Määritelmä: "Positiivisen kokonaisluvun n kertoma on luvun n ja kaikkien sitä pienempien 
#positiivisten kokonaislukujen tulo, ja se merkitään n!."

def factorial(number):
    index = number - 1
    count = number
    while index != 1:
        count = count * index
        index = index - 1
    return count

test = 6
print("The factorial of", test, "is", factorial(test))