ma_string = "Je m'appelle Dede"


compteur = 0

for lettres in ma_string:
    if lettres == "e":
        compteur += 1


if compteur > 0:
    print(f"Le caractère est présent {compteur} fois")
else:
    print(f"Le caractère est introuvable")


