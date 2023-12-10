def findAnimalPos(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'S':
                return y, x
            
def findLoopStart(y, x, map):
    mapLenY = len(map)
    mapLenX = len(map[0])
    if y > 0:
        if map[y-1][x] in ['|', '7', 'F']:
            return y-1, x, 'south'
    if x > 0:
        if map[y][x-1] in ['-', 'L', 'F']:
            return y, x-1, 'east'
    if x < mapLenX - 1:
        if map[y][x+1] in ['-', 'J', '7']:
            return y, x+1, 'west'
    if y < mapLenY - 1:
        if map[y+1][x] in ['|', 'L', 'J']:
            return y+1, x, 'north'

def nextPos(y, x, cameFrom, map):
    if map[y][x] == '|':
        return (y-1, x, 'south') if cameFrom == 'south' else (y+1, x, 'north')
    elif map[y][x] == '-':
        return (y, x+1, 'west') if cameFrom == 'west' else (y, x-1, 'east')
    elif map[y][x] == 'L':
        return (y-1, x, 'south') if cameFrom == 'east' else (y, x+1, 'west')
    elif map[y][x] == 'J':
        return (y, x-1, 'east') if cameFrom == 'north' else (y-1, x, 'south')
    elif map[y][x] == '7':
        return (y, x-1, 'east') if cameFrom == 'south' else (y+1, x, 'north')
    elif map[y][x] == 'F':
        return (y, x+1, 'west') if cameFrom == 'south' else (y+1, x, 'north')

def findLoopLength(y, x, cameFrom, map):
    stepsTaken = 1 # start one step from S
    while True:
        y, x, cameFrom = nextPos(y, x, cameFrom, map)
        stepsTaken += 1
        if map[y][x] == 'S': 
            break
    return stepsTaken


if __name__ == '__main__':
    with open('day10/input.txt') as f:
        map = [line.strip() for line in f]
    aY, aX = findAnimalPos(map)
    y, x, cameFrom = findLoopStart(aY, aX, map)
    print('Furthest part from start is: ' + str(int(findLoopLength(y, x, cameFrom, map) / 2)))
