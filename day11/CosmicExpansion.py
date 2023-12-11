def findGalaxies(cosmos):
    galaxies = set()
    for y in range(len(cosmos)):
        for x in range(len(cosmos[y])):
            if cosmos[y][x] == '#':
                galaxies.add((y, x))
    return galaxies

def applyHorizontalDrift(cosmos, galaxies, drift):
    horizontalExpands = []
    newGalaxies = set()

    for y in range(len(cosmos)):
        if '#' not in cosmos[y]:
            horizontalExpands.append(y)
    horizontalExpands.reverse()
    for galaxy in galaxies:
        for y in horizontalExpands:
            if galaxy[0] > y:
                galaxy = (galaxy[0] + drift, galaxy[1])
        newGalaxies.add(galaxy)
    return newGalaxies

def applyVerticalDrift(cosmos, galaxies, drift):
    verticalExpands = []
    newGalaxies = set()

    for x in range(len(cosmos[0])):
        insert = True
        for y in cosmos:
            if y[x] == '#':
                insert = False
                break
        if insert: verticalExpands.append(x)
    verticalExpands.reverse()
    for galaxy in galaxies:
        for x in verticalExpands:
            if galaxy[1] > x:
                galaxy = (galaxy[0], galaxy[1] + drift)
        newGalaxies.add(galaxy)
    return newGalaxies

def applyGalaxyDrift(cosmos, galaxies, drift):
    galaxies = applyHorizontalDrift(cosmos, galaxies, drift)
    galaxies = applyVerticalDrift(cosmos, galaxies, drift)
    return galaxies

def calcShortestPathCheckSum(galaxies):
    checksum = 0
    galaxy = galaxies.pop()
    while len(galaxies):
        for otherGalaxy in galaxies:
            checksum += abs(otherGalaxy[0] - galaxy[0]) + abs(otherGalaxy[1] - galaxy[1])
        galaxy = galaxies.pop()
    return checksum

if __name__ == '__main__':
    with open('day11/input.txt') as f:
        cosmos = [line.strip() for line in f]
    galaxies = findGalaxies(cosmos)
    galaxies = applyGalaxyDrift(cosmos, galaxies, 1)
    print('Checksum for shortest path between galaxies is: ' + str(calcShortestPathCheckSum(galaxies)))
    galaxiesP2 = findGalaxies(cosmos)
    galaxiesP2 = applyGalaxyDrift(cosmos, galaxiesP2, 999999)
    print('Checksum for shortest path between galaxies part 2 is: ' + str(calcShortestPathCheckSum(galaxiesP2)))
