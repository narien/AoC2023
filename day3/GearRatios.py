

def isPart(schematic, schematicLine, start, end):
    start = max(0, start - 1)
    end = min(end, len(schematic[0]) - 1)

    infront = schematic[schematicLine][start]
    behind = schematic[schematicLine][end]
    above = schematic[schematicLine - 1][start:end + 1] if schematicLine > 0 else ''
    below = schematic[schematicLine + 1][start:end + 1] if schematicLine < len(schematic) - 1 else ''
    if not infront.isdigit() and not infront == '.':
        return True
    if not behind.isdigit() and not behind == '.':
        return True
    for c in above:
        if not c.isdigit() and not c == '.':
            return True
    for c in below:
        if not c.isdigit() and not c == '.':
            return True

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

                if isPart(schematic, i, start, end):
                    sumOfParts += int(schematic[i][start:end])
            j += 1
    return sumOfParts


if __name__ == '__main__':
    with open('day3/input.txt') as f:
        schematic = [val.strip() for val in f]

    print('Sum of all parts numbers: ' + str(sumAllPartNumbers(schematic)))