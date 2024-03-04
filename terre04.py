import sys


if len(sys.argv) != 2:
    print("Mon rôle est de vous dire si votre chiffre est pair ou impair.")
else:
    argument = sys.argv[1]
    if not argument.lstrip("-").isdigit():
        print("Veuillez saisir un chiffre.")
    else:
        if int(argument)%2==0:
            print("Votre nombre est pair.")
        else:
            print("Votre nombre est impair.")