L = [1,2,5,6,8,9,10]

def remplace(L):
    L[0],L[-1] = L[-1],L[0]    
    print(L)

remplace(L)