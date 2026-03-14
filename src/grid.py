import random
from config import EMPTY, WALL


def creer_grille(lignes, colonnes):
    return [[EMPTY for _ in range(colonnes)] for _ in range(lignes)]


def inserer_murs(terrain, proportion):
    lignes, colonnes = len(terrain), len(terrain[0])
    total = lignes * colonnes
    nb_murs = int(total * proportion)

    positions = set()
    while len(positions) < nb_murs:
        x = random.randint(0, lignes - 1)
        y = random.randint(0, colonnes - 1)

        if terrain[x][y] == EMPTY:
            terrain[x][y] = WALL
            positions.add((x, y))

    return positions


def selection_aleatoire(grille):
    def point_vide():
        while True:
            x = random.randint(0, len(grille) - 1)
            y = random.randint(0, len(grille[0]) - 1)
            if grille[x][y] == EMPTY:
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

                if 0 <= x < len(grille) and 0 <= y < len(grille[0]) and grille[x][y] == EMPTY:
                    return (x, y)
                else:
                    print("Position invalide ou déjà occupée !")
            except ValueError:
                print("Entrée invalide !")

    debut = saisir_point("Coordonnées du point de départ")
    fin = saisir_point("Coordonnées du point d'arrivée")

    while fin == debut:
        print("Départ et arrivée doivent être différents !")
        fin = saisir_point("Coordonnées du point d'arrivée")

    return debut, fin
