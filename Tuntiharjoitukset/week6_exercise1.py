#Harjoitus 1
#Kirjoita rekursiivinen funktio, joka tulostaa Fibonaccin lukujonon n ensimmäistä termiä.

#Fibonaccin lukujono muodostuu seuraavasti:
#F(n) = 0, kun n = 0
#F(n) = 1, kun n = 1
#F(n) = F(n-1) + F(n-2), kun n > 1



def count_fibo(n):
   if n <= 1:
       return(n)
   else:
       return((count_fibo(n-1) + count_fibo(n-2)))

def print_fibo(n):
    for i in range(n):
        print(count_fibo(i))

def main():
    print_fibo(6)

if __name__ == "__main__":
    main()