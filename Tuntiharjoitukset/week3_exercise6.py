sana = input("Syötä sana: ")
tuloste = ""
for kirjain in sana:
    if kirjain in sana:
        if kirjain not in tuloste:
            tuloste += kirjain + ": " + str(sana.count(kirjain)) + ", "
print(tuloste)