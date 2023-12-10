import functools

def extrapolateNextValue(firstSequence):
    sequences = [firstSequence]
    nextToSequence = 0
    
    while True:
        sequence = sequences[nextToSequence]
        nextSequence = []
        for i in range(len(sequence) - 1):
            nextSequence.append(sequence[i+1] - sequence[i])
        sequences.append(nextSequence)
        if all(value == 0 for value in sequence): break
        nextToSequence += 1
    sequences.reverse()
    nextValue = 0
    previousValue = 0
    for sequence in sequences:
        nextValue += sequence[-1]
        previousValue = sequence[0] - previousValue
    return nextValue, previousValue


def calcChecksum(lines):
    checksumP1 = 0
    checksumP2 = 0
    for line in lines:
        line = [int(i) for i in line.split()]
        p1, p2 = extrapolateNextValue(line)
        checksumP1 += p1
        checksumP2 += p2
    return checksumP1, checksumP2

if __name__ == '__main__':
    with open('day9/input.txt') as f:
        lines = [line.strip() for line in f]
    print('Extrapolation checksum is: ' + str(calcChecksum(lines)))