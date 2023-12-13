def evaluateRow(row, backup):
    hashCount = 0
    for c in row:
        if c == '#':
            hashCount += 1
        else:
            if hashCount > 0:
                expected = backup.pop(0)
                if hashCount != expected:
                    return False
                hashCount = 0
    return len(backup) == 0 or backup.pop(0) == hashCount and len(backup) == 0


def countArrangements(row, backup):
    if '?' in row:





def countTotalPossibleArrangements(conditions):
    totalArrangements = 0
    for condition in conditions:
        row, backup = condition.split()
        row = [c for c in row]
        backup = [int(val) for val in backup.split(',')]
        totalArrangements += countArrangements(row, backup)
    return totalArrangements

if __name__ == '__main__':
    with open('day12/input.txt') as f:
        conditions = [line.strip() for line in f]

    print('Total possible arrangements: ' + str(countTotalPossibleArrangements(conditions)))