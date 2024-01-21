# een lijst gebruiken in Python
boodschappenlijstje = ["Appels", "Bananen", "Melk", "Brood", "Chocolade"]
print(boodschappenlijstje)

# een item toevoegen aan het einde van een lijst
boodschappenlijstje.append("Eieren")
print(boodschappenlijstje)

# een item verwijderen uit een lijst
boodschappenlijstje.remove("Melk")
print(boodschappenlijstje)

# een item op een specifieke plaats wijzigen
boodschappenlijstje[2] = "Volkorenbrood"
print(boodschappenlijstje)

# de lengte van een lijst ophalen
print(len(boodschappenlijstje))



# index error
my_list = [1, 2, 3]
print(my_list[3])

# type error
my_list = [1, 2, 3]
result = "Sum is: " + my_list
print(result)

# name error
print(non_existent_list)



# sorteren
getallen = [7, 2, 5, 1, 10]

# Sorteer de lijst in oplopende volgorde
getallen.sort()
print("Oplopend gesorteerde lijst:", getallen) # Output: [1, 2, 5, 7, 10]

# Sorteer de lijst in aflopende volgorde
getallen.sort(reverse=True)
print("Aflopend gesorteerde lijst:", getallen) # Output: [10, 7, 5, 2, 1]



# itereren in een lijst:
def toon_lijst(lijst):
    for item in lijst:
        print(item)

mijn_lijst = [1, 2, 3, 4, 5]
toon_lijst(mijn_lijst)



# itereren over een string:
def toon_karakters(woord):
    for karakter in woord:
        print(karakter)

toon_karakters("CodeFever")



# een lus vroeger stoppen via break:
mijn_lijst = [1, 3, 5, 7, 9, 10, 11, 13, 15]

for nummer in mijn_lijst:
    if nummer % 2 == 0:
        print("Het eerste even getal is gevonden:", nummer)
        break
