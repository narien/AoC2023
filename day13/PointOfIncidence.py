import copy

def checkHorizontal(pattern, invalidRow):
    lastIndex = len(pattern) - 1
    foundMatch = False
    for i in range(lastIndex):
        if pattern[i] == pattern[i+1] and i != invalidRow:
            firstReflection = i
            left = firstReflection
            right = firstReflection + 1
            while pattern[left] == pattern[right]:
                left -= 1
                right += 1
                if left < 0 or right > lastIndex:
                    return True, firstReflection + 1
    return False, 0

def checkVertical(pattern, invalidRow):
    pattern = list(zip(*pattern[::-1]))
    found, preceedingRows = checkHorizontal(pattern, invalidRow)
    if found:
        return found, preceedingRows
    return False, 0

def checkPattern(pattern, p1Reflection):
    found, preceedingRows = checkHorizontal(pattern, p1Reflection[1] if p1Reflection[0] == 'h' else -1)
    if found:
        return found, preceedingRows * 100, ('h', preceedingRows - 1)
    found, preceedingColumns = checkVertical(pattern, p1Reflection[1] if p1Reflection[0] == 'v' else -1)
    return found, preceedingColumns, ('v', preceedingColumns - 1)


def countPreceedingRowsAndColumns(patterns):
    checkSum = 0
    p1ReflectionList = []
    for pattern in patterns:
        _, patternCheckSum, p1Reflection = checkPattern(pattern, ('', -1))
        checkSum += patternCheckSum
        p1ReflectionList.append(p1Reflection)
    return checkSum, p1ReflectionList

def fixSmudgeAndCalc(pattern, p1ReflectionList):
    p1Reflection = p1ReflectionList.pop(0)
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            patternCopy = copy.deepcopy(pattern)
            patternCopy[i][j] = '.' if patternCopy[i][j] == '#' else '#'
            found, checkSum, _ = checkPattern(patternCopy, p1Reflection)
            if found:
                return checkSum
    return 0


def countPreceedingRowsAndColumnsWithSmudges(patterns, p1ReflectionList):
    checkSum = 0
    for pattern in patterns:
        checkSum += fixSmudgeAndCalc(pattern, p1ReflectionList)
    return checkSum


if __name__ == '__main__':
    with open('day13/input.txt') as f:
        lines = [line.strip() for line in f]
    patterns = []
    pattern = []
    for line in lines:
        if line == '':
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append([c for c in line])
    patterns.append(pattern)

    checkSum, p1ReflectionList = countPreceedingRowsAndColumns(patterns)
    print('Checksum for part 1: ' + str(checkSum))
    print('Checksum for part 2: ' + str(countPreceedingRowsAndColumnsWithSmudges(patterns, p1ReflectionList)))