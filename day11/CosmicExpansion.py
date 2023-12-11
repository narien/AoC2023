def expandCosmos(cosmos):
    horizontalExpands = []
    for y in range(len(cosmos)):
        if '#' not in cosmos[y]:
            horizontalExpands.append(y)
    horizontalExpands.reverse()
    for y in horizontalExpands:
        cosmos.insert(y, cosmos[y])

    verticalExpands = []
    for x in range(len(cosmos[0])):
        insert = True
        for y in cosmos:
            if y[x] == '#':
                insert = False
                break
        if insert: verticalExpands.append(x)
    verticalExpands.reverse()
    for x in verticalExpands:
        for y in range(len(cosmos)):
            cosmos[y] = cosmos[y][0:x] + '.' + cosmos[y][x:]

def findGalaxies(cosmos):
    galaxies = set()
    for y in range(len(cosmos)):
        for x in range(len(cosmos[y])):
            if cosmos[y][x] == '#':
                galaxies.add((y, x))
    return galaxies

def calcShortestPathCheckSum(galaxies, cosmos):
    checksum = 0
    galaxy = galaxies.pop()
    while len(galaxies):
        for otherGalaxy in galaxies:
            checksum += abs(galaxy[0] - otherGalaxy[0]) + abs(galaxy[1] - otherGalaxy[1])
        galaxy = galaxies.pop()
    return checksum

if __name__ == '__main__':
    with open('day11/input.txt') as f:
        cosmos = [line.strip() for line in f]
    expandCosmos(cosmos)
    galaxies = findGalaxies(cosmos)
    print('Checksum for shortest path between galaxies is: ' + str(calcShortestPathCheckSum(galaxies, cosmos)))
