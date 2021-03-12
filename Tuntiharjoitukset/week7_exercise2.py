# Harjoitus 2
# Määritä luokka Point. Point kuvaa pistettä 2-ulotteisessa avaruudessa.
# Mieti mitä jäsenmuuttujia kyseinen luokka tarvitsee ja toteuta ne.
#
# Määritä luokka Rectangle, joka kuvaa nelikulmiota. Rectanglen tulee periytyä
# Shape-luokasta ja se määrittellään kulmapisteiden avulla. Toteuta kulmapisteet
# määrittelmäsi Point-luokkaa käyttäen. Tässä toteutuksessa nelikulmion oletetaan
# aina olevan suorakulmio, mutta ei välttämättä neliö.
# Rectangle-luokassa toteutetaan seuraavat jäsenfunktiot:
# - area: palauttaa nelikulmion pinta-alan. Ylikirjoitetaan Shape-luokan toteutus.
# - width: palauttaa nelikulmion leveyden.
# - height: palauttaa nelikulmion korkeuden.

from week7_exercise1 import Shape 

class Point():
    def __init__(self):
        print("Please enter the x co-ordinate")
        self.x = int(input())
        print("Please enter the y co-ordinate")
        self.y = int(input())

class Rectangle(Shape):
    def isRectangle(a, b, c, d):
        if a.x == c.x and b.x == d.x and a.y == b.y and c.y == d.y:
            rectangle = Rectangle(a, b, c, d)
            return rectangle
        else:
            print("Error, this is not a rectangle or a square!")
            
        
    def __init__(self, a, b, c, d):
        Rectangle.area(self, a, b, c)
        Rectangle.width(self, a, b)
        Rectangle.height(self, a, c)

    def area(self, a, b, c):
        self.width = Rectangle.width(self, a, b)
        self.height = Rectangle.height(self, a, c)
        self.area = self.width * self.height
        return self.area
    
    def width(self, a, b):
        self.width = b.x - a.x
        if self.width < 0:
            self.width = self.width * -1
        return self.width

    def height(self, a, c):
        self.height = a.y - c.y
        if self.height < 0:
            self.height = self.height * -1
        return self.height

def main():
    # a = top-left point        b = top-right point
    
    # c = bottom-left point     d = bottom-right point
    print("Top-left point")
    a = Point()
    print("Top-right point")
    b = Point()
    print("Bottom-left point")
    c = Point()
    print("Bottom-right point")
    d = Point()
    neliö = Rectangle.isRectangle(a, b, c, d)
    print("The width is:", neliö.width)
    print("The height is:", neliö.height)
    print("The area is:",  neliö.area)


if __name__ == "__main__":
    main()