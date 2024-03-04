import sys

arguments = sys.argv[1:]

if len(arguments) != 3:
    print("Veuillez mettre 3 arguments.")
else:
    if not all(arg.isdigit() for arg in arguments):
        print("Veuillez mettre 3 nombres.")
    else:
        num1 = int(arguments[0])
        num2 = int(arguments[1])
        num3 = int(arguments[2])
        
        if num1 == num2 == num3:
            print("Erreur, nombres identiques.")
        
        else:
  
            if (num2 < num1 < num3) or (num3 < num1 < num2):
                num_milieu = num1
                print(num1)
            elif (num3 < num2 < num1) or (num1 < num2 < num3):
                num_milieu = num2
                print(num2)
            else:
                num_milieu = num3
                print(num3)
            
            
            
        
            
        
            
            
        
   