#Kirjoita funktio, joka palauttaa suurimman luvun, mikä on tallennettu parametrina
#saatuun tietorakenteeseen. Mieti myös sopiva arvo palautettavaksi siinä tapauksessa, että 
#tietorakenne ei sisällä mitään lukuja.
#Toteuta myös vastaava funktio, mikä palauttaa pienimmän luvun tietorakenteessa.

def max(tuple):
    highest = tuple[0]
    for number in tuple:
        if number > highest:
            highest = number
    return highest

def min(tuple):
    lowest = tuple[0]
    for number in tuple:
        if number < lowest:
            lowest = number
    return lowest

test = [1, 2, 3, 4, -5, 10]
print("The highest number in ths list is:", max(test))
print("The lowest number in this list is:", min(test))