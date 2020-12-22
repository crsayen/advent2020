from copy import deepcopy
from itertools import permutations
cube = []
sideLen = None
with open('input17') as f:
    layer = []
    for line in f:
        line = line.replace('\n', '')
        layer.append([c == '#' for c in line])
    sideLen = len(layer)
    cube = [layer, *([[[False] * sideLen] * sideLen] * (sideLen - 1))]


def getNeighbors(coords):
    neighbors = []
    for p in [
        [0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,1,0],[1,0,1],
        [0,0,-1],[0,-1,0],[0,-1,-1],[-1,0,0],[-1,-1,0],[-1,0,-1],
        [0,-1,1],[-1,1,0],[-1,0,1],
        [0,1,-1],[1,-1,0],[1,0,-1],
        [1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1],
    ]:
        newCoords = deepcopy(coords)
        for i,n in enumerate(p):
            newCoords[i] += n
        if all(c < sideLen - 1 and c > -1 for c in newCoords):
            neighbors.append(deepcopy(newCoords))
    return neighbors

for cyclen in range(6):
    print(f'cycle: {cyclen}')
    newCube = deepcopy(cube)
    for x in range(sideLen):
        for y in range(sideLen):
            for z in range(sideLen):
                nActiveNeighbors = 0
                for [nbx, nby, nbz] in getNeighbors([x, y, z]):
                    if cube[nbx][nby][nbz]:
                        nActiveNeighbors += 1
                if cube[x][y][z]:
                    if nActiveNeighbors not in [2,3]:
                        newCube[x][y][z] == False
                else:
                    if nActiveNeighbors == 3:
                        print(f'switching: {[x,y,z]}')
                        newCube[x][y][z] == True
    """ if cyclen == 5:
        for lyr in newCube:
            for ln in lyr:
                print(ln)
            print('\n') """
    cube = deepcopy(newCube)

count = 0

for x in range(sideLen):
    for y in range(sideLen):
        for z in range(sideLen):
            if cube[x][y][z]: count += 1

print(count)

