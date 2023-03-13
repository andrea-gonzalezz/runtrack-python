L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def sommes_paires(L):
    somme = 0
    for i in range(len(L)):
        if L[i]%2 == 0:
            somme += L[i]
    return somme

print(sommes_paires(L))