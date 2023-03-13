def positif_negatif(nombre):
    if nombre > 0:
         print('Le nombre est positif')
    else:
         print('Le nombre est négatif')
    
nombre = int(input("Entrez un nombre: "))
print(positif_negatif(nombre))
