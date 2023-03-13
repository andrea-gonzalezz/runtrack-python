def calcule(num1, operateur, num2):
    if operateur == "+":
        return num1 + num2
    elif operateur == "-":
        return num1 - num2
    elif operateur == "*":
        return num1 * num2
    elif operateur == "/":
        return num1 / num2
    else:
        return "Opérateur non reconnu"
    
num1 = int(input("Entrez un nombre: "))
operateur = input("Entrez un opérateur: ")
num2 = int(input("Entrez un nombre: "))


operation = calcule(num1, operateur, num2)
print(operation)