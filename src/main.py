import os

from config import START, GOAL, PATH, EMPTY
from display import afficher_carte
from grid import creer_grille, inserer_murs
from input_handler import demander_dimensions, choisir_difficulte, definir_positions
from pathfinding import astar


def demarrer_simulation():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Système A* : Mission Pathfinder ===\n")

    lignes, colonnes = demander_dimensions()
    niveau = choisir_difficulte()

    carte = creer_grille(lignes, colonnes)
    inserer_murs(carte, niveau)

    start, goal = definir_positions(carte)
    carte[start[0]][start[1]] = START
    carte[goal[0]][goal[1]] = GOAL

    itineraire = astar(carte, start, goal)

    if itineraire:
        for x, y in itineraire:
            if carte[x][y] == EMPTY:
                carte[x][y] = PATH

        print("\nChemin trouvé !")
        print("Itinéraire de S à G :")
        print(" -> ".join([f"{pos}" for pos in [start] + itineraire + [goal]]))
    else:
        print("\nAucun chemin trouvé entre S et G.")

    afficher_carte(carte)


if __name__ == "__main__":
    demarrer_simulation()
