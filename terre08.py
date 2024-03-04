import sys


arguments = sys.argv[1:]

if len(arguments) != 2:
    print("Erreur d'arguments.")
else:
    if not all(arg.isdigit() for arg in arguments):
        print("Que des nombres.")
    else:
        chiffre_1 = int(sys.argv[1])
        chiffre_2 = int(sys.argv[2])
        print(chiffre_1**chiffre_2)


