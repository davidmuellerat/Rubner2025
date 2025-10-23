import random

cards = list(range(52))

def checkHand(hand):

    hand.sort()
    colorcards = []
    symbolcards = []
    for x in range(5):
        colorcards.append(hand[x] // 13)
        symbolcards.append(hand[x] % 13)
    handType = ""
    if len(set(colorcards)) == 1 and (symbolcards[0]+1 == symbolcards[1] and symbolcards[1]+1 == symbolcards[2] and symbolcards[2]+1 == symbolcards[3] and symbolcards[3]+1 == symbolcards[4]):
        handType = "Straight Flush"
    elif len(set(symbolcards)) == 2 and (symbolcards.count(symbolcards[0]) == 4 or symbolcards.count(symbolcards[1] == 4)):
        handType = "Four of a Kind"
    elif len(set(symbolcards)) == 2:
        handType = "Full House"
    elif len(set(colorcards)) == 1:
        handType = "Flush"
    elif symbolcards[0]+1 == symbolcards[1] and symbolcards[1]+1 == symbolcards[2] and symbolcards[2]+1 == symbolcards[3] and symbolcards[3]+1 == symbolcards[4]:
        handType = "Straight"
    elif len(set(symbolcards)) == 3 and (symbolcards.count(symbolcards[0]) == 3 or symbolcards.count(symbolcards[1]) == 3 or symbolcards.count(symbolcards[2]) == 3):
        handType = "Three of a Kind"
    elif len(set(symbolcards)) == 3 and (symbolcards.count(symbolcards[0]) == 2 or symbolcards.count(symbolcards[1]) == 2 or symbolcards.count(symbolcards[2]) == 2):
        handType = "Two Pair"
    elif len(set(symbolcards)) == 4:
        handType = "Pair"
    else:
        handType = "High Card"
    return handType


x = 0
listCounts = [0,0,0,0,0,0,0,0,0]

while x < 1000000:
    hand = [random.sample(cards,5)]
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
