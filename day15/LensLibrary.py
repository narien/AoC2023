
def calcHashSum(strings):
    total = 0
    for s in strings:
        hash = 0
        for c in s:
            hash = ((hash + ord(c)) * 17) % 256
        total += hash
    return total

if __name__ == '__main__':
    with open('day15/input.txt') as f:
        strings = f.read().strip().split(',')
    print('HashSum is: ' + str(calcHashSum(strings)))
