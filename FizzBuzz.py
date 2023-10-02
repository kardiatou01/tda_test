class FizzBuzz:
    @staticmethod
    def affiche(n1, n2):
        resultat = ""

        for i in range(n1, n2 + 1):
            if i % 15 == 0:
                resultat += "FrisBee"
            elif i % 5 == 0:
                resultat += "Buzz"
            elif i % 3 == 0:
                resultat += "Fizz"
            else:
                resultat += str(i)

        return resultat


# Appel de la méthode affiche avec deux nombres en entrée
FizzBuzz.affiche(5, 10)  # Affiche "BuzzFizz78FizzBuzz"
FizzBuzz.affiche(10, 16) # Affiche "Buzz11Fizz1314FrisBee16"    

    