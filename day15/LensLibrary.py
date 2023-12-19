def calcHash(s):
    hash = 0
    for c in s:
        hash = ((hash + ord(c)) * 17) % 256
    return hash

def calcHashSum(strings):
    total = 0
    for s in strings:
        total += calcHash(s)
    return total

class keyVal:
    def __init__(self, key, val=0):
        self.key = key
        self.val = val

    def __eq__(self, other):
        return self.key == other.key


def upsert(s, hMap):
    key, val = s.split('=')
    i = calcHash(key)
    if keyVal(key) in hMap[i]:
        j = hMap[i].index(keyVal(key))
        hMap[i][j] = keyVal(key, int(val))
    else:
        hMap[i].append(keyVal(key, int(val)))

def delete(s, hMap):
    key = s[:-1]
    i = calcHash(key)
    if keyVal(key) in hMap[i]:
        j = hMap[i].index(keyVal(key))
        hMap[i].pop(j)

def init(strings):
    hMap = [[] for _ in range(256)]
    for s in strings:
        if '=' in s:
            upsert(s, hMap)
        else:
            delete(s, hMap)
    return hMap

def calcFocusingPower(hMap):
    total = 0
    for i in range(len(hMap)):
        for j in range(len(hMap[i])):
            total += (i + 1) * (j+1) * hMap[i][j].val
    return total

if __name__ == '__main__':
    with open('day15/input.txt') as f:
        strings = f.read().strip().split(',')
    print('HashSum is: ' + str(calcHashSum(strings)))

    hMap = init(strings)
    print('Focusing power is: ' + str(calcFocusingPower(hMap)))