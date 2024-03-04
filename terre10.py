import sys

from sympy import *

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("Erreur d'arguments.")
else:
    if not all(arg.isdigit() for arg in arguments):
        print("Qu'un chiffre.")
    else:
        chiffre = int(sys.argv[1])
        if chiffre <= 1:
            print("Le nombre doit être supérieur à 1.")
        else:
            if isprime(chiffre):
                print("C'est un nombre premier.")
            else:
                print("Ce n'est pas un nombre premier.")
                
                
            
            
        