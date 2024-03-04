import sys
import string

alphabet = string.ascii_lowercase

if len(sys.argv) != 2:
    print("Solution : Utilisez une lettre en minuscule de l'alphabet, le programme terminera pour vous. ")
else: 
    argument = sys.argv[1]
    if len(argument) != 1 or not argument.isalpha():
        print("Une lettre svp.")
    elif not argument.islower():
        print("Une lettre minuscule svp.")
    else:
        index = alphabet.index(argument)
        print("".join(alphabet[index:]))
   
    


