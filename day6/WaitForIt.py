from functools import reduce

def calcNbrOfWaysToWin(durations, records):
    winningWays = []
    for i in range(len(durations)):
        duration = durations[i]
        record = records[i]
        nbrOfWaysToWin = 0
        for chargeTime in range(duration):
            raceTime = duration - chargeTime

            distance = raceTime*chargeTime
            if distance > record:
                nbrOfWaysToWin += 1
        winningWays.append(nbrOfWaysToWin)
    print('Wins checksum: ' + str(reduce((lambda x, y: x * y), winningWays)))


if __name__ == '__main__':
    with open('day6/input.txt') as f:
        lines = [line.strip() for line in f]

    durationsP1 = [int(duration) for duration in lines[0].split()[1:]]
    recordsP1 = [int(record) for record in lines[1].split()[1:]]
    calcNbrOfWaysToWin(durationsP1, recordsP1)

    durationsP2 = [int(''.join(lines[0].split()[1:]))]
    recordsP2 = [int(''.join(lines[1].split()[1:]))]
    calcNbrOfWaysToWin(durationsP2, recordsP2)