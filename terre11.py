import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("Veuillez saisir l'heure en format HH:MM")
else: 
    heure_saisie = arguments[0]
    heure_minute = heure_saisie.split(":")
    if not heure_minute[0].isdigit() or not heure_minute[1].isdigit():
        print("Des nombres au format HH:MM svp.")
    else:
        heure = int(heure_minute[0])
        minute = int(heure_minute[1])
        if not (0 <= heure <= 23 and 0 <= minute <= 59):
            print("Erreur d'arguments.")
        elif heure < 12:
            print(f"{heure:02}:{minute:02} AM")
        elif heure == 0:
            if minute == 0:
                print("12:00 AM")
            else:
                print(f"12:{minute} AM")
        elif heure == 12:
            if minute == 0:
                print(f"12:00 PM")
            else:
                print(f"12:{minute:02} PM")
        else:
            print(f"{heure-12}:{minute:02}PM")
            


