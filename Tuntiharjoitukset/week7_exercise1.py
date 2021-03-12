# Harjoitus 1
# Määritä luokka Shape, josta peritään myöhemmin luokat Circle ja Rectangle.
# Shape-luokassa määritetään jäsenfunktio area, joka ylikirjoitetaan lapsiluokissa.
# Shape-luokan toteutuksessa riittää, että kyseinen funktio palauttaa arvon None
# (koska pinta-ala on mieletön käsite abstraktille kuviolle).
#
# Määritä luokka Circle, joka periytyy luokasta Shape. Circle-luokka kuvaa ympyrää
# ja sen tulisi määrittää seuraavat jäsenfunktiot:
# - area: palauttaa ympyrän pinta-alan. Ylikirjoitetaan kantaluokan toteutus
# - circumference: palauttaa ympyrän ympärysmitan.
# Mieti mitä jäsenmuuttujia luokka tarvitsee ominaisuuksien toteuttamiseksi
# ja määritä ne.
import math

class Shape:
    def __init__(self):
        self.area = None

class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            print("The radius can't be negative")
        else:
            Circle.area(self, radius)
            Circle.circumference(self, radius)

    def area(self, radius):
        self.area = (math.pi * (radius ** 2))
        return self.area
    
    def circumference(self, radius):
        self.circumference = (2 * math.pi * radius)
        return self.circumference       

def main():
    a = Shape()
    b = Circle(1)
    print(b.circumference)
    print(b.area)
    

if __name__ == "__main__":
    main()