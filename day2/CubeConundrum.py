from functools import reduce

def sumPossibleGameIds(games):
    maxCubes = {'red': 12, 'green': 13, 'blue': 14}
    gameIdSum = 0
    for game in games:
        valid = True
        game = game.split(':')
        gameId = int(game[0].split()[1])

        sets = game[1].split(';')
        for set in sets:
            cubes = [cubes.strip() for cubes in set.split(',')]
            for cube in cubes:
                nbr, color = cube.split()
                nbr = int(nbr)
                if  nbr > maxCubes[color]:
                    valid = False
        if valid:
            gameIdSum += gameId

    return gameIdSum

def sumLeastNbrOfCubes(games):
    sumLeastCubesPower = 0
    for game in games:
        leastNbrOfCubes = {'red': 0, 'green': 0, 'blue': 0}
        game = game.split(':')
        # gameId = int(game[0].split()[1])

        sets = game[1].split(';')
        for set in sets:
            cubes = [cubes.strip() for cubes in set.split(',')]
            for cube in cubes:
                nbr, color = cube.split()
                nbr = int(nbr)

                if  nbr > leastNbrOfCubes[color]:
                    leastNbrOfCubes[color] = nbr

        sumLeastCubesPower += reduce((lambda x, y: x * y), leastNbrOfCubes.values())
    return sumLeastCubesPower


if __name__ == '__main__':
    with open('day2/input.txt') as f:
        games = [val.strip() for val in f]

    print('Sum of valid gameIds: ' + str(sumPossibleGameIds(games)))
    print('Sum of least nbr of cubes: ' + str(sumLeastNbrOfCubes(games)))
