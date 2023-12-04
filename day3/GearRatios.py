
gearRatios = {}
def addToGearRatios(x, y, val):
    if (x, y) in gearRatios:
        gearRatios[(x, y)].append(val)
    else:
        gearRatios[(x, y)] = [val]

def sumAllGearRatios():
    sumOfGearRatios = 0
    for l in gearRatios.values():
        if len(l) == 2:
            sumOfGearRatios += l[0] * l[1]
    return sumOfGearRatios


def isPart(schematic, schematicLine, start, end, val):
    start = max(0, start - 1)
    end = min(end, len(schematic[0]) - 1)

    infront = schematic[schematicLine][start]
    behind = schematic[schematicLine][end]
    above = schematic[schematicLine - 1][start:end + 1] if schematicLine > 0 else ''
    below = schematic[schematicLine + 1][start:end + 1] if schematicLine < len(schematic) - 1 else ''
    if not infront.isdigit() and not infront == '.':
        if infront == '*':
            addToGearRatios(start, schematicLine, val)
        return True
    if not behind.isdigit() and not behind == '.':
        if behind == '*':
            addToGearRatios(end, schematicLine, val)
        return True
    for i, c in enumerate(above):
        if not c.isdigit() and not c == '.':
            if c == '*':
                addToGearRatios(i + start, schematicLine - 1, val)
            return True
    for i, c in enumerate(below):
        if not c.isdigit() and not c == '.':
            if c == '*':
                addToGearRatios(i + start, schematicLine + 1, val)
            return True
    return False

def sumAllPartNumbers(schematic):
    sumOfParts = 0
    lineLength = len(schematic[0])

    for i in range(len(schematic)):
        j = 0
        while j < lineLength:
            if schematic[i][j].isdigit():
                start = j
                while j != lineLength and schematic[i][j].isdigit():
                    j += 1
                end = j

                val = int(schematic[i][start:end])
                if isPart(schematic, i, start, end, val):
                    sumOfParts += val
            j += 1
    return sumOfParts


if __name__ == '__main__':
    with open('day3/input.txt') as f:
        schematic = [val.strip() for val in f]

    print('Sum of all parts numbers: ' + str(sumAllPartNumbers(schematic)))
    print('Sum of all gear ratios: ' + str(sumAllGearRatios()))

