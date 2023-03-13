L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def max_min(L):
    max = L[0]
    min = L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
        if L[i] < min:
            min = L[i]
    return max, min

print(max_min(L))