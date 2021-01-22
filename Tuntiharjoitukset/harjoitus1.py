# Jos pieni alkukirjain muuta isoksi
# Seuraa kirjaimellisesti tehtävänantoa
syote = input("Mikä sinun nimesi on? ")
if syote.islower():
    print("Sinun nimesi on", syote.capitalize())
else:
    print("Sinun nimesi on", syote)

# Yksinkertainen versio, ei if tarkistusta
syote = input("Mikä sinun nimesi on? ")
print("Sinun nimesi on " + syote.capitalize())
