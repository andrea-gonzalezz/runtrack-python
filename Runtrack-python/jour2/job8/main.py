def fruits_saisons(type, saison):
    if type == "fruits" and saison =="hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise et cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legumes" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Je ne connais pas ce type de fruit ou légume")

type = input("Fruits ou légumes? ")
saison = input("Hiver ou été? ")
print(fruits_saisons(type, saison))