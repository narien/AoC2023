
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

def sumAllCards(cards):
    cards.reverse()

    cardRes = {}

    for card in cards:
        totalCardsFromCard = 1
        winners, actual = card.split('|')
        winners = winners.split()
        cardNbr = int(winners[1][0:-1])
        winners = set(winners[2:])
        actual = actual.split()
        wins = 0
        for num in actual:
            if num in winners:
                wins += 1
        
        for i in range(wins):
            totalCardsFromCard += cardRes.get(cardNbr + i + 1, 0)
        cardRes[cardNbr] = totalCardsFromCard
    return sum(cardRes.values())




if __name__ == '__main__':
    with open('day4/input.txt') as f:
        cards = [val.strip() for val in f]

    print('Total points: ' + str(sumAllPoints(cards)))
    print('Total nbr of cards: ' + str(sumAllCards(cards)))