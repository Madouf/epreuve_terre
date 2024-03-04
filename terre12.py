import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    print("Veuillez saisir l'heure au format HH:MM AM/PM")
else:
    heure_saisie = " ".join(arguments)
    heure_minute_meridiem = heure_saisie.split(" ")
    heure_minute = heure_minute_meridiem[0]
    meridiem = heure_minute_meridiem[1]

    heure_minute_split = heure_minute.split(":")
    if len(heure_minute_split) != 2:
        print("Erreur d'arguments.")
    else:
        heure = int(heure_minute_split[0])
        minute = int(heure_minute_split[1])
        if not (0 <= heure <= 23 and 0 <= minute <= 59):
            print("Erreur d'arguments.")
        else:
            if meridiem not in ["AM", "PM"]:
                print("Erreur d'arguments.")
            else:
                if heure == 12 and minute == 0:
                    if meridiem == "AM":
                        print("00:00")
                    else:
                        print("12:00")
                else:
                    if meridiem == "PM":
                        heure += 12
                    print(f"{heure:02}:{minute:02}")
