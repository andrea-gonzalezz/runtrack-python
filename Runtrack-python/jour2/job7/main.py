def developpeur(langage):
    if langage == "javascript":
        print("Tu es un developpeur web")
    elif langage == "python":
        print("Tu es un developpeur IA")
    elif langage == "java":
        print("Tu es un developpeur logiciel")
    elif langage == "reactjs":
        print("Tu es un developpeur mobile")
    else:
        print("Un jour tu seras le meilleur developpeur du monde")

langage = input("Quel est ton langage de programmation préféré? ")
print(developpeur(langage))