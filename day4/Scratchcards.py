
def sumAllPoints(cards):
    total = 0
    for card in cards:
        cTotal = 0
        winners, actual = card.split('|')
        winners = set(winners.split()[2:])
        actual = actual.split()
        for num in actual:
            if num in winners:
                cTotal = cTotal * 2 if cTotal > 0 else 1
        total += cTotal
    return total


if __name__ == '__main__':
    with open('day4/input.txt') as f:
        cards = [val.strip() for val in f]

    print('Total points: ' + str(sumAllPoints(cards)))