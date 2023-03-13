def triangle_rectangle(a,b,c):
    if a == b or a == c or b == c:
        print("Le triangle est isocèle")
    if a == b and b == c:
        print("Le triangle est équilatéral")
    if a**2 + b**2 == c**2:
        print("Le triangle est rectangle")
    else:
        print(None)

a = int(input("Longueur du premier côté: "))
b = int(input("Longueur du deuxième côté: "))
c = int(input("Longueur du troisième côté: "))

print(triangle_rectangle(a,b,c))
