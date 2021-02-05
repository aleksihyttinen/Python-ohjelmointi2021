sana = "haloo"
uusisana = ""
laskuri = 0
for x in range(len(sana)):
    if (x%2)==0:
        uusisana += sana[laskuri]
        laskuri += 2
print(uusisana)