import random

cards = list(range(52))

def checkHand(hand):

    suits = [c // 13 for c in hand]
    values = sorted([c % 13 for c in hand])

    is_wheel = values == [0, 1, 2, 3, 12]
    is_straight = all(values[i] + 1 == values[i+1] for i in range(4)) or is_wheel

    is_flush = len(set(suits)) == 1

    counts = [values.count(v) for v in set(values)]
    counts.sort(reverse=True)

    if is_straight and is_flush:
        return "Straight Flush"

    if counts == [4,1]:
        return "Four of a Kind"

    if counts == [3,2]:
        return "Full House"

    if is_flush:
        return "Flush"

    if is_straight:
        return "Straight"

    if counts == [3,1,1]:
        return "Three of a Kind"

    if counts == [2,2,1]:
        return "Two Pair"

    if counts == [2,1,1,1]:
        return "Pair"

    return "High Card"



x = 0
listCounts = [0,0,0,0,0,0,0,0,0]

while x < 1000000:
    hand = random.sample(cards,5)
    if checkHand(hand) == "Straight Flush":
        listCounts[0]+=1
    elif checkHand(hand) == "Four of a Kind":
        listCounts[1]+=1
    elif checkHand(hand) == "Full House":
        listCounts[2]+=1
    elif checkHand(hand) == "Flush":
        listCounts[3]+=1
    elif checkHand(hand) == "Straight":
        listCounts[4]+=1
    elif checkHand(hand) == "Three of a Kind":
        listCounts[5]+=1
    elif checkHand(hand) == "Two Pair":
        listCounts[6]+=1
    elif checkHand(hand) == "Pair":
        listCounts[7]+=1
    elif checkHand(hand) == "High Card":
        listCounts[8]+=1
    x = x+1

print("Straight Flush: " + str(listCounts[0]/1000000*100) + "%")
print("Four of a Kind: " + str(listCounts[1]/1000000*100) + "%")
print("Full House: " + str(listCounts[2]/1000000*100) + "%")
print("Flush: " + str(listCounts[3]/1000000*100) + "%")
print("Straight: " + str(listCounts[4]/1000000*100) + "%")
print("Three of a Kind: " + str(listCounts[5]/1000000*100) + "%")
print("Two Pair: " + str(listCounts[6]/1000000*100) + "%")
print("Pair: " + str(listCounts[7]/1000000*100) + "%")
print("High Card: " + str(listCounts[8]/1000000*100) + "%")
