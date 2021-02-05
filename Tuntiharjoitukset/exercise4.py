syote = ""
tuloste = []
syote = input("Syötä sanoja, pysäytä sovellus sanalla stop: ")
while syote != "stop":
    if syote == "stop":
        break
    else:
        tuloste.append(syote)
        syote = input("Syötä sanoja, pysäytä sovellus sanalla stop: ")
print(", ".join(tuloste))