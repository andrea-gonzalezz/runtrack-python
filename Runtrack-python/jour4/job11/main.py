L = [7, 11, 42, 39, 2]

def incremente_liste(L):
    for i in range(len(L)):
        L[i] += 1
    return L

print(incremente_liste(L))
 