L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def produit():
    i = 0
    n = 0
    while i < len(L):
        if L[i]>25 and L[i]<90:
            n = n*L[i]
        i += 1