import sys

if len(sys.argv) != 3:
    print("Veuillez saisir uniquement 2 nombres.")
else: 
    argument_1 = sys.argv[1]
    argument_2 = sys.argv[2]
    if not (argument_1.isdigit() and argument_2.isdigit()):
        print("Uniquement des nombres.")
    else:
        argument_1 = int(argument_1)
        argument_2 = int(argument_2)
        if argument_2 == 0:
            print("Le diviseur ne peut pas être égal à zéro.")
        elif argument_1 < argument_2:
            print("Le premier chiffre ne peut pas inférieur ou égal au diviseur.")
        else:
            quotient = argument_1 // argument_2
            reste = argument_1 % argument_2
            print("Resultat : " + str(quotient))
            print("Reste : " + str(reste))

            