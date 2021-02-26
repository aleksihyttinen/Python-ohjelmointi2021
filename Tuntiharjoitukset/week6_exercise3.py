#Harjoitus 3
#Alla oleva funktio tarkistaa, onko sana palindromi. Kirjoita funktiosta rekursiivinen versio.
#Ratkaisu voi olla helpompi, jos jaat sen useampaan funktioon.

def isPalindrome(word):
   word = word.lower()
   word = "".join(word.split())
   if len(word) < 2:
      return True
   if word[0] != word[-1]:
      return False
   return isPalindrome(word[1:-1])

def main():
   print(isPalindrome("Saippua \nkauppias"))

if __name__ == "__main__":
    main()