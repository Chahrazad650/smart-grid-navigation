from grid import selection_aleatoire, selection_manuelle


def demander_dimensions():
    while True:
        try:
            l = int(input("Nombre de lignes (>2) : "))
            c = int(input("Nombre de colonnes (>2) : "))
            if l > 2 and c > 2:
                return l, c
            else:
                print("Valeurs trop petites !")
        except ValueError:
            print("Saisie invalide, réessaie !")


def choisir_difficulte():
    print("\nChoisis ton niveau de mission :")
    print("1. Facile (10% de murs)")
    print("2. Moyen (30% de murs)")
    print("3. Difficile (50% de murs)")

    while True:
        niv = input("Ton choix (1/2/3) : ")
        if niv == "1":
            return 0.10
        elif niv == "2":
            return 0.30
        elif niv == "3":
            return 0.50
        else:
            print("Choix incorrect, recommence !")


def definir_positions(grille):
    print("\n🔧 Méthode de placement des points START et GOAL :")
    print("1. Automatique (aléatoire)")
    print("2. Manuelle (saisie des coordonnées)")

    while True:
        choix = input("Ton choix (1/2) : ")
        if choix == "1":
            return selection_aleatoire(grille)
        elif choix == "2":
            return selection_manuelle(grille)
        else:
            print("Saisie invalide !")
