lista = [1, 2, 5, 8, 3, 6, 9, 10, -2]
parilliset = 0
parittomat = 0
for x in lista:
    if x % 2 == 0:
        parilliset += 1
    else:
        parittomat += 1
print("parilliset: ", parilliset, "\nparittomat: ", parittomat)