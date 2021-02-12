#Kirjoita funktio, joka laskee parametrina saadun sanan vokaalisen määrän. Vokaaleja
#ovat kirjaimet [a, e, i, o, u, y, ä, ö] (ts. suomen kielen mukaiset vokaalit :).
#Funktio palauttaa vokaalien määrän.

def vocals(word):
    word = str.lower(word)
    vocals = ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö']
    counter = 0
    for letter in word:
        if letter in vocals:
            counter += 1
    return counter
test = "TesTISAna"
print(vocals(test))