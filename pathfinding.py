import heapq
from config import WALL

#Implémentation de A*
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(terrain, depart, objectif):
    mouvements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    file_ouverte = []

    heapq.heappush(file_ouverte, (manhattan(depart, objectif), 0, depart))

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
                if terrain[voisin[0]][voisin[1]] == WALL:
                    continue

                tentative = cout_actuel + 1

                if voisin not in couts or tentative < couts[voisin]:
                    couts[voisin] = tentative
                    score = tentative + manhattan(voisin, objectif)
                    heapq.heappush(file_ouverte, (score, tentative, voisin))
                    origine[voisin] = position

    return None
