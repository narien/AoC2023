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


if __name__ == '__main__':
    with open('day7/input.txt') as f:
        lines = [line.strip() for line in f]

    lines = sorted(lines, key=functools.cmp_to_key(compare))
    totalWinnings = 0
    for i in range(len(lines)):
        totalWinnings += int(lines[i].split()[1]) * (i+1)
    print(lines)
    print('Total winnings: ' + str(totalWinnings))