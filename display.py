def afficher_carte(terrain):
    print("\nCarte de la mission :\n")
    for ligne in terrain:
        print("|", end=" ")
        for cellule in ligne:
            print(f"{cellule:^3}", end=" ")
        print("|")
