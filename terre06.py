import sys

arguments = sys.argv[1:]

if len(arguments) < 1:
    print("Erreur d'arguments.")
else:
    if not all(arg.isalpha() for arg in arguments):
        print("Veuillez saisir une chaîne de caractères")
    else:
        arguments = ' '.join(arguments)
        inverse = ""
        count = len(arguments)
        while count > 0:
            inverse += arguments[count-1]
            count -= 1
        print(inverse)
            
            