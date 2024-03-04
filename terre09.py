import sys

argument = sys.argv[1:]

if len(argument) != 1:
    print("Erreur d'arguments.")
else:
    if not all(arg.isdigit() for arg in argument):
        print("Qu'un chiffre.")
    else:
        chiffre = int(sys.argv[1])
    print(chiffre**0.5)

    