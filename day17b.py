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
    unHyperCube = tuple(map(tuple, map(tuple, [*padtop, layer, *padbottom])))
    padhyper1 = [[[[False] * sideLen] * sideLen] * sideLen] * (sideLen // 2)
    padhyper2 = [[[[False] * sideLen] * sideLen] * sideLen] * ((sideLen // 2) - 1)
    cube = [*padhyper1, unHyperCube, *padhyper2]

def getNeighbors(coords):
    neighbors = []
    for p in product((-1, 0, 1), repeat=4):
        newCoords = [None, None, None, None]
        for i,n in enumerate(p):
            newCoords[i] = coords[i] + n
        try:
            cube[newCoords[0]][newCoords[1]][newCoords[2]][newCoords[3]]
            if coords != newCoords: neighbors.append(newCoords)
        except: pass
    return neighbors

for cyclen in range(6):
    newCube = list(list(list(list(list(row) for row in plane)) for plane in unhyper) for unhyper in cube)
    for (x, y, z, w) in product(range(sideLen), repeat=4):
        nActiveNeighbors = 0
        for [nbx, nby, nbz, nbw] in getNeighbors([x, y, z, w]):
            if cube[nbx][nby][nbz][nbw]:
                nActiveNeighbors += 1
        if cube[x][y][z][w]:
            newCube[x][y][z][w] = nActiveNeighbors in [2,3]
        else:
            newCube[x][y][z][w] = nActiveNeighbors == 3
    cube = tuple(tuple(tuple(tuple(tuple(row) for row in plane)) for plane in unhyper) for unhyper in newCube)

count = 0

for (x, y, z, w) in product(range(sideLen), repeat=4):
    if cube[x][y][z][w]: count += 1

print(count)

