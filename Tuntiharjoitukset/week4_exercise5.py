#Kirjoita funktio, joka tarkistaa, onko sana palindromi. Palindromi on sana, joka on sama
#kirjoitettuna oikein ja väärin päin. Sanan kirjainten koolla ei ole merkitystä.
#Oletus: Sana ei sisällä white space -merkkejä (rivinvaihto, välilyönti, tabulaattori).
#Bonus: Sana saa sisältää white space -merkkejä, mutta niitä ei oteta huomioon tarkistettaessa,
#onko sana palindromi.

def palindrome(word):
    word = str.lower(word)
    word = ''.join(word.split()) #jos haluaa whitespacet näkyviin lopputulosteeseen, tallenna alkuperäinen sana erilliseen muuttujaan
    reversedword = word[::-1]
    if reversedword == word:
        print(word.capitalize(), "is a palindrome.")
    else:
        print(word.capitalize(), "is not a palindrome.")

test = "sa ippu akaup pia\n s"
palindrome(test)