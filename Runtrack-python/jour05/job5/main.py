marches = 100
hauteur_cm = 20

def distance_toilettes(marches, hauteur_cm):
    distance_jour = (marches * hauteur_cm) / 100
    distance_semaine = distance_jour * 7
    return f"La distance parcourue en une semaine est de {distance_semaine*2}m"

print(distance_toilettes(marches, hauteur_cm))