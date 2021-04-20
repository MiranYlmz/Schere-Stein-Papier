import random

print("Spiele Schere-Stein-Papier mit mir!")
print("Bitte wähle: Schere (s), Stein (r) oder Papier (p)")

eingabe = input("Dein Element: ")
# print(eingabe)

spielzeuge = ["s", "p", "r"]
if eingabe in spielzeuge:

    computer = random.choice(spielzeuge)
    print("Computer " + computer)

    if computer == eingabe:
        print("Untentschieden")
    elif computer == "s" and eingabe == "p":
        print("Du hast verloren!")
    elif computer == "s" and eingabe == "r":
        print("Du hast gewonnen!")
    elif computer == "r" and eingabe == "p":
        print("Du hast gewonnen!")
    elif computer == "r" and eingabe == "s":
        print("Du hast verloren!")
    elif computer == "p" and eingabe == "s":
        print("Du hast gewonnen!")
    elif computer == "p" and eingabe == "r":
        print("Du hast verloren")
else:
    print("ungültige Eingabe, bitte gebe s,r oder p ein !")
