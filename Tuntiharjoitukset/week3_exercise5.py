lukujenmaara = int(input("Monenko luvun keskiarvon haluat laskea? "))
luvut = 0
index = 0
while index < lukujenmaara:
    luvut += (int(input("Syötä luvut: ")))
    index += 1
tulos = luvut / lukujenmaara
print("Lukujesi keskiarvo on: ", tulos)
