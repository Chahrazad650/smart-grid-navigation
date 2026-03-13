import random
import os
import heapq


# Affichage de la carte dans la console
def afficher_carte(terrain):
    print("\nCarte de la mission :\n")
    for ligne in terrain:
        print("|", end=" ")
        for cellule in ligne:
            print(f"{cellule:^3}", end=" ")
        print("|")


# Création des murs (obstacles)
def inserer_murs(terrain, proportion):
    lignes, colonnes = len(terrain), len(terrain[0])
    total = lignes * colonnes
    nb_murs = int(total * proportion)

    positions = set()
    while len(positions) < nb_murs:
        x, y = random.randint(0, lignes - 1), random.randint(0, colonnes - 1)
        if terrain[x][y] == ".":
            terrain[x][y] = "#"
            positions.add((x, y))
    return positions


# Obtenir la taille du terrain depuis l'utilisateur
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
            print("Saisie invalide, réessaye !")


# Niveau de difficulté (nombre d'obstacles)
def choisir_difficulte():
    print("\n🎮 Choisis ton niveau de mission :")
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


# Demande à l'utilisateur ou choix aléatoire pour START et GOAL
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


def selection_aleatoire(grille):
    def point_vide():
        while True:
            x, y = random.randint(0, len(grille) - 1), random.randint(0, len(grille[0]) - 1)
            if grille[x][y] == ".":
                return (x, y)

    debut = point_vide()
    fin = point_vide()
    while fin == debut:
        fin = point_vide()
    return debut, fin


def selection_manuelle(grille):
    def saisir_point(message):
        while True:
            try:
                x = int(input(f"{message} - ligne (0 à {len(grille) - 1}) : "))
                y = int(input(f"{message} - colonne (0 à {len(grille[0]) - 1}) : "))
                if 0 <= x < len(grille) and 0 <= y < len(grille[0]) and grille[x][y] == ".":
                    return (x, y)
                else:
                    print("Position invalide ou déjà occupée ! ")
            except ValueError:
                print("Entrée invalide ! ")
    debut = saisir_point("Coordonnées du point de départ")
    fin = saisir_point("Coordonnées du point d'arrivée")
    while fin == debut:
        print("Départ et arrivée doivent être différents ! ")
        fin = saisir_point("Coordonnées du point d'arrivée")
    return debut, fin


# Calcul de distance estimée (heuristique de Manhattan)
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Implémentation de l'algorithme A*
def astar(terrain, depart, objectif):
    mouvements = [(0,1), (1,0), (0,-1), (-1,0)]
    file_ouverte = []
    heapq.heappush(file_ouverte, (0 + manhattan(depart, objectif), 0, depart))
    origine = {}
    couts = {depart: 0}

    while file_ouverte:
        _, cout_actuel, position = heapq.heappop(file_ouverte)

        if position == objectif:
            chemin = []
            while position in origine:
                chemin.append(position)
                position = origine[position]
            chemin.reverse()
            return chemin

        for dx, dy in mouvements:
            voisin = (position[0] + dx, position[1] + dy)
            if 0 <= voisin[0] < len(terrain) and 0 <= voisin[1] < len(terrain[0]):
                if terrain[voisin[0]][voisin[1]] == "#":
                    continue
                tentative = cout_actuel + 1
                if voisin not in couts or tentative < couts[voisin]:
                    couts[voisin] = tentative
                    score = tentative + manhattan(voisin, objectif)
                    heapq.heappush(file_ouverte, (score, tentative, voisin))
                    origine[voisin] = position

    return None


# Lancement du jeu
def demarrer_simulation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===  Système A* : Mission Pathfinder ===\n")
    lignes, colonnes = demander_dimensions()
    niveau = choisir_difficulte()

    carte = [["." for _ in range(colonnes)] for _ in range(lignes)]
    inserer_murs(carte, niveau)

    start, goal = definir_positions(carte)
    carte[start[0]][start[1]] = "S"
    carte[goal[0]][goal[1]] = "G"

    # Trouver un chemin
    itineraire = astar(carte, start, goal)

    if itineraire:
        for (x, y) in itineraire:
            if carte[x][y] == ".":
                carte[x][y] = "*"
        print("\nChemin trouvé !")
        print("Itinéraire de S à G :")
        print(" -> ".join([f"{pos}" for pos in [start] + itineraire + [goal]]))
    else:
        print("\n Aucun chemin trouvé entre S et G.")

    afficher_carte(carte)


if __name__ == "__main__":
    demarrer_simulation()