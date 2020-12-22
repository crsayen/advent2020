from itertools import product
cube = None
sideLen = 20
with open('input17') as f:
    layer = []
    for line in f:
        line = line.replace('\n', '')
        padrow = [False] * ((sideLen - len(line)) // 2)
        layer.append( [*padrow, *[c == '#' for c in line], *padrow])
    padlayer = [[False] * sideLen] * ((sideLen - len(layer)) // 2)
    layer = [*padlayer, *layer, *padlayer]
    padtop = [[[False] * sideLen] * sideLen] * (sideLen // 2)
    padbottom = [[[False] * sideLen] * sideLen] * ((sideLen // 2) - 1)
    cube = tuple(map(tuple, map(tuple, [*padtop, layer, *padbottom])))

def getNeighbors(coords):
    neighbors = []
    for p in product((-1, 0, 1), repeat=3):
        newCoords = [None, None, None]
        for i,n in enumerate(p):
            newCoords[i] = coords[i] + n
        try:
            cube[newCoords[0]][newCoords[1]][newCoords[2]]
            if coords != newCoords: neighbors.append(newCoords)
        except: pass
    return neighbors

for cyclen in range(6):
    newCube = list(list(list(list(row) for row in plane)) for plane in cube)
    for (x, y, z) in product(range(sideLen), repeat=3):
        nActiveNeighbors = 0
        for [nbx, nby, nbz] in getNeighbors([x, y, z]):
            if cube[nbx][nby][nbz]:
                nActiveNeighbors += 1
        if cube[x][y][z] == True:
            newCube[x][y][z] = nActiveNeighbors in [2,3]
        else:
            newCube[x][y][z] = nActiveNeighbors == 3
    cube = tuple(tuple(tuple(tuple(row) for row in plane)) for plane in newCube)

count = 0

for (x, y, z) in product(range(sideLen), repeat=3):
    if cube[x][y][z]: count += 1

print(count)

