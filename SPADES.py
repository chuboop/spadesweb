# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:05:12 2020

@author: chuti
"""

import random
#import time - in order to change pace of play
suitspades =   spades =   SPA = ("AA-SPA", "KK-SPA", "QQ-SPA", "JJ-SPA", "10-SPA", "09-SPA", "08-SPA", "07-SPA", "06-SPA", "05-SPA", "04-SPA", "03-SPA", "02-SPA")
suithearts =   hearts =   HEA = ("AA-HEA", "KK-HEA", "QQ-HEA", "JJ-HEA", "10-HEA", "09-HEA", "08-HEA", "07-HEA", "06-HEA", "05-HEA", "04-HEA", "03-HEA", "02-HEA")
suitdiamonds = diamonds = DIA = ("AA-DIA", "KK-DIA", "QQ-DIA", "JJ-DIA", "10-DIA", "09-DIA", "08-DIA", "07-DIA", "06-DIA", "05-DIA", "04-DIA", "03-DIA", "02-DIA")
suitclubs =    clubs =    CLB = ("AA-CLB", "KK-CLB", "QQ-CLB", "JJ-CLB", "10-CLB", "09-CLB", "08-CLB", "07-CLB", "06-CLB", "05-CLB", "04-CLB", "03-CLB", "02-CLB")

masterdeck = ("AA-SPA", "KK-SPA", "QQ-SPA", "JJ-SPA", "10-SPA", "09-SPA", "08-SPA", "07-SPA", "06-SPA", "05-SPA", "04-SPA", "03-SPA", "02-SPA", \
        "AA-HEA", "KK-HEA", "QQ-HEA", "JJ-HEA", "10-HEA", "09-HEA", "08-HEA", "07-HEA", "06-HEA", "05-HEA", "04-HEA", "03-HEA", "02-HEA", \
        "AA-DIA", "KK-DIA", "QQ-DIA", "JJ-DIA", "10-DIA", "09-DIA", "08-DIA", "07-DIA", "06-DIA", "05-DIA", "04-DIA", "03-DIA", "02-DIA", \
        "AA-CLB", "KK-CLB", "QQ-CLB", "JJ-CLB", "10-CLB", "09-CLB", "08-CLB", "07-CLB", "06-CLB", "05-CLB", "04-CLB", "03-CLB", "02-CLB")
origindeck = ["AA-SPA", "KK-SPA", "QQ-SPA", "JJ-SPA", "10-SPA", "09-SPA", "08-SPA", "07-SPA", "06-SPA", "05-SPA", "04-SPA", "03-SPA", "02-SPA", \
        "AA-HEA", "KK-HEA", "QQ-HEA", "JJ-HEA", "10-HEA", "09-HEA", "08-HEA", "07-HEA", "06-HEA", "05-HEA", "04-HEA", "03-HEA", "02-HEA", \
        "AA-DIA", "KK-DIA", "QQ-DIA", "JJ-DIA", "10-DIA", "09-DIA", "08-DIA", "07-DIA", "06-DIA", "05-DIA", "04-DIA", "03-DIA", "02-DIA", \
        "AA-CLB", "KK-CLB", "QQ-CLB", "JJ-CLB", "10-CLB", "09-CLB", "08-CLB", "07-CLB", "06-CLB", "05-CLB", "04-CLB", "03-CLB", "02-CLB"]

"""    
00 01 02 03 04 05 06 07 08 09 10 11 12
13 14 15 16 17 18 19 20 21 22 23 24 25
26 27 28 29 30 31 32 33 34 35 36 37 38
39 40 41 42 43 44 45 46 47 48 49 50 51
"""

def resetdeck():
    global origindeck
    origindeck = list(masterdeck)

def suit(card):
    if card in suitspades:
        return(suitspades)
    if card in suithearts:
        return(suithearts)
    if card in suitdiamonds:
        return(suitdiamonds)
    if card in suitclubs:
        return(suitclubs)

def numcards(PLAYER, suit=0):
    if suit == 0:
        return len(PLAYER[0])
    else:
        k = 0
        for card in PLAYER[0]:
            if card in suit:
                k += 1
        return k

def printcurrentcards(PLAYER):
    for x in range(0,numcards(PLAYER)):
        basesuit = suit(PLAYER[0][x])
        if (PLAYER[0][x] in basesuit) and (PLAYER[0][x-1] not in basesuit):
            print("")
        print(PLAYER[0][x])

def listinsert(listname, position, element):
    #Inserts the given string "element" into the list at the given position, where position is an index value.
    #It will displace the current element at position to the right.
    #Returns resultlist, which is a new list with the given insertion.
    templistupper = listname[position:]
    templistlower = listname[:position]
    resultlist = templistlower + [element] + templistupper
    return resultlist

def shuffleanddeal():
    cardcount = 51
    global deck1
    deck1 = []
    global deck2
    deck2 = []
    global deck3
    deck3 = []
    global deck4
    deck4 = []
    while cardcount <= 51 and cardcount >= 39:
        listcardsN = random.sample(range(0,cardcount),13)
        listcardsN.sort()
        i = 0
        while i <= 12: #Adding the cards of index listcardsN from origindeck to deck1
            deck1 += [origindeck[listcardsN[i]]]
            cardcount -= 1
            i += 1
        k = 12
        while k >= 0: #Removing the cards from the set
            del origindeck[listcardsN[k]]
            k -= 1
    print(deck1)
    print("")
    while cardcount <= 38 and cardcount >= 26:
        listcardsN = random.sample(range(0,cardcount),13)
        listcardsN.sort()
        i = 0
        while i <= 12:
            deck2 += [origindeck[listcardsN[i]]]
            cardcount -= 1
            i += 1
        k = 12
        while k >= 0:
            del origindeck[listcardsN[k]]
            k -= 1
    print(deck2)
    print("")
    while cardcount <= 25 and cardcount >= 13:
        listcardsN = random.sample(range(0,cardcount),13)
        listcardsN.sort()
        i = 0
        while i <= 12:
            deck3 += [origindeck[listcardsN[i]]]
            cardcount -= 1
            i += 1
        k = 12
        while k >= 0:
            del origindeck[listcardsN[k]]
            k -= 1
    print(deck3)
    print("")
    while cardcount <= 12 and cardcount >= 0: #I know this is completely unnecessary and that deck4 = origindeck would suffice; just for consistency
        listcardsN = random.sample(range(0,cardcount+1),13)
        listcardsN.sort()
        i = 0
        while i <= 12:
            deck4 += [origindeck[listcardsN[i]]]
            cardcount -=1
            i += 1
        k = 12
        while k >= 0:
            del origindeck[listcardsN[k]]
            k -=1
    print(deck4)
    print("")
    global playedcards1
    playedcards1 = []
    global playedcards2
    playedcards2 = []
    global playedcards3
    playedcards3 = []
    global playedcards4
    playedcards4 = []
    global remainingcards1
    remainingcards1 = list(masterdeck)
    for card in deck1:
        del remainingcards1[remainingcards1.index(card)]
    global remainingcards2
    remainingcards2 = list(masterdeck)
    for card in deck2:
        del remainingcards2[remainingcards2.index(card)]
    global remainingcards3
    remainingcards3 = list(masterdeck)
    for card in deck3:
        del remainingcards3[remainingcards3.index(card)]
    global remainingcards4
    remainingcards4 = list(masterdeck)
    for card in deck4:
        del remainingcards4[remainingcards4.index(card)]
    # USER = [0 deck, 1 playedcards, 2 remainingcards, 3 NIL, 4 PARTNER NIL, 5 TRICKS, 6 BID, 7 PARTNER TRICKS, 8 PARTNER BID,
    #         9 TEAM TRICKS, 10 TEAM BID, 11 BAG PENALTY, 12 TEAM SCORE, 13 ENEMY SCORE, 14 AI=0 PLAYER=1]
    #PLAYER = [deck#, playedcards#, remainingcards#, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14]
    global PLAYER1
    PLAYER1 = [deck1, playedcards1, remainingcards1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    global PLAYER2
    PLAYER2 = [deck2, playedcards2, remainingcards2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    global PLAYER3
    PLAYER3 = [deck3, playedcards3, remainingcards3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    global PLAYER4
    PLAYER4 = [deck4, playedcards4, remainingcards4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    resetdeck()
    
def evalcards(cardA, cardB, cardC, cardD):
    """
    Evaluates a maximum of four cards. The suit is determined by card1.
    Each card is a string.
    Outputs a list of cards in descending order.
    """
    array = []
    ranks = []
    spadessort = []
    cardsinsuit = 1
    # BASESUIT definitions
    if cardA[-3:] == "SPA":
        basesuit = suitspades
    if cardA[-3:] == "HEA":
        basesuit = suithearts
    if cardA[-3:] == "DIA":
        basesuit = suitdiamonds
    if cardA[-3:] == "CLB":
        basesuit = suitclubs
    if cardB in basesuit:
        cardsinsuit += 1
    if cardC in basesuit:
        cardsinsuit += 1
    if cardD in basesuit:
        cardsinsuit += 1
    #BEGIN SORTING CARDS
    cardBBB = cardB
    cardCCC = cardC
    cardDDD = cardD
    if cardB not in basesuit:
        cardBBB = basesuit[12]
    if cardC not in basesuit:
        cardCCC = basesuit[12]
    if cardD not in basesuit:
        cardDDD = basesuit[12]
    array += [str(basesuit.index(cardA))]
    if len(str(basesuit.index(cardA))) == 1:
        del array[0]
        array += ["0"+str(basesuit.index(cardA))]
    array += [str(basesuit.index(cardBBB))]
    if len(str(basesuit.index(cardBBB))) == 1:
        del array[1]
        array += ["0"+str(basesuit.index(cardBBB))]
    array += [str(basesuit.index(cardCCC))]
    if len(str(basesuit.index(cardCCC))) == 1:
        del array[2]
        array += ["0"+str(basesuit.index(cardCCC))]
    array += [str(basesuit.index(cardDDD))]
    if len(str(basesuit.index(cardDDD))) == 1:
        del array[3]
        array += ["0"+str(basesuit.index(cardDDD))]
    array.sort()
    for x in range(0,cardsinsuit):
        ranks += [basesuit[int(array[x])]]
    #CHECKING FOR NOT IN SUIT AND FOR SPADES
    if cardB not in basesuit:
        if cardB in spades:
            spadessort += [cardB]
        else:
            ranks += [cardB]
    if cardC not in basesuit:
        if cardC in spades:
            if (cardB in spades) and (spades.index(cardC) < spades.index(cardB)):
                spadessort = listinsert(spadessort, 0, cardC)
            elif (cardB in spades) and (spades.index(cardC) > spades.index(cardB)):
                spadessort += [cardC]
            else:
                spadessort += [cardC]
        else:
            ranks += [cardC]
    if cardD not in basesuit:
        if cardD in spades:
            if (cardB in spades) and (cardC in spades):
                if (spades.index(cardD) < spades.index(cardC)) and (spades.index(cardD) < spades.index(cardB)):
                    spadessort = listinsert(spadessort, 0, cardD)
                elif ((spades.index(cardD) < spades.index(cardC)) and (spades.index(cardD) > spades.index(cardB))) or ((spades.index(cardD) > spades.index(cardC)) and (spades.index(cardD) < spades.index(cardB))):
                    spadessort = listinsert(spadessort, 1, cardD)
                elif (spades.index(cardD) > spades.index(cardC)) and (spades.index(cardD) > spades.index(cardB)):
                    spadessort += [cardD]
            elif (cardB in spades) and (cardC not in spades):
                if spades.index(cardD) < spades.index(cardB):
                    spadessort = listinsert(spadessort, 0, cardD)
                if spades.index(cardD) > spades.index(cardB):
                    spadessort += [cardD]
            elif (cardB not in spades) and (cardC in spades):
                if spades.index(cardD) < spades.index(cardC):
                    spadessort = listinsert(spadessort, 0, cardD)
                if spades.index(cardD) > spades.index(cardC):
                    spadessort += [cardD]
            else:
                spadessort += [cardD]
        else:
            ranks += [cardD]
    ranks = spadessort + ranks
    return(ranks)

def playcard(PLAYER, card):
    if PLAYER == PLAYER1:
        print("PLAYER1 plays "+card+"!")
        PLAYER2[2].remove(card)
        PLAYER3[2].remove(card)
        PLAYER4[2].remove(card)
    if PLAYER == PLAYER2:
        print("PLAYER2 plays "+card+"!")
        PLAYER1[2].remove(card)
        PLAYER3[2].remove(card)
        PLAYER4[2].remove(card)
    if PLAYER == PLAYER3:
        print("PLAYER3 plays "+card+"!")
        PLAYER1[2].remove(card)
        PLAYER2[2].remove(card)
        PLAYER4[2].remove(card)
    if PLAYER == PLAYER4:
        print("PLAYER4 plays "+card+"!")
        PLAYER1[2].remove(card)
        PLAYER2[2].remove(card)
        PLAYER3[2].remove(card)
    PLAYER[1] = listinsert(PLAYER[1], 0, card)
    del PLAYER[0][PLAYER[0].index(card)]
    return(card)

#BIDDING PHASE
#BIDDING PHASE
#BIDDING PHASE

def guaranteedspades(PLAYER):
    spadesset = []
    amtcover = -1
    guaranteed = 0
    for k in range(numcards(PLAYER, spades)):
        spadesset += [PLAYER[0][k]]
    for i in range(len(spadesset)):
        amtcover += (spades.index(spadesset[i]) - i)
        if spades.index(spadesset[i]) - spades.index(spadesset[i-1]) == 1:
            amtcover -= 1
        if amtcover < 0:
            guaranteed += 1
        print("amtcover: "+str(amtcover))
        print("guaranteed: "+str(guaranteed))
    return guaranteed

def bidset(PLAYER):
    print(str(PLAYER))
def bidhigh(PLAYER):
    print(str(PLAYER))
def bidnormal(PLAYER):
    bid = 0
    print(str(PLAYER))
def bidlow(PLAYER):
    print(str(PLAYER))
def bidbag(PLAYER):
    print(str(PLAYER))
def bidnil(PLAYER):
    PLAYER[3] = 1
    return 0
def bidblindnil(PLAYER):
    PLAYER[3] = 2
    return 0

"""
define amountofhandsguaranteed:
    somehow if spades count
    FIND AMOUNT OF COVER CARDS ABOVE; SUBTRACT FOR EVERY CARD
    compare COVER_NEEDED to COVERSPADES
    KQ needs 2, but only has one (A)
    Q J 9 8: A and K cover Q and J, but 10 cannot cover both 9 and 8
    do for loop until numspades; will automatically start at biggest and begin
    canceling
"""


#END BIDDING PHASE
#END BIDDING PHASE
#END BIDDING PHASE

#In the list, don't use strings for everything. Just use numbers and booleans.
# EVERY AI PERFECTLY CARD COUNTS
    
    