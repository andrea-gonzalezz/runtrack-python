alphabet = "abcdefghijklmnopqrstuvwxyz"

def pyramide(alphabet):
    for i in range(len(alphabet)):
        print(alphabet[:i+1])

pyramide(alphabet)