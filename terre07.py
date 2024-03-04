import sys

argument = sys.argv[1:]

if len(argument) > 1:
    print("Qu'un argument permis dans ce script.")

string = argument[0]

# Faire une boucle pour compter chaque caracteres d'une chaine

caractere = 0

for lettre in string:
    if lettre.isalpha():
        caractere = caractere+1
    else:
        print("Erreur")
        
print(caractere)



