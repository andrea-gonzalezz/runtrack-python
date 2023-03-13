L = [10,20,30,20,10,50,60,40,80,50,40]

def mylen(L):
    count = 0
    for i in L:
        count += 1
    return count



def myappend(i, L):  
    nouvelle_L = L.copy()
    nouvelle_L[mylen(nouvelle_L):] = [i] 
    return nouvelle_L

def supprimer_doublons(L):
    nouvelle_L = []
    for i in L:
        if i not in nouvelle_L:
            nouvelle_L = myappend(i, nouvelle_L)
    return nouvelle_L

print(supprimer_doublons(L))