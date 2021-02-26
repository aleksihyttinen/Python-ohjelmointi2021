#Harjoitus 2
#Kirjoita funktio, joka laskee numeroiden määrän luvussa rekursiivisesti.
#Esim. luvun 10253 tulos on 5 ja luvun 42 tulos on 2.

def count_numbers(n):
    if n < 10:
          return 1
    else:
          return 1 + count_numbers(n/10)


def main():
    print(count_numbers(100))

if __name__ == "__main__":
    main()
