L = [8, 24,48,2,16]
def multiples_trois(L):
    compteur = 0
    for i in range(len(L)):
        if L[i]%3 == 0:
            compteur += 1
    return compteur
            
multiples = multiples_trois(L)
print(multiples)