from collections import Counter
import functools

def compare(item1, item2):
    s1 = item1.split()[0]
    s2 = item2.split()[0]

    c1 = Counter(s1)
    c2 = Counter(s2)

    hC1 = max(c1.values())
    hC2 = max(c2.values())

    if hC1 > hC2: return 1
    if hC1 < hC2: return -1

    if hC1 == 3:
        if len(c1) == 2 and not len(c2) == 2: return 1
        if len(c2) == 2 and not len(c1) == 2: return -1

    if hC1 == 2:
        if len(c1) == 3 and not len(c2) == 3: return 1
        if len(c2) == 3 and not len(c1) == 3: return -1

    for i in range(len(s1)):
        if s1[i] == s2[i]: continue
        if s1[i] == 'A': return 1
        if s2[i] == 'A': return -1
        if s1[i] == 'K': return 1
        if s2[i] == 'K': return -1
        if s1[i] == 'Q': return 1
        if s2[i] == 'Q': return -1
        if s1[i] == 'J': return 1
        if s2[i] == 'J': return -1
        if s1[i] == 'T': return 1
        if s2[i] == 'T': return -1
        n1 = int(s1[i])
        n2 = int(s2[i])
        return 1 if n1 > n2 else -1
    return 0

def maxValueKey(d):
     v = list(d.values())
     k = list(d.keys())
     return k[v.index(max(v))]

def compareP2(item1, item2):
    s1 = item1.split()[0]
    s2 = item2.split()[0]

    c1 = Counter(s1)
    c2 = Counter(s2)

    if 'J' in c1.keys() and len(c1.keys()) > 1:
        j1 = c1.pop('J')
        c1[maxValueKey(c1)] += j1
    if 'J' in c2.keys() and len(c2.keys()) > 1:
        j2 = c2.pop('J')
        c2[maxValueKey(c2)] += j2


    hC1 = max(c1.values())
    hC2 = max(c2.values())

    if hC1 > hC2: return 1
    if hC1 < hC2: return -1

    if hC1 == 3:
        if len(c1) == 2 and not len(c2) == 2: return 1
        if len(c2) == 2 and not len(c1) == 2: return -1

    if hC1 == 2:
        if len(c1) == 3 and not len(c2) == 3: return 1
        if len(c2) == 3 and not len(c1) == 3: return -1

    for i in range(len(s1)):
        if s1[i] == s2[i]: continue
        if s1[i] == 'A': return 1
        if s2[i] == 'A': return -1
        if s1[i] == 'K': return 1
        if s2[i] == 'K': return -1
        if s1[i] == 'Q': return 1
        if s2[i] == 'Q': return -1
        if s1[i] == 'J': return -1  # swap J around since it is now the least valuable one
        if s2[i] == 'J': return 1   # swap J around since it is now the least valuable one
        if s1[i] == 'T': return 1
        if s2[i] == 'T': return -1
        n1 = int(s1[i])
        n2 = int(s2[i])
        return 1 if n1 > n2 else -1
    return 0

if __name__ == '__main__':
    with open('day7/input.txt') as f:
        lines = [line.strip() for line in f]

    sortedP1 = sorted(lines, key=functools.cmp_to_key(compare))
    totalWinningsP1 = 0
    for i in range(len(lines)):
        totalWinningsP1 += int(sortedP1[i].split()[1]) * (i+1)
    print('Total winnings part one: ' + str(totalWinningsP1))
    print(sortedP1)

    sortedP2 = sorted(lines, key=functools.cmp_to_key(compareP2))
    totalWinningsP2 = 0
    for i in range(len(lines)):
        totalWinningsP2 += int(sortedP2[i].split()[1]) * (i+1)
    print('Total winnings part two: ' + str(totalWinningsP2))