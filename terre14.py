import sys

arguments = sys.argv[1:]

if len(arguments) < 3:
    print("Veuillez mettre 3 arguments ou +.")
else:
    if not all(arg.isdigit() for arg in arguments):
        print("Veuillez mettre 3 nombres ou +.")
    else:
        nombres = [int(arg) for arg in arguments]
        triee = True
        for i in range(len(nombres)-1):
            if nombres[i] > nombres[i+1]:
                triee = False
                break
            
if triee:
    print("Triée")
else:
    print("Pas Triée")
            
                
                    
                    
