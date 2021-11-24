import math, copy, random, time

# fix all-in calculating winner and biggest hand thing
from cmu_112_graphics import *
# Citations
# https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#exampleSnake on line 51
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids on line 609
def appStarted(app):
    app.rows = 16
    app.cols = 25
    app.waitingForFirstKeyPress = True
    app.names = ['Marielle', 'Zhuo', 'Ahmed', 'Priyanshi', 'Harini',
    'Sally', 'Anna', 'Helen', 'Jiajun', 'Dani', 'Maggie', 'Luolan', 'Xiaotong',
    'Alice', 'Andy', 'Cassidy', 'Bowie']
    app.hatColors = ['blue', 'red', 'yellow', 'pink', 'purple', 'brown', 'orange',
    'blue violet', 'dark violet', 'navy', 'gold']
    app.money = [2000, 2000, 2000, 2000]
    app.cards = [ [2, 'h'], [2, 'd'], [2, 's'], [2, 'c'], [3, 'h'], [3, 'd'], [3, 's'], [3, 'c'],
    [4, 'h'], [4, 'd'], [4, 's'], [4, 'c'], [5, 'h'], [5, 'd'], [5, 's'], [5, 'c'], [6, 'h'], [6, 'd'], [6, 's'], [6, 'c'],
    [7, 'h'], [7, 'd'], [7, 's'], [7, 'c'], [8, 'h'], [8, 'd'], [8, 's'], [8, 'c'], [8, 'h'], [9, 'd'], [9, 's'], [9, 'c'],
    [10, 'h'], [10, 'd'], [10, 's'], [10, 'c'], [11, 'h'], [11, 'd'], [11, 's'], [11, 'c'], [12, 'h'], 
    [12, 'd'], [12, 's'], [12, 'c'], [13, 'h'], [13, 'd'], [13, 's'], [13, 'c'], [14, 'h'], [14, 'd'], 
    [14, 's'], [14, 'c'] ]
    app.moves = ['', 'Check', 'Raise', 'Call', 'All in!', 'Fold']
    # name, hat color, money, moves, card1, card2
    app.playerFacts = [ ['you', app.hatColors[random.randint(0,len(app.hatColors) - 1)],
    app.money[0], app.moves[0] ], [app.names.pop(random.randint(0,len(app.names) - 1)), 
    app.hatColors[random.randint(0,len(app.hatColors) - 1)], app.money[1], app.moves[0] ], 
    [app.names.pop(random.randint(0,len(app.names) - 1)), 
    app.hatColors[random.randint(0,len(app.hatColors) - 1)], app.money[2], app.moves[0] ], 
    [app.names.pop(random.randint(0,len(app.names) - 1)), 
    app.hatColors[random.randint(0,len(app.hatColors) - 1)], app.money[3], app.moves[0] ] ]
    app.bodyColor = [random.choice(app.hatColors), random.choice(app.hatColors),
    random.choice(app.hatColors)]
    # locations of text boxes
    app.locations = [ [650, 690], [250, 500], [680, 280], [1090, 500] ]
    playAgain(app)
    app.foldAndCheckCount = 0
    app.errorMessage = False
    app.cantChooseThisMove = False
    app.numberOfButtonPresses = 0

def playAgain(app):
    app.tempCards = copy.deepcopy(app.cards)
    for i in range(4):
        app.playerFacts[i][3] = app.moves[0]
    app.moneyPerRound = [0, 0, 0, 0]
    app.yourTurn = False
    app.totalMoneyOnTable = 0
    app.playersMoneyOnTable = [0, 0, 0, 0]
    app.playerRaised = False
    app.allInAmount = 0
    app.playersCards = False
    app.noRaise = True
    app.calledAllIn = [False, False, False, False]
    app.threeCards = False
    app.fourCards = False
    app.fiveCards = False
    app.cardsOnTable = []
    app.highestHand = []
    app.handOfWinner = None
    app.winner = []
    app.moneyAtBeginning = []
    for i in range(4):
        app.moneyAtBeginning.append(copy.deepcopy(app.playerFacts[i][2]))
    app.totalNumberOfClicks = 0
    app.keyPresses = 0
    app.textOnCards = []
    addCards(app)
    app.errorMessage = False
    app.showCards = False
    
def keyPressed(app, event):
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#exampleSnake
    if (app.waitingForFirstKeyPress):
        app.waitingForFirstKeyPress = False
    elif (event.key == 'Left'):
    #pre-card round
        try:
            if app.totalNumberOfClicks != 0 or app.keyPresses != 0:
                print(x)
            else:
                app.keyPresses += 1
                preCardRound(app)
                app.yourTurn = True
        except:
            app.errorMessage = True
    elif (event.key == 'Up'):
    # three card round
        app.keyPresses += 1
        app.moneyPerRound = [0, 0, 0, 0]
        app.playerRaised = False
        for i in range(4):
            app.playerFacts[i][3] == app.moves[0]
        threeCardRound(app)
        app.yourTurn = True
    elif (event.key == 'Right'):
    # four card round
        app.keyPresses += 1
        app.moneyPerRound = [0, 0, 0, 0]
        app.playerRaised = False
        for i in range(4):
            app.playerFacts[i][3] == app.moves[0]
        fourCardRound(app)
        app.yourTurn = True
    elif (event.key == 'Down'):
    # five card round
        app.keyPresses += 1
        app.moneyPerRound = [0, 0, 0, 0]
        app.playerRaised = False
        for i in range(4):
            app.playerFacts[i][3] == app.moves[0]
        fiveCardRound(app)
        app.yourTurn = True
    elif (event.key == 's'):
        app.keyPresses += 1
        findWinner(app)
        addMoney(app)
        for i in range(1, 4):
            if app.playerFacts[i][2] == 0 and app.winner != []:
                app.playerFacts[i][0] == 'out'
        print(app.winner)
    elif (event.key == 'n'):
    # doesn't work? Dunno why
        try:
            if ((app.totalNumberOfClicks != 4 and app.winner == []) 
            or (app.keyPresses != 5 and app.winner == [])):
                print(x)
            else:
                app.keyPresses += 1
                app.time = time.time()
                while time.time() < app.time + 2:
                    pass
                for i in range(4):
                    app.playerFacts[i].pop(5)
                    app.playerFacts[i].pop(4)
                playAgain(app)
        except:
            app.errorMessage = True
        
def mousePressed(app, event):
    if ((app.width/2 - 590 <= event.x <= app.width/2 - 440) and
    (app.height/2 + 300 <= event.y <= app.height/2 + 370)):
    # if check box clicked
        canCheck = True
        try:
            for i in range(1, 4):
                if (app.playerFacts[i][3] == (app.moves[2] or app.moves[3]
                or app.moves[4])):
                    canCheck = False
            if app.playerFacts[0][3] == (app.moves[4] or app.moves[5]):
                    canCheck = False
            if canCheck == False:
                print(x)
            else:
                app.cantChooseThisMove = False
                app.foldAndCheckCount += 1
                app.playerFacts[0][3] = app.moves[1]
                app.yourTurn = False
                app.totalNumberOfClicks += 1
                everyPlayerButOneFolded(app)
        except:
            app.cantChooseThisMove = True
    if ((app.width/2 - 410 <= event.x <= app.width/2 - 260) and
    (app.height/2 + 300 <= event.y <= app.height/2 + 370)):
    # if raise box clicked
        try:
            if (app.playerFacts[0][3] == (app.moves[5] or app.moves[4]) or app.threeCards == False
            or app.playerFacts[0][2] == 0):
            # can't raise on pre-card round
                print(x)
            else:
                app.cantChooseThisMove = False
                app.foldAndCheckCount = 0
                app.playerFacts[0][3] = app.moves[2]
                if app.noRaise == True:
                    if app.playerFacts[0][2] >= 100:
                        app.playerFacts[0][2] -= 100
                        app.totalMoneyOnTable += 100
                        app.moneyPerRound[0] += 100
                        app.playersMoneyOnTable[0] += 100
                    else:
                        app.totalMoneyOnTable += app.playerFacts[0][2]
                        app.moneyPerRound[0] += app.playerFacts[0][2]
                        app.playersMoneyOnTable[0] += app.playerFacts[0][2]
                        app.playerFacts[0][2] = 0
                else:
                    if app.playerFacts[0][2] >= 200:
                        app.playerFacts[0][2] -= 200
                        app.totalMoneyOnTable += 200
                        app.moneyPerRound[0] += 200
                        app.playersMoneyOnTable[0] += 200
                    else:
                        app.totalMoneyOnTable += app.playerFacts[0][2]
                        app.moneyPerRound[0] += app.playerFacts[0][2]
                        app.playersMoneyOnTable[0] += app.playerFacts[0][2]
                        app.playerFacts[0][2] = 0
                app.playerRaised = True
                app.yourTurn = False
                app.time = time.time()
                while time.time() < app.time + .5:
                    pass
                if len(app.cardsOnTable) < 3:
                    playerRaised(app)
                else: 
                    playerRaisedAndCardsOnTable(app)
                app.totalNumberOfClicks += 1
                everyPlayerButOneFolded(app)
        except:
            app.cantChooseThisMove = True
    if ((app.width/2 + 160 <= event.x <= app.width/2 + 310) and
    (app.height/2 + 300 <= event.y <= app.height/2 + 370)):
    # if call box clicked
        canCall = False
        for i in range(1, 4):
            if (app.playerFacts[i][3] == (app.moves[2] or app.moves[3]
            or app.moves[4])):
                canCall = True
            elif app.totalNumberOfClicks == 0:
                canCall = True
        try:
            if (app.playerFacts[0][3] == (app.moves[5] or app.moves[4]) or canCall == False
            or app.playerFacts[0][2] == 0):
                print(x)
            else:
                app.cantChooseThisMove = False
                app.foldAndCheckCount = 0
                app.playerFacts[0][3] = app.moves[3]
                if app.totalNumberOfClicks == 0:
                    if app.playerFacts[0][2] >= 20:
                        app.playerFacts[0][2] -= 20
                        app.totalMoneyOnTable += 20
                        app.moneyPerRound[0] += 20
                        app.playersMoneyOnTable[0] += 20
                    else:
                        app.totalMoneyOnTable += app.playerFacts[0][2]
                        app.moneyPerRound[0] += app.playerFacts[0][2]
                        app.playersMoneyOnTable[0] += app.playerFacts[0][2]
                        app.playerFacts[0][2] = 0
                else:
                    if app.playerFacts[0][2] >= 100:
                        app.playerFacts[0][2] -= 100
                        app.totalMoneyOnTable += 100
                        app.moneyPerRound[0] += 100
                        app.playersMoneyOnTable[0] += 100
                    else:
                        app.totalMoneyOnTable += app.playerFacts[0][2]
                        app.moneyPerRound[0] += app.playerFacts[0][2]
                        app.playersMoneyOnTable[0] += app.playerFacts[0][2]
                        app.playerFacts[0][2] = 0
                app.yourTurn = False
                app.totalNumberOfClicks += 1
                everyPlayerButOneFolded(app)
        except:
            app.cantChooseThisMove = True
    if ((app.width/2 + 330 <= event.x <= app.width/2 + 480) and
    (app.height/2 + 300 <= event.y <= app.height/2 + 370)):
    # if all-in box clicked
        try:
            if (app.playerFacts[0][3] == app.moves[5] or app.threeCards == False
            or app.playerFacts[0][2] == 0):
            # can't all-in on pre-card round
                print(x)
            else:
                app.cantChooseThisMove = False
                app.foldAndCheckCount = 0
                app.playerFacts[0][3] = app.moves[4]
                app.totalMoneyOnTable += app.playerFacts[0][2]
                app.moneyPerRound[0] += app.playerFacts[0][2]
                app.allInAmount = app.playerFacts[0][2]
                app.playersMoneyOnTable[0] += app.playerFacts[0][2]
                app.playerFacts[0][2] = 0
                app.yourTurn = False
                app.time = time.time()
                while time.time() < app.time + .5:
                    pass
                if len(app.cardsOnTable) < 3:
                    playerAllIn(app)
                else: 
                    playerAllInAndCardsOnTable(app)
                app.totalNumberOfClicks += 1
                everyPlayerButOneFolded(app)
        except:
            app.cantChooseThisMove = True
    if ((app.width/2 + 500 <= event.x <= app.width/2 + 650) and
    (app.height/2 + 300 <= event.y <= app.height/2 + 370)):
    # if fold box clicked
        app.cantChooseThisMove = False
        app.foldAndCheckCount += 1
        app.playerFacts[0][3] = app.moves[5]
        app.yourTurn = False
        app.totalNumberOfClicks += 1
        everyPlayerButOneFolded(app)
    if (((app.width/2 + 490 - event.x)**2 + (app.height/2 - 210 - event.y)**2)**.5 <= 80):
    # if show cards button clicked
        try:
            if app.numberOfButtonPresses > 3:
                print(x)
            else:
                app.showCards = True
                app.playerFacts[0][2] -= 200
                app.numberOfButtonPresses += 1
        except:
            app.cantChooseThisMove = True

def addCards(app):
    for i in range(4):
    # add players cards
        app.playerFacts[i].append(app.tempCards.pop(random.randint(0, len(app.tempCards) - 1)))
        app.playerFacts[i].append(app.tempCards.pop(random.randint(0, len(app.tempCards) - 1)))
    for i in range(4):
    # add cards to be displayed
        app.textOnCards.append(copy.deepcopy(app.playerFacts[i][4]))
        app.textOnCards.append(copy.deepcopy(app.playerFacts[i][5]))
    for i in range(8):
        if app.textOnCards[i][0] == 11:
            app.textOnCards[i][0] = 'J'
        if app.textOnCards[i][0] == 12:
            app.textOnCards[i][0] = 'Q'
        if app.textOnCards[i][0] == 13:
            app.textOnCards[i][0] = 'K'
        if app.textOnCards[i][0] == 14:
            app.textOnCards[i][0] = 'A'
    app.playersCards = True

def preCardRound(app):
    app.errorMessage = False
    app.playerFacts[1][2] -= 20
    app.totalMoneyOnTable += 20
    app.moneyPerRound[1] += 20
    app.playersMoneyOnTable[1] += 20
    if app.foldAndCheckCount > 12:
    # see if you folded or checked too many times
        if app.playerFacts[0][2] >= 20:
            app.playerFacts[0][2] -= 20
        else:
            app.playerFacts[0][2] = 0
    for i in range(1, 4):
        if app.winner != app.playerFacts[i][0] and app.playerFacts[i][2] <= 0:
        # if player is already out, then keep fold
            app.playerFacts[i][3] = app.moves[5]
        elif (app.playerFacts[i] == app.playerFacts[1]):
        # check (only for big blind)
            app.playerFacts[i][3] = app.moves[1]
        elif (app.playerFacts[i][4][0] < 4 and app.playerFacts[i][5][0] < 4 
        and app.playerFacts[i][4][0] != app.playerFacts[i][5][0]):
        # fold
            app.playerFacts[i][3] = app.moves[5]
        elif app.playerFacts[i][3] != app.moves[5]:
        # call
            app.playerFacts[i][3] = app.moves[3]
            if app.playerFacts[i][2] >= 20:
                app.playerFacts[i][2] -= 20
                app.totalMoneyOnTable += 20
                app.moneyPerRound[i] += 20
                app.playersMoneyOnTable[i] += 20
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0

def playerRaised(app):
    for i in range(1, 4):
        if app.playerFacts[i][3] == app.moves[5]:
        # if already fold
            continue
        elif (app.playerFacts[i][4][0] < 6 and app.playerFacts[i][5][0] < 6
        and app.playerFacts[i][4][0] != app.playerFacts[i][5][0]):
        # fold
            app.playerFacts[i][3] = app.moves[5]
        elif app.playerFacts[i][3] != app.moves[5]:
        # call
            app.playerFacts[i][3] = app.moves[3]
            if app.playerFacts[i][2] >= 100:
                app.playerFacts[i][2] -= 100
                app.totalMoneyOnTable += 100
                app.moneyPerRound[i] += 100
                app.playersMoneyOnTable[i] += 100
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0

def playerAllIn(app):
    for i in range(1, 4):
        if (app.playerFacts[i][4][0] > 3 and app.playerFacts[i][5][0] > 3
        and app.playerFacts[i][4][0] == app.playerFacts[i][5][0]
        and (app.winner == app.playerFacts[i][0] or app.playerFacts[i][2] > 0)):
        # all-in as well
            app.playerFacts[i][3] = app.moves[3]
            if app.playerFacts[i][2] > app.allInAmount:
            # if other player has more money than you
                app.playerFacts[i][2] -= app.playersMoneyOnTable[0] - app.playersMoneyOnTable[i]
                app.totalMoneyOnTable += app.playersMoneyOnTable[0] - app.playersMoneyOnTable[i]
                app.moneyPerRound[i] += app.playersMoneyOnTable[0] - app.playersMoneyOnTable[i]
                app.playersMoneyOnTable[i] = app.playersMoneyOnTable[0]
                app.calledAllIn[i] = True
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0
                app.calledAllIn[i] = True
        else: # fold
            app.playerFacts[i][3] == app.moves[5]

def threeCardRound(app):
    app.errorMessage = False
    if app.foldAndCheckCount > 12:
        if app.playerFacts[0][2] >= 20:
            app.playerFacts[0][2] -= 20
        else:
            app.playerFacts[0][2] = 0
    for i in range(3):
        app.cardsOnTable.append(app.tempCards.pop(random.randint(0, len(app.tempCards) - 1)))
    for i in range(3):
        app.textOnCards.append(copy.deepcopy(app.cardsOnTable[i]))
    for i in range(8, 11):
        if app.textOnCards[i][0] == 11:
            app.textOnCards[i][0] = 'J'
        if app.textOnCards[i][0] == 12:
            app.textOnCards[i][0] = 'Q'
        if app.textOnCards[i][0] == 13:
            app.textOnCards[i][0] = 'K'
        if app.textOnCards[i][0] == 14:
            app.textOnCards[i][0] = 'A'
    app.threeCards = True
    findHighestHand(app)
    bluffComponent = 3
    for i in range(1, 4):
        if (app.winner != app.playerFacts[i][0] and app.playerFacts[i][2] <= 0
        or (0 == app.playerFacts[0][2] or 0 == app.playerFacts[1][2] or 0 == app.playerFacts[2][2]
        or 0 == app.playerFacts[3][2])):
            app.playerFacts[i][3] = app.moves[1]
        elif (app.highestHand[i][0] + app.highestHand[i][1] < 5 and app.noRaise == False
        and app.calledAllIn[i] == False):
        # fold
            app.playerFacts[i][3] = app.moves[5]
        elif ((app.highestHand[i][0] + app.highestHand[i][1] >= 8 and app.playerFacts[i][3] != app.moves[5]
        and app.noRaise == True) or (app.playerFacts[i][3] != app.moves[5] and app.noRaise == True and
        random.randint(1,3) == bluffComponent) and app.calledAllIn[i] == False and 
        app.playerFacts[0][2] != 0):
        # raise
            app.playerFacts[i][3] = app.moves[2]
            if app.playerFacts[i][2] >= 100:
                app.playerFacts[i][2] -= 100
                app.totalMoneyOnTable += 100
                app.moneyPerRound[i] += 100
                app.playersMoneyOnTable[i] += 100
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0
            app.noRaise = False
        elif app.playerFacts[i][3] != app.moves[5]:
        #call
            app.playerFacts[i][3] = app.moves[3]
            if app.playerFacts[i][2] >= 100:
                app.playerFacts[i][2] -= 100
                app.totalMoneyOnTable += 100
                app.moneyPerRound[i] += 100
                app.playersMoneyOnTable[i] += 100
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0
    onlyCallOrFold = True
    for i in range(1, 4):
        if app.playerFacts[i][3] != app.moves[3] and app.playerFacts[i][3] != app.moves[5]:
            onlyCallOrFold = False
    if onlyCallOrFold == True:
        for i in range(1, 4):
            if app.playerFacts[i][3] == app.moves[3]:
            # change to check if it was call
                app.playerFacts[i][3] = app.moves[1]
                app.playerFacts[i][2] += 100
                app.totalMoneyOnTable -= 100
                app.moneyPerRound[i] -= 100
                app.playersMoneyOnTable[i] -= 100

def playerRaisedAndCardsOnTable(app):
    for i in range(1, 4):
        if app.playerFacts[i][3] == app.moves[5]:
        # if already fold
            continue
        elif (app.highestHand[i][0] + app.highestHand[i][1] < 20
        and app.moneyPerRound[i] < 100):
        # fold
            app.playerFacts[i][3] = app.moves[5]
        elif app.playerFacts[i][3] != app.moves[5]:
        # call
            app.playerFacts[i][3] = app.moves[3]
            if app.playerFacts[i][2] >= 100:
                app.playerFacts[i][2] -= 100
                app.totalMoneyOnTable += 100
                app.moneyPerRound[i] += 100
                app.playersMoneyOnTable[i] += 100
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0

def playerAllInAndCardsOnTable(app):
    for i in range(1, 4):
        if app.playerFacts[i][3] == app.moves[5]:
        # if already fold
            continue
        elif ((app.highestHand[i][0] + app.highestHand[i][1]) < 12 and 
        app.calledAllIn[i] == False):
        # fold
            app.playerFacts[i][3] = app.moves[5]
        elif app.playerFacts[i][3] != app.moves[5]:
        # call
            app.playerFacts[i][3] = app.moves[3]
            if app.playerFacts[i][2] > app.allInAmount:
                app.playerFacts[i][2] -= app.playersMoneyOnTable[0] - app.playersMoneyOnTable[i]
                app.totalMoneyOnTable += app.playersMoneyOnTable[0] - app.playersMoneyOnTable[i]
                app.moneyPerRound[i] += app.playersMoneyOnTable[0] - app.playersMoneyOnTable[i]
                app.playersMoneyOnTable[i] += app.playersMoneyOnTable[0]
                app.calledAllIn[i] = True
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0
                app.calledAllIn[i] = True

def fourCardRound(app):
    app.noRaise = True
    app.errorMessage = False
    if app.foldAndCheckCount > 12:
        if app.playerFacts[0][2] >= 20:
            app.playerFacts[0][2] -= 20
        else:
            app.playerFacts[0][2] = 0
    app.cardsOnTable.append(app.tempCards.pop(random.randint(0, len(app.tempCards) - 1)))
    app.textOnCards.append(copy.deepcopy(app.cardsOnTable[3]))
    if app.textOnCards[11][0] == 11:
        app.textOnCards[11][0] = 'J'
    if app.textOnCards[11][0] == 12:
        app.textOnCards[11][0] = 'Q'
    if app.textOnCards[11][0] == 13:
        app.textOnCards[11][0] = 'K'
    if app.textOnCards[11][0] == 14:
        app.textOnCards[11][0] = 'A'
    app.fourCards = True
    app.highestHand = []
    findHighestHand(app)
    bluffComponent = 3
    for i in range(1, 4):
        if (app.winner != app.playerFacts[i][0] and app.playerFacts[i][2] <= 0 or
        (0 == app.playerFacts[0][2] or 0 == app.playerFacts[1][2] or 0 == app.playerFacts[2][2]
        or 0 == app.playerFacts[3][2])):
            app.playerFacts[i][3] = app.moves[1]
        if (app.highestHand[i][0] + app.highestHand[i][1] < 10 and app.noRaise == False
        and app.calledAllIn[i] == False):
        # fold
            app.playerFacts[i][3] = app.moves[5]
        elif ((app.highestHand[i][0] + app.highestHand[i][1] >= 10 and app.playerFacts[i][3] != app.moves[5]
        and app.noRaise == True) or (app.playerFacts[i][3] != app.moves[5] and app.noRaise == True and
        random.randint(1,3) == bluffComponent) and app.calledAllIn[i] == False and
        app.playerFacts[0][2] != 0):
        # raise
            app.playerFacts[i][3] = app.moves[2]
            if app.playerFacts[i][2] >= 100:
                app.playerFacts[i][2] -= 100
                app.totalMoneyOnTable += 100
                app.moneyPerRound[i] += 100
                app.playersMoneyOnTable[i] += 100
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0
            app.noRaise = False
        elif app.playerFacts[i][3] != app.moves[5]:
        #call
            app.playerFacts[i][3] = app.moves[3]
            if app.playerFacts[i][2] >= 100:
                app.playerFacts[i][2] -= 100
                app.totalMoneyOnTable += 100
                app.moneyPerRound[i] += 100
                app.playersMoneyOnTable[i] += 100
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0
    onlyCallOrFold = True
    for i in range(1, 4):
        if app.playerFacts[i][3] != app.moves[3] and app.playerFacts[i][3] != app.moves[5]:
            onlyCallOrFold = False
    if onlyCallOrFold == True:
        for i in range(1, 4):
            if app.playerFacts[i][3] == app.moves[3]:
            # change to check if it was call
                app.playerFacts[i][3] = app.moves[1]
                app.playerFacts[i][2] += 100
                app.totalMoneyOnTable -= 100
                app.moneyPerRound[i] -= 100
                app.playersMoneyOnTable[i] -= 100

def fiveCardRound(app):
    app.noRaise = True
    app.errorMessage = False
    if app.foldAndCheckCount > 12:
        if app.playerFacts[0][2] >= 20:
            app.playerFacts[0][2] -= 20
        else:
            app.playerFacts[0][2] = 0
    app.cardsOnTable.append(app.tempCards.pop(random.randint(0, len(app.tempCards) - 1)))
    app.textOnCards.append(copy.deepcopy(app.cardsOnTable[4]))
    if app.textOnCards[12][0] == 11:
        app.textOnCards[12][0] = 'J'
    if app.textOnCards[12][0] == 12:
        app.textOnCards[12][0] = 'Q'
    if app.textOnCards[12][0] == 13:
        app.textOnCards[12][0] = 'K'
    if app.textOnCards[12][0] == 14:
        app.textOnCards[12][0] = 'A'
    app.fiveCards = True
    app.highestHand = []
    findHighestHand(app)
    bluffComponent = 3
    for i in range(1, 4):
        if (app.winner != app.playerFacts[i][0] and app.playerFacts[i][2] <= 0 or
        (0 == app.playerFacts[0][2] or 0 == app.playerFacts[1][2] or 0 == app.playerFacts[2][2]
        or 0 == app.playerFacts[3][2])):
            app.playerFacts[i][3] = app.moves[1]
        if (app.highestHand[i][0] + app.highestHand[i][1] < 15 and app.noRaise == False
        and app.calledAllIn[i] == False):
        # fold
            app.playerFacts[i][3] = app.moves[5]
        elif ((app.highestHand[i][0] + app.highestHand[i][1] >= 15 and app.playerFacts[i][3] != app.moves[5]
        and app.noRaise == True) or (app.playerFacts[i][3] != app.moves[5] and app.noRaise == True and
        random.randint(1,3) == bluffComponent) and app.calledAllIn[i] == False and
        app.playerFacts[0][2] != 0):
        # raise
            app.playerFacts[i][3] = app.moves[2]
            if app.playerFacts[i][2] >= 100:
                app.playerFacts[i][2] -= 100
                app.totalMoneyOnTable += 100
                app.moneyPerRound[i] += 100
                app.playersMoneyOnTable[i] += 100
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0
            app.noRaise = False
        elif app.playerFacts[i][3] != app.moves[5]:
        #call
            app.playerFacts[i][3] = app.moves[3]
            if app.playerFacts[i][2] >= 100:
                app.playerFacts[i][2] -= 100
                app.totalMoneyOnTable += 100
                app.moneyPerRound[i] += 100
                app.playersMoneyOnTable[i] += 100
            else:
                app.totalMoneyOnTable += app.playerFacts[i][2]
                app.moneyPerRound[i] += app.playerFacts[i][2]
                app.playersMoneyOnTable[i] += app.playerFacts[i][2]
                app.playerFacts[i][2] = 0
    onlyCallOrFold = True
    for i in range(1, 4):
        if app.playerFacts[i][3] != app.moves[3] and app.playerFacts[i][3] != app.moves[5]:
            onlyCallOrFold = False
    if onlyCallOrFold == True:
        for i in range(1, 4):
            if app.playerFacts[i][3] == app.moves[3]:
            # change to check if it was call
                app.playerFacts[i][3] = app.moves[1]
                app.playerFacts[i][2] += 100
                app.totalMoneyOnTable -= 100
                app.moneyPerRound[i] -= 100
                app.playersMoneyOnTable[i] -= 100
    # remove later
    for i in range(4):
        print(app.playerFacts[i][4])
        print(app.playerFacts[i][5])
        print('\n')
    print(app.highestHand)

def findHighestHand(app):
    # give each hand a number 0 - 90 (90 is best)
    for i in range(4):
        if (app.winner != app.playerFacts[i][0] and app.playerFacts[i][2] <= 0):
            continue
    # straight flush?
        rank = [-1, -1]
        rank.append(app.playerFacts[i][4][0])
        rank.append(app.playerFacts[i][5][0])
        for j in range(len(app.cardsOnTable)):
            rank.append(app.cardsOnTable[j][0])
        rank.sort()
        while len(rank) > 7:
            rank.pop(0)
        suit = []
        suit.append(app.playerFacts[i][4][1])
        suit.append(app.playerFacts[i][5][1])
        for j in range(len(app.cardsOnTable)):
            suit.append(app.cardsOnTable[j][1])
        FiveOfSameSuit = False
        for j in range(len(suit)):
            if suit.count(suit[j]) == 5:
                FiveOfSameSuit = suit[j]
        if ((FiveOfSameSuit != False) and
        (rank[0] + 4 == rank[1] + 3 == rank[2] + 2 == rank[3] + 1 == rank[4]
        or rank[1] + 4 == rank[2] + 3 == rank[3] + 2 == rank[4] + 1 == rank[5]
        or rank[2] + 4 == rank[3] + 3 == rank[4] + 2 == rank[5] + 1 == rank[6])):
            app.highestHand.append([80, 0])
    # four of a kind?
        if len(app.highestHand) < 1 + i:
            rank = []
            rank.append(app.playerFacts[i][4][0])
            rank.append(app.playerFacts[i][5][0])
            for j in range(len(app.cardsOnTable)):
                rank.append(app.cardsOnTable[j][0])
            rank.sort()
            fourOfAKind = False
            for j in range(len(rank)):
                if rank.count(rank[j]) == 4:
                    fourOfAKind = True
            if fourOfAKind == True:
                app.highestHand.append([70, 9*rank[3]/14])
    # full house?
        if len(app.highestHand) < 1 + i:
            rank = []
            rank.append(app.playerFacts[i][4][0])
            rank.append(app.playerFacts[i][5][0])
            for j in range(len(app.cardsOnTable)):
                rank.append(app.cardsOnTable[j][0])
            rank.sort()
            threeCardRank = False
            for j in range(len(rank)):
                if rank.count(rank[j]) == 3:
                    threeCardRank = rank[j]
            twoCardRank = False
            for j in range(len(rank)):
                if rank.count(rank[j]) == 2 and rank[j] != threeCardRank:
                    twoCardRank = rank[j]
            if threeCardRank != False and twoCardRank != False :
                app.highestHand.append([60, 9*threeCardRank/14])
    # flush?
        if len(app.highestHand) < 1 + i:
            suit = []
            suit.append(app.playerFacts[i][4][1])
            suit.append(app.playerFacts[i][5][1])
            for j in range(len(app.cardsOnTable)):
                suit.append(app.cardsOnTable[j][1])
            FiveOfSameSuit = False
            for j in range(len(suit)):
                if suit.count(suit[j]) == 5:
                    FiveOfSameSuit = suit[j]
            if FiveOfSameSuit != False:
                app.highestHand.append([50, 0])
    # straight?
        if len(app.highestHand) < 1 + i:
            rank = [-1, -1]
            rank.append(app.playerFacts[i][4][0])
            rank.append(app.playerFacts[i][5][0])
            for j in range(len(app.cardsOnTable)):
                rank.append(app.cardsOnTable[j][0])
            rank.sort()
            while len(rank) > 7:
                rank.pop(0)
            if ((rank[0] + 4 == rank[1] + 3 == rank[2] + 2 == rank[3] + 1 == rank[4])
            or (rank[1] + 4 == rank[2] + 3 == rank[3] + 2 == rank[4] + 1 == rank[5])
            or (rank[2] + 4 == rank[3] + 3 == rank[4] + 2 == rank[5] + 1 == rank[6])):
                app.highestHand.append([40, 0])
    # three of a kind?
        if len(app.highestHand) < 1 + i:
            rank = []
            rank.append(app.playerFacts[i][4][0])
            rank.append(app.playerFacts[i][5][0])
            for j in range(len(app.cardsOnTable)):
                rank.append(app.cardsOnTable[j][0])
            threeOfAKind = set()
            for j in range(len(rank)):
                if rank.count(rank[j]) == 3:
                    threeOfAKind.add(rank[j])
            if threeOfAKind != set():
                app.highestHand.append([30, 9*max(threeOfAKind)/14])
    # two pair?
        if len(app.highestHand) < 1 + i:
            rank = []
            rank.append(app.playerFacts[i][4][0])
            rank.append(app.playerFacts[i][5][0])
            for j in range(len(app.cardsOnTable)):
                rank.append(app.cardsOnTable[j][0])
            rank.sort()
            findBiggestPair = set()
            for j in range(len(rank)):
                if rank.count(rank[j]) == 2:
                    findBiggestPair.add(rank[j])
            if len(findBiggestPair) >= 2:
                biggerPair = max(findBiggestPair)
                smallerPair = min(findBiggestPair)
                app.highestHand.append([20, 4.5*biggerPair/14 + 4.5*smallerPair/14])
    # pair?
        if len(app.highestHand) < 1 + i:
            rank = []
            rank.append(app.playerFacts[i][4][0])
            rank.append(app.playerFacts[i][5][0])
            for j in range(len(app.cardsOnTable)):
                rank.append(app.cardsOnTable[j][0])
            pair = set()
            for j in range(len(rank)):
                if rank.count(rank[j]) == 2:
                    pair.add(rank[j])
            if len(pair) >= 1:
                app.highestHand.append([10, 9*max(pair)/14])
    # highest card?
        if len(app.highestHand) < 1 + i:
            rank = []
            rank.append(app.playerFacts[i][4][0])
            rank.append(app.playerFacts[i][5][0])
            for j in range(len(app.cardsOnTable)):
                rank.append(app.cardsOnTable[j][0])
            app.highestHand.append([0, 9*max(rank)/14])

def findWinner(app):
    app.errorMessage = False
    findHighestScore = []
    if app.keyPresses == 5:
        for i in range(len(app.highestHand)):
            if app.playerFacts[i][3] != app.moves[5]:
                findHighestScore.append(app.highestHand[i][0] + app.highestHand[i][1])
            else:
                findHighestScore.append(0)
        for i in range(len(findHighestScore)):
            if (max(findHighestScore) == findHighestScore[i] and 
            (app.winner == app.playerFacts[i][0] or app.playerFacts[i][2] >= 0)):
            # add winners to list
                app.winner.append(app.playerFacts[i][0])
                if 0 <= app.highestHand[i][0] < 10:
                    app.handOfWinner = 'high card'
                if 10 <= app.highestHand[i][0] < 20:
                    app.handOfWinner = 'pair'
                if 20 <= app.highestHand[i][0] < 30:
                    app.handOfWinner = 'two pairs'
                if 30 <= app.highestHand[i][0] < 40:
                    app.handOfWinner = 'three of a kind'
                if 40 <= app.highestHand[i][0] < 50:
                    app.handOfWinner = 'straight'
                if 50 <= app.highestHand[i][0] < 60:
                    app.handOfWinner = 'flush'
                if 60 <= app.highestHand[i][0] < 70:
                    app.handOfWinner = 'full house'
                if 70 <= app.highestHand[i][0] < 80:
                    app.handOfWinner = 'four of a kind'
                if 80 <= app.highestHand[i][0]:
                    app.handOfWinner = 'straight flush'

def everyPlayerButOneFolded(app):
    if (app.playerFacts[0][3] != app.moves[5] and app.playerFacts[1][3] == app.moves[5]
    and app.playerFacts[2][3] == app.moves[5] and app.playerFacts[3][3] == app.moves[5]):
    # if only you don't fold
        app.playerFacts[0][2] += app.totalMoneyOnTable
        app.winner.append(app.playerFacts[0][0])
        app.handOfWinner = 'None'
    if (app.playerFacts[0][3] == app.moves[5] and app.playerFacts[1][3] != app.moves[5]
    and app.playerFacts[2][3] == app.moves[5] and app.playerFacts[3][3] == app.moves[5]):
    # if only player 1 doesn't fold
        app.playerFacts[1][2] += app.totalMoneyOnTable
        app.winner.append(app.playerFacts[1][0])
        app.handOfWinner = 'None'
    if (app.playerFacts[0][3] == app.moves[5] and app.playerFacts[1][3] == app.moves[5]
    and app.playerFacts[2][3] != app.moves[5] and app.playerFacts[3][3] == app.moves[5]):
    # if only player 2 doesn't fold
        app.playerFacts[2][2] += app.totalMoneyOnTable
        app.winner.append(app.playerFacts[2][0])
        app.handOfWinner = 'None'
    if (app.playerFacts[0][3] == app.moves[5] and app.playerFacts[1][3] == app.moves[5]
    and app.playerFacts[2][3] == app.moves[5] and app.playerFacts[3][3] != app.moves[5]):
    # if only player 3 doesn't fold
        app.playerFacts[3][2] += app.totalMoneyOnTable
        app.winner.append(app.playerFacts[3][0])
        app.handOfWinner = 'None'

def addMoney(app):
# splits money between winners
    if len(app.winner) == 1:
        for i in range(4):
            if app.winner[0] in app.playerFacts[i]:
                app.playerFacts[i][2] += app.totalMoneyOnTable
    if len(app.winner) == 2:
        for i in range(4):
            if app.winner[0] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/2, 4)
            if app.winner[1] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/2, 4)
    if len(app.winner) == 3:
        for i in range(4):
            if app.winner[0] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/3, 4)
            if app.winner[1] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/3, 4)
            if app.winner[2] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/3, 4)
    if len(app.winner) == 4:
        for i in range(4):
            if app.winner[0] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/4, 4)
            if app.winner[1] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/4, 4)
            if app.winner[2] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/4, 4)
            if app.winner[3] in app.playerFacts[i]:
                app.playerFacts[i][2] += round(app.totalMoneyOnTable/4, 4)

def drawYourCards(app, canvas):
    # cards
    canvas.create_rectangle(app.width/2 - 120, app.height/2 + 250, app.width/2 - 20, app.height/2 + 400,
    fill = 'ivory', outline = 'black', width = 3)
    canvas.create_rectangle(app.width/2 + 20, app.height/2 + 250, app.width/2 + 120, app.height/2 + 400,
    fill = 'ivory', outline = 'black', width = 3)
    # suit and rank on first card
    centerx = app.width/2 - 70
    centery = app.height/2 + 325
    suitOne = app.playerFacts[0][4][1]
    canvas.create_text(app.width/2 - 100, app.height/2 + 270, text = app.textOnCards[0][0],
    fill = 'red' if (suitOne == 'h' or suitOne == 'd') else 'black', font = 'Arial 16 bold')
    canvas.create_text(app.width/2 - 40, app.height/2 + 380, text = app.textOnCards[0][0],
    fill = 'red' if (suitOne == 'h' or suitOne == 'd') else 'black', font = 'Arial 16 bold')
    if suitOne == 'd': drawDiamond(app, canvas, centerx, centery)
    if suitOne == 'h': drawHeart(app, canvas, centerx, centery)
    if suitOne == 's': drawSpade(app, canvas, centerx, centery)
    if suitOne == 'c': drawClub(app, canvas, centerx, centery)
    # suit and rank on second card
    centerx = app.width/2 + 70
    suitTwo = app.playerFacts[0][5][1]
    canvas.create_text(app.width/2 + 40, app.height/2 + 270, text = app.textOnCards[1][0],
    fill = 'red' if (suitTwo == 'h' or suitTwo == 'd') else 'black', font = 'Arial 16 bold')
    canvas.create_text(app.width/2 + 100, app.height/2 + 380, text = app.textOnCards[1][0],
    fill = 'red' if (suitTwo == 'h' or suitTwo == 'd') else 'black', font = 'Arial 16 bold')
    if suitTwo == 'd': drawDiamond(app, canvas, centerx, centery)
    if suitTwo == 'h': drawHeart(app, canvas, centerx, centery)
    if suitTwo == 's': drawSpade(app, canvas, centerx, centery)
    if suitTwo == 'c': drawClub(app, canvas, centerx, centery)

def drawDiamond(app, canvas, centerx, centery):
    canvas.create_polygon(centerx - 20, centery, centerx, centery - 30, centerx + 20,
    centery, centerx, centery + 30, fill = 'red')

def drawHeart(app, canvas, centerx, centery):
    # triangle
    canvas.create_polygon(centerx - 20, centery - 12, centerx + 20, centery - 12, centerx, 
    centery + 18, fill = 'red')
    # two circles
    canvas.create_oval(centerx - 18, centery - 22, centerx, centery - 2, fill = 'red',
    width = 0)
    canvas.create_oval(centerx, centery - 22, centerx + 18, centery - 2, fill = 'red',
    width = 0)

def drawSpade(app, canvas, centerx, centery):
    # upper triangle
    canvas.create_polygon(centerx, centery - 25, centerx + 20, centery - 5, centerx - 20,
    centery - 5, fill = 'black')
    # two circles
    canvas.create_oval(centerx - 20, centery - 10, centerx, centery + 8, fill = 'black')
    canvas.create_oval(centerx, centery - 10, centerx + 20, centery + 8, fill = 'black')
    # lower triangle
    canvas.create_polygon(centerx, centery - 6, centerx + 10, centery + 25, centerx - 10,
    centery + 25, fill = 'black')

def drawClub(app, canvas, centerx, centery):
    # three circles
    canvas.create_oval(centerx - 20, centery - 12, centerx, centery + 8, fill = 'black')
    canvas.create_oval(centerx, centery - 12, centerx + 20, centery + 8, fill = 'black')
    canvas.create_oval(centerx - 10, centery - 27, centerx + 10, centery - 7, fill = 'black')
    # triangle
    canvas.create_polygon(centerx, centery - 10, centerx + 10, centery + 20, centerx - 10,
    centery + 20, fill = 'black')

def getCellBounds(app, row, col):
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    cellWidth = app.width / app.cols
    cellHeight = app.height / app.rows
    x0 = col * cellWidth
    x1 = (col+1) * cellWidth
    y0 = row * cellHeight
    y1 = (row+1) * cellHeight
    return (x0, y0, x1, y1)

def drawTable(app, canvas):
    canvas.create_oval(app.width/2 - 400, app.height/2 - 200, app.width/2 + 400,
    app.height/2 + 400, fill = 'saddlebrown', outline = 'black', width = 3)
    canvas.create_text(app.width/2, app.height/2 + 100, text = 'Casino Victoria',
    fill = 'black', font = 'Verdana 25 bold')

def drawTiledFloor(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = 'black' if ((row%2 == 0 and col%2 == 0) or 
            (row%2 == 1 and col%2 == 1)) else 'blanchedalmond'
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)

def drawBodies(app, canvas):
    # player 1
    if (app.winner == app.playerFacts[1][0] or app.playerFacts[1][2] > 0
    or (app.playerFacts[1][2] == 0 and app.winner == []) and app.playerFacts[1][0] != 'out'):
        canvas.create_oval(app.width/2 - 470, app.height/2, app.width/2 - 370, 
        app.height/2 + 200, fill = app.bodyColor[0], outline = 'black', width = 1)
    # player 2
    if (app.winner == app.playerFacts[2][0] or app.playerFacts[2][2] > 0
    or (app.playerFacts[2][2] == 0 and app.winner == []) and app.playerFacts[2][0] != 'out'):
        canvas.create_oval(app.width/2 - 100, app.height/2 - 200, app.width/2 + 100, 
        app.height/2 - 300, fill = app.bodyColor[1], outline = 'black', width = 1)
    # player 3
    if (app.winner == app.playerFacts[3][0] or app.playerFacts[3][2] > 0
    or (app.playerFacts[3][2] == 0 and app.winner == []) and app.playerFacts[3][0] != 'out'):
        canvas.create_oval(app.width/2 + 370, app.height/2, app.width/2 + 470, 
        app.height/2 + 200, fill = app.bodyColor[2], outline = 'black', width = 1)

def drawHats(app, canvas):
    # you
    canvas.create_oval(app.width/2 - 70, app.height/2 + 490, app.width/2 + 70, app.height/2 + 490, 
    fill = app.playerFacts[0][1], outline = 'black', width = 3)
    canvas.create_oval(app.width/2 - 40, app.height/2 + 550, app.width/2 + 40, app.height/2 + 630,
    fill = app.playerFacts[0][1], outline = 'black', width = 3)
    # player 1
    if (app.winner == app.playerFacts[1][0] or app.playerFacts[1][2] > 0
    or (app.playerFacts[1][2] == 0 and app.winner == []) and app.playerFacts[1][0] != 'out'):
        canvas.create_oval(app.width/2 - 520, app.height/2 + 30, app.width/2 - 320, 
        app.height/2 + 170, fill = app.playerFacts[1][1], outline = 'black', width = 3)
        canvas.create_oval(app.width/2 - 460, app.height/2 + 60, app.width/2 - 380, 
        app.height/2 + 140, fill = app.playerFacts[1][1], outline = 'black', width = 3)
        canvas.create_text(app.width/2 - 420, app.height/2 + 100, text = app.playerFacts[1][0], 
        fill = 'black', font = 'System 20 bold')
    # player 2
    if (app.winner == app.playerFacts[2][0] or app.playerFacts[2][2] > 0
    or (app.playerFacts[2][2] == 0 and app.winner == []) and app.playerFacts[2][0] != 'out'):
        canvas.create_oval(app.width/2 - 70, app.height/2 - 150, app.width/2 + 70, 
        app.height/2 - 350, fill = app.playerFacts[2][1], outline = 'black', width = 3)
        canvas.create_oval(app.width/2 - 40, app.height/2 - 210, app.width/2 + 40, 
        app.height/2 - 290, fill = app.playerFacts[2][1], outline = 'black', width = 3)
        canvas.create_text(app.width/2, app.height/2 - 270, text = app.playerFacts[2][0], 
        fill = 'black', font = 'System 20 bold')
    # player 3
    if (app.winner == app.playerFacts[3][0] or app.playerFacts[3][2] > 0
    or (app.playerFacts[3][2] == 0 and app.winner == []) and app.playerFacts[3][0] != 'out'):
        canvas.create_oval(app.width/2 + 320, app.height/2 + 30, app.width/2 + 520, 
        app.height/2 + 170, fill = app.playerFacts[3][1], outline = 'black', width = 3)
        canvas.create_oval(app.width/2 + 380, app.height/2 + 60, app.width/2 + 460, 
        app.height/2 + 140, fill = app.playerFacts[3][1], outline = 'black', width = 3)
        canvas.create_text(app.width/2 + 420, app.height/2 + 100, text = app.playerFacts[3][0], 
        fill = 'black', font = 'System 20 bold')

def drawScores(app, canvas):
    # you
    canvas.create_rectangle(app.width/2 - 650, app.height/2 - 400, app.width/2 - 400, app.height/2 - 350,
    fill = 'white', width = 4)
    canvas.create_text(app.width/2 - 525, app.height/2 - 375, text = f'You: ${app.playerFacts[0][2]}',
    font = 'Arial 14 bold')
    # player 1
    if (app.winner == app.playerFacts[1][0] or app.playerFacts[1][2] > 0
    or (app.playerFacts[1][2] == 0 and app.winner == []) and app.playerFacts[1][0] != 'out'):
        canvas.create_rectangle(app.width/2 - 650, app.height/2 - 330, app.width/2 - 400, 
        app.height/2 - 280, fill = app.playerFacts[1][1], width = 4)
        canvas.create_text(app.width/2 - 525, app.height/2 - 305, 
        text = f'{app.playerFacts[1][0]}: ${app.playerFacts[1][2]}', font = 'Arial 14 bold')
    # player 2
    if (app.winner == app.playerFacts[2][0] or app.playerFacts[2][2] > 0
    or (app.playerFacts[2][2] == 0 and app.winner == []) and app.playerFacts[2][0] != 'out'):
        canvas.create_rectangle(app.width/2 - 650, app.height/2 - 260, app.width/2 - 400, 
        app.height/2 - 210, fill = app.playerFacts[2][1], width = 4)
        canvas.create_text(app.width/2 - 525, app.height/2 - 235, 
        text = f'{app.playerFacts[2][0]}: ${app.playerFacts[2][2]}', font = 'Arial 14 bold')
    # player 3
    if (app.winner == app.playerFacts[3][0] or app.playerFacts[3][2] > 0
    or (app.playerFacts[3][2] == 0 and app.winner == []) and app.playerFacts[3][0] != 'out'):
        canvas.create_rectangle(app.width/2 - 650, app.height/2 - 190, app.width/2 - 400, 
        app.height/2 - 140, fill = app.playerFacts[3][1], width = 4)
        canvas.create_text(app.width/2 - 525, app.height/2 - 165, 
        text = f'{app.playerFacts[3][0]}: ${app.playerFacts[3][2]}', font = 'Arial 14 bold')

def drawChipsOnTable(app, canvas):
    # you
    if ((app.winner == app.playerFacts[0][0] or app.playerFacts[0][2] > 0
    or (app.playerFacts[0][2] == 0 and app.winner == [])) and 
    (app.totalNumberOfClicks != 0 or app.moneyPerRound[0] != 0)):
        canvas.create_rectangle(app.width/2 + 50, app.height/2 + 200, app.width/2 + 80,
        app.height/2 + 230, fill = 'gold', width = 0)
        canvas.create_oval(app.width/2 + 50, app.height/2 + 220, app.width/2 + 80,
        app.height/2 + 240, fill = 'gold', width = 0)
        canvas.create_oval(app.width/2 + 50, app.height/2 + 190, app.width/2 + 80,
        app.height/2 + 210, fill = 'gold', outline = 'black', width = 1)
        canvas.create_text(app.width/2 + 65, app.height/2 + 190, text = f'${app.playersMoneyOnTable[0]}',
        font = 'Arial 14 bold')
    # player 1
    if ((app.winner == app.playerFacts[1][0] or app.playerFacts[1][2] > 0
    or (app.playerFacts[1][2] == 0 and app.winner == [])) and 
    (app.totalNumberOfClicks != 0 or app.moneyPerRound[1] != 0) and app.playerFacts[1][0] != 'out'):
        canvas.create_rectangle(app.width/2 - 300, app.height/2 - 40, app.width/2 - 270,
        app.height/2 - 10, fill = 'gold', width = 0)
        canvas.create_oval(app.width/2 - 300, app.height/2 - 20, app.width/2 - 270,
        app.height/2, fill = 'gold', width = 0)
        canvas.create_oval(app.width/2 - 300, app.height/2 - 50, app.width/2 - 270,
        app.height/2 - 30, fill = 'gold', outline = 'black', width = 1)
        canvas.create_text(app.width/2 - 285, app.height/2 - 50, text = f'${app.playersMoneyOnTable[1]}',
        font = 'Arial 14 bold')
    # player 2
    if ((app.winner == app.playerFacts[2][0] or app.playerFacts[2][2] > 0
    or (app.playerFacts[2][2] == 0 and app.winner == [])) and 
    (app.totalNumberOfClicks != 0 or app.moneyPerRound[2] != 0) and app.playerFacts[2][0] != 'out'):
        canvas.create_rectangle(app.width/2 - 15, app.height/2 - 90, app.width/2 + 15,
        app.height/2 - 60, fill = 'gold', width = 0)
        canvas.create_oval(app.width/2 - 15, app.height/2 - 70, app.width/2 + 15,
        app.height/2 - 50, fill = 'gold', width = 0)
        canvas.create_oval(app.width/2 - 15, app.height/2 - 100, app.width/2 + 15,
        app.height/2 - 80, fill = 'gold', outline = 'black', width = 1)
        canvas.create_text(app.width/2, app.height/2 - 100, text = f'${app.playersMoneyOnTable[2]}',
        font = 'Arial 14 bold')
    # player 3
    if ((app.winner == app.playerFacts[3][0] or app.playerFacts[3][2] > 0
    or (app.playerFacts[3][2] == 0 and app.winner == [])) and 
    (app.totalNumberOfClicks != 0 or app.moneyPerRound[3] != 0) and app.playerFacts[3][0] != 'out'):
        canvas.create_rectangle(app.width/2 + 270, app.height/2 - 40, app.width/2 + 300,
        app.height/2 - 10, fill = 'gold', width = 0)
        canvas.create_oval(app.width/2 + 270, app.height/2 - 20, app.width/2 + 300,
        app.height/2, fill = 'gold', width = 0)
        canvas.create_oval(app.width/2 + 270, app.height/2 - 50, app.width/2 + 300,
        app.height/2 - 30, fill = 'gold', outline = 'black', width = 1)
        canvas.create_text(app.width/2 + 285, app.height/2 - 50, text = f'${app.playersMoneyOnTable[3]}',
        font = 'Arial 14 bold')

def drawTextBubbles(app, canvas):
    for i in range(4):
        if (app.winner == app.playerFacts[i][0] or app.playerFacts[i][2] > 0
        or (app.playerFacts[i][2] == 0 and app.winner == []) and app.playerFacts[i][0] != 'out'):
            # print check
            if app.playerFacts[i][3] == app.moves[1]:
                canvas.create_polygon(app.locations[i][0] - 20, app.locations[i][1] - 60, 
                app.locations[i][0] + 20, app.locations[i][1] - 60, app.locations[i][0], 
                app.locations[i][1] - 10, fill = 'NavajoWhite2', outline = 'black', width = 0)
                canvas.create_oval(app.locations[i][0] - 70, app.locations[i][1] - 100,
                app.locations[i][0] + 70, app.locations[i][1] - 50, fill = 'NavajoWhite2', 
                outline = 'black', width = 0)
                canvas.create_text(app.locations[i][0], app.locations[i][1] - 75,
                text = app.moves[1], font = 'System 20 bold')
            # print raise
            if app.playerFacts[i][3] == app.moves[2]:
                canvas.create_polygon(app.locations[i][0] - 20, app.locations[i][1] - 60, 
                app.locations[i][0] + 20, app.locations[i][1] - 60, app.locations[i][0], 
                app.locations[i][1] - 10, fill = 'NavajoWhite2', outline = 'black', width = 0)
                canvas.create_oval(app.locations[i][0] - 70, app.locations[i][1] - 100,
                app.locations[i][0] + 70, app.locations[i][1] - 50, fill = 'NavajoWhite2', 
                outline = 'black', width = 0)
                canvas.create_text(app.locations[i][0], app.locations[i][1] - 75,
                text = app.moves[2], font = 'System 20 bold')
            # print call
            if app.playerFacts[i][3] == app.moves[3]:
                canvas.create_polygon(app.locations[i][0] - 20, app.locations[i][1] - 60, 
                app.locations[i][0] + 20, app.locations[i][1] - 60, app.locations[i][0], 
                app.locations[i][1] - 10, fill = 'NavajoWhite2', outline = 'black', width = 0)
                canvas.create_oval(app.locations[i][0] - 70, app.locations[i][1] - 100,
                app.locations[i][0] + 70, app.locations[i][1] - 50, fill = 'NavajoWhite2', 
                outline = 'black', width = 0)
                canvas.create_text(app.locations[i][0], app.locations[i][1] - 75,
                text = app.moves[3], font = 'System 20 bold')
            # print all in
            if app.playerFacts[i][3] == app.moves[4]:
                canvas.create_polygon(app.locations[i][0] - 20, app.locations[i][1] - 60, 
                app.locations[i][0] + 20, app.locations[i][1] - 60, app.locations[i][0], 
                app.locations[i][1] - 10, fill = 'NavajoWhite2', outline = 'black', width = 0)
                canvas.create_oval(app.locations[i][0] - 70, app.locations[i][1] - 100,
                app.locations[i][0] + 70, app.locations[i][1] - 50, fill = 'NavajoWhite2', 
                outline = 'black', width = 0)
                canvas.create_text(app.locations[i][0], app.locations[i][1] - 75,
                text = app.moves[4], font = 'System 20 bold')
            # print fold
            if app.playerFacts[i][3] == app.moves[5]:
                canvas.create_polygon(app.locations[i][0] - 20, app.locations[i][1] - 60, 
                app.locations[i][0] + 20, app.locations[i][1] - 60, app.locations[i][0], 
                app.locations[i][1] - 10, fill = 'NavajoWhite2', outline = 'black', width = 0)
                canvas.create_oval(app.locations[i][0] - 70, app.locations[i][1] - 100,
                app.locations[i][0] + 70, app.locations[i][1] - 50, fill = 'NavajoWhite2', 
                outline = 'black', width = 0)
                canvas.create_text(app.locations[i][0], app.locations[i][1] - 75,
                text = app.moves[5], font = 'System 20 bold')
            # loser comment
            if (app.moneyAtBeginning[i] - app.playerFacts[i][2] > 300) and app.keyPresses == 5:
                canvas.create_polygon(app.locations[i][0] - 20, app.locations[i][1] - 60, 
                app.locations[i][0] + 20, app.locations[i][1] - 60, app.locations[i][0], 
                app.locations[i][1] - 10, fill = 'NavajoWhite2', outline = 'black', width = 0)
                canvas.create_oval(app.locations[i][0] - 170, app.locations[i][1] - 120,
                app.locations[i][0] + 170, app.locations[i][1] - 30, fill = 'NavajoWhite2', 
                outline = 'black', width = 0)
                canvas.create_text(app.locations[i][0], app.locations[i][1] - 75,
                text = 'Bro, u made me lose so much $$$!', fill = 'red', font = 'System 15 bold')
            # winner comment
            if (app.playerFacts[i][2] - app.moneyAtBeginning[i] > 600) and app.keyPresses == 5:
                canvas.create_polygon(app.locations[i][0] - 20, app.locations[i][1] - 60, 
                app.locations[i][0] + 20, app.locations[i][1] - 60, app.locations[i][0], 
                app.locations[i][1] - 10, fill = 'NavajoWhite2', outline = 'black', width = 0)
                canvas.create_oval(app.locations[i][0] - 170, app.locations[i][1] - 120,
                app.locations[i][0] + 170, app.locations[i][1] - 30, fill = 'NavajoWhite2', 
                outline = 'black', width = 0)
                canvas.create_text(app.locations[i][0], app.locations[i][1] - 75,
                text = 'Boy, I won a lot of $$$!', fill = 'green', font = 'System 15 bold')

def drawMoveBoxes(app, canvas):
    # check box
    canvas.create_rectangle(app.width/2 - 590, app.height/2 + 300, app.width/2 - 440, app.height/2 + 370,
    fill = 'goldenrod', outline = 'black', width = 4)
    canvas.create_text(app.width/2 - 515, app.height/2 + 335, text = 'Check', font = 'Arial 20 bold')
    # raise box
    canvas.create_rectangle(app.width/2 - 410, app.height/2 + 300, app.width/2 - 260, app.height/2 + 370,
    fill = 'orchid', outline = 'black', width = 4)
    canvas.create_text(app.width/2 - 335, app.height/2 + 335, text = 'Raise', font = 'Arial 20 bold')
    # call box
    canvas.create_rectangle(app.width/2 + 160, app.height/2 + 300, app.width/2 + 310, app.height/2 + 370,
    fill = 'teal', outline = 'black', width = 4)
    canvas.create_text(app.width/2 + 235, app.height/2 + 335, text = 'Call', font = 'Arial 20 bold')
    # all in box
    canvas.create_rectangle(app.width/2 + 330, app.height/2 + 300, app.width/2 + 480, app.height/2 + 370,
    fill = 'orangered', outline = 'black', width = 4)
    canvas.create_text(app.width/2 + 405, app.height/2 + 335, text = 'All in', font = 'Arial 20 bold')
    # fold box
    canvas.create_rectangle(app.width/2 + 500, app.height/2 + 300, app.width/2 + 650, app.height/2 + 370,
    fill = 'palegreen', outline = 'black', width = 4)
    canvas.create_text(app.width/2 + 575, app.height/2 + 335, text = 'Fold', font = 'Arial 20 bold')

def drawYourTurn(app, canvas):
    if app.yourTurn == True:
        canvas.create_rectangle(app.width/2 - 80, app.height/2 - 420, app.width/2 + 80, app.height/2 - 380,
        fill = 'white', outline = 'black', width = 3)
        canvas.create_text(app.width/2, app.height/2 - 400, text = 'Your Turn!', font = 'Arial 20 bold')

def drawTotalMoneyOnTable(app, canvas):
    canvas.create_rectangle(app.width/2 + 290, app.height/2 - 400, app.width/2 + 650, app.height/2 - 350,
    fill = 'white', width = 4)
    canvas.create_text(app.width/2 + 470, app.height/2 - 375, text = f'Total money on table: {app.totalMoneyOnTable}',
    font = 'Arial 16 bold')

def drawShowCardsButton(app, canvas):
    canvas.create_oval(app.width/2 + 410, app.height/2 - 290, app.width/2 + 570, app.height/2 - 130,
    fill = 'grey', outline = 'black', width = 2)
    canvas.create_oval(app.width/2 + 430, app.height/2 - 270, app.width/2 + 550, app.height/2 - 150,
    fill = 'red', outline = 'black', width = 2)
    canvas.create_text(app.width/2 + 490, app.height/2 - 210, text = 'Show\ncards', fill = 'black', 
    font = 'Arial 16 bold')

def drawThreeCards(app, canvas):
    # cards
    canvas.create_rectangle(app.width/2 - 310, app.height/2 + 15, app.width/2 - 210, app.height/2 + 165,
    fill = 'ivory', outline = 'black', width = 3)
    canvas.create_rectangle(app.width/2 - 180, app.height/2 + 15, app.width/2 - 80, app.height/2 + 165,
    fill = 'ivory', outline = 'black', width = 3)
    canvas.create_rectangle(app.width/2 - 50, app.height/2 + 15, app.width/2 + 50, app.height/2 + 165,
    fill = 'ivory', outline = 'black', width = 3)
    # text on first card
    suitOne = app.cardsOnTable[0][1]
    canvas.create_text(app.width/2 - 290, app.height/2 + 35, text = app.textOnCards[8][0],
    fill = 'red' if (suitOne == 'h' or suitOne == 'd') else 'black', font = 'Arial 16 bold')
    canvas.create_text(app.width/2 - 230, app.height/2 + 145, text = app.textOnCards[8][0],
    fill = 'red' if (suitOne == 'h' or suitOne == 'd') else 'black', font = 'Arial 16 bold')
    # text on second card
    suitTwo = app.cardsOnTable[1][1]
    canvas.create_text(app.width/2 - 160, app.height/2 + 35, text = app.textOnCards[9][0],
    fill = 'red' if (suitTwo == 'h' or suitTwo == 'd') else 'black', font = 'Arial 16 bold')
    canvas.create_text(app.width/2 - 100, app.height/2 + 145, text = app.textOnCards[9][0],
    fill = 'red' if (suitTwo == 'h' or suitTwo == 'd') else 'black', font = 'Arial 16 bold')
    # text on third card
    suitThree = app.cardsOnTable[2][1]
    canvas.create_text(app.width/2 - 30, app.height/2 + 35, text = app.textOnCards[10][0],
    fill = 'red' if (suitThree == 'h' or suitThree == 'd') else 'black', font = 'Arial 16 bold')
    canvas.create_text(app.width/2 + 30, app.height/2 + 145, text = app.textOnCards[10][0],
    fill = 'red' if (suitThree == 'h' or suitThree == 'd') else 'black', font = 'Arial 16 bold')
    # draw suits
    centery = app.height/2 + 90
    centerx = app.width/2 - 260
    if suitOne == 'd': drawDiamond(app, canvas, centerx, centery)
    if suitOne == 'h': drawHeart(app, canvas, centerx, centery)
    if suitOne == 's': drawSpade(app, canvas, centerx, centery)
    if suitOne == 'c': drawClub(app, canvas, centerx, centery)
    centerx = app.width/2 - 130
    if suitTwo == 'd': drawDiamond(app, canvas, centerx, centery)
    if suitTwo == 'h': drawHeart(app, canvas, centerx, centery)
    if suitTwo == 's': drawSpade(app, canvas, centerx, centery)
    if suitTwo == 'c': drawClub(app, canvas, centerx, centery)
    centerx = app.width/2
    if suitThree == 'd': drawDiamond(app, canvas, centerx, centery)
    if suitThree == 'h': drawHeart(app, canvas, centerx, centery)
    if suitThree == 's': drawSpade(app, canvas, centerx, centery)
    if suitThree == 'c': drawClub(app, canvas, centerx, centery)

def drawFourthCard(app, canvas):
    canvas.create_rectangle(app.width/2 + 80, app.height/2 + 15, app.width/2 + 180, app.height/2 + 165,
    fill = 'ivory', outline = 'black', width = 3)
    suitFour = app.cardsOnTable[3][1]
    canvas.create_text(app.width/2 + 100, app.height/2 + 35, text = app.textOnCards[11][0],
    fill = 'red' if (suitFour == 'h' or suitFour == 'd') else 'black', font = 'Arial 16 bold')
    canvas.create_text(app.width/2 + 160, app.height/2 + 145, text = app.textOnCards[11][0],
    fill = 'red' if (suitFour == 'h' or suitFour == 'd') else 'black', font = 'Arial 16 bold')
    centerx = app.width/2 + 130
    centery = app.height/2 + 90
    if suitFour == 'd': drawDiamond(app, canvas, centerx, centery)
    if suitFour == 'h': drawHeart(app, canvas, centerx, centery)
    if suitFour == 's': drawSpade(app, canvas, centerx, centery)
    if suitFour == 'c': drawClub(app, canvas, centerx, centery)

def drawFifthCard(app, canvas):
    canvas.create_rectangle(app.width/2 + 210, app.height/2 + 15, app.width/2 + 310, app.height/2 + 165,
    fill = 'ivory', outline = 'black', width = 3)
    suitFive = app.cardsOnTable[4][1]
    canvas.create_text(app.width/2 + 230, app.height/2 + 35, text = app.textOnCards[12][0],
    fill = 'red' if (suitFive == 'h' or suitFive == 'd') else 'black', font = 'Arial 16 bold')
    canvas.create_text(app.width/2 + 290, app.height/2 + 145, text = app.textOnCards[12][0],
    fill = 'red' if (suitFive == 'h' or suitFive == 'd') else 'black', font = 'Arial 16 bold')
    centerx = app.width/2 + 260
    centery = app.height/2 + 90
    if suitFive == 'd': drawDiamond(app, canvas, centerx, centery)
    if suitFive == 'h': drawHeart(app, canvas, centerx, centery)
    if suitFive == 's': drawSpade(app, canvas, centerx, centery)
    if suitFive == 'c': drawClub(app, canvas, centerx, centery)

def drawShowAllCards(app, canvas):
    # player 1
    # left card
    if (app.playerFacts[1][3] != app.moves[5] and (app.winner == app.playerFacts[1][0] or 
    app.playerFacts[1][2] > 0 or (app.playerFacts[1][2] == 0 and app.winner == [])) and 
    app.playerFacts[1][0] != 'out'):
        canvas.create_rectangle(app.width/2 - 590, app.height/2 + 15, app.width/2 - 490, 
        app.height/2 + 165, fill = 'ivory', outline = 'black', width = 3)
        P1suitOne = app.playerFacts[1][5][1]
        canvas.create_text(app.width/2 - 570, app.height/2 + 35, text = app.textOnCards[3][0],
        fill = 'red' if (P1suitOne == 'h' or P1suitOne == 'd') else 'black', font = 'Arial 16 bold')
        canvas.create_text(app.width/2 - 510, app.height/2 + 145, text = app.textOnCards[3][0],
        fill = 'red' if (P1suitOne == 'h' or P1suitOne == 'd') else 'black', font = 'Arial 16 bold')
        centery = app.height/2 + 90
        centerx = app.width/2 - 540
        if P1suitOne == 'd': drawDiamond(app, canvas, centerx, centery)
        if P1suitOne == 'h': drawHeart(app, canvas, centerx, centery)
        if P1suitOne == 's': drawSpade(app, canvas, centerx, centery)
        if P1suitOne == 'c': drawClub(app, canvas, centerx, centery)
        # right card
        canvas.create_rectangle(app.width/2 - 460, app.height/2 + 15, app.width/2 - 360, 
        app.height/2 + 165, fill = 'ivory', outline = 'black', width = 3)
        P1suitTwo = app.playerFacts[1][4][1]
        canvas.create_text(app.width/2 - 440, app.height/2 + 35, text = app.textOnCards[2][0],
        fill = 'red' if (P1suitTwo == 'h' or P1suitTwo == 'd') else 'black', font = 'Arial 16 bold')
        canvas.create_text(app.width/2 - 380, app.height/2 + 145, text = app.textOnCards[2][0],
        fill = 'red' if (P1suitTwo == 'h' or P1suitTwo == 'd') else 'black', font = 'Arial 16 bold')
        centerx = app.width/2 - 410
        if P1suitTwo == 'd': drawDiamond(app, canvas, centerx, centery)
        if P1suitTwo == 'h': drawHeart(app, canvas, centerx, centery)
        if P1suitTwo == 's': drawSpade(app, canvas, centerx, centery)
        if P1suitTwo == 'c': drawClub(app, canvas, centerx, centery)
    # player 2
    # left card
    if (app.playerFacts[2][3] != app.moves[5] and (app.winner == app.playerFacts[2][0] or 
    app.playerFacts[2][2] > 0 or (app.playerFacts[2][2] == 0 and app.winner == [])) and
    app.playerFacts[2][0] != 'out'):
        canvas.create_rectangle(app.width/2 - 115, app.height/2 - 300, app.width/2 - 15, 
        app.height/2 - 150, fill = 'ivory', outline = 'black', width = 3)
        P2suitOne = app.playerFacts[2][5][1]
        canvas.create_text(app.width/2 - 95, app.height/2 - 280, text = app.textOnCards[5][0],
        fill = 'red' if (P2suitOne == 'h' or P2suitOne == 'd') else 'black', font = 'Arial 16 bold')
        canvas.create_text(app.width/2 - 35, app.height/2 - 170, text = app.textOnCards[5][0],
        fill = 'red' if (P2suitOne == 'h' or P2suitOne == 'd') else 'black', font = 'Arial 16 bold')
        centery = app.height/2 - 225
        centerx = app.width/2 - 65
        if P2suitOne == 'd': drawDiamond(app, canvas, centerx, centery)
        if P2suitOne == 'h': drawHeart(app, canvas, centerx, centery)
        if P2suitOne == 's': drawSpade(app, canvas, centerx, centery)
        if P2suitOne == 'c': drawClub(app, canvas, centerx, centery)
        # right card
        canvas.create_rectangle(app.width/2 + 15, app.height/2 - 300, app.width/2 + 115, 
        app.height/2 - 150, fill = 'ivory', outline = 'black', width = 3)
        P2suitTwo = app.playerFacts[2][4][1]
        canvas.create_text(app.width/2 + 35, app.height/2 - 280, text = app.textOnCards[4][0],
        fill = 'red' if (P2suitTwo == 'h' or P2suitTwo == 'd') else 'black', font = 'Arial 16 bold')
        canvas.create_text(app.width/2 + 95, app.height/2 - 170, text = app.textOnCards[4][0],
        fill = 'red' if (P2suitTwo == 'h' or P2suitTwo == 'd') else 'black', font = 'Arial 16 bold')
        centerx = app.width/2 + 65
        if P2suitTwo == 'd': drawDiamond(app, canvas, centerx, centery)
        if P2suitTwo == 'h': drawHeart(app, canvas, centerx, centery)
        if P2suitTwo == 's': drawSpade(app, canvas, centerx, centery)
        if P2suitTwo == 'c': drawClub(app, canvas, centerx, centery)
    # player 3
    # left card
    if (app.playerFacts[3][3] != app.moves[5] and (app.winner == app.playerFacts[3][0] or 
    app.playerFacts[3][2] > 0 or (app.playerFacts[3][2] == 0 and app.winner == [])) and
    app.playerFacts[3][0] != 'out'):
        canvas.create_rectangle(app.width/2 + 360, app.height/2 + 15, app.width/2 + 460, 
        app.height/2 + 165, fill = 'ivory', outline = 'black', width = 3)
        P3suitOne = app.playerFacts[3][5][1]
        canvas.create_text(app.width/2 + 380, app.height/2 + 35, text = app.textOnCards[7][0],
        fill = 'red' if (P3suitOne == 'h' or P3suitOne == 'd') else 'black', font = 'Arial 16 bold')
        canvas.create_text(app.width/2 + 440, app.height/2 + 145, text = app.textOnCards[7][0],
        fill = 'red' if (P3suitOne == 'h' or P3suitOne == 'd') else 'black', font = 'Arial 16 bold')
        centery = app.height/2 + 90
        centerx = app.width/2 + 410
        if P3suitOne == 'd': drawDiamond(app, canvas, centerx, centery)
        if P3suitOne == 'h': drawHeart(app, canvas, centerx, centery)
        if P3suitOne == 's': drawSpade(app, canvas, centerx, centery)
        if P3suitOne == 'c': drawClub(app, canvas, centerx, centery)
        # right card
        canvas.create_rectangle(app.width/2 + 490, app.height/2 + 15, app.width/2 + 590, 
        app.height/2 + 165, fill = 'ivory', outline = 'black', width = 3)
        P3suitTwo = app.playerFacts[3][4][1]
        canvas.create_text(app.width/2 + 510, app.height/2 + 35, text = app.textOnCards[6][0],
        fill = 'red' if (P3suitTwo == 'h' or P3suitTwo == 'd') else 'black', font = 'Arial 16 bold')
        canvas.create_text(app.width/2 + 570, app.height/2 + 145, text = app.textOnCards[6][0],
        fill = 'red' if (P3suitTwo == 'h' or P3suitTwo == 'd') else 'black', font = 'Arial 16 bold')
        centerx = app.width/2 + 540
        if P3suitTwo == 'd': drawDiamond(app, canvas, centerx, centery)
        if P3suitTwo == 'h': drawHeart(app, canvas, centerx, centery)
        if P3suitTwo == 's': drawSpade(app, canvas, centerx, centery)
        if P3suitTwo == 'c': drawClub(app, canvas, centerx, centery)

def drawWinner(app, canvas):
    canvas.create_rectangle(app.width/2 - 250, app.height/2 - 400, app.width/2 + 250, app.height/2 - 300,
    fill = 'white', outline = 'black', width = 3)
    if len(app.winner) == 1 and app.handOfWinner == 'None':
        canvas.create_text(app.width/2, app.height/2 - 350, 
        text = f'The winner is {app.winner[0]}! Click the n key to move on\nto the next round nor exit the game to quit playing.', 
        fill = 'blue', font = 'Arial 14 bold')
    elif len(app.winner) == 1:
        canvas.create_text(app.width/2, app.height/2 - 350, 
        text = f'The winner is {app.winner[0]} with a {app.handOfWinner}! Click the n key to\nmove on to the next round or exit the game to quit playing.', 
        fill = 'blue', font = 'Arial 12 bold')
    elif len(app.winner) == 2:
        canvas.create_text(app.width/2, app.height/2 - 350, 
        text = f'The winners are {app.winner[0]} and {app.winner[1]} with a {app.handOfWinner}!\nClick the n key to move on to the next roundor exit the game to\nquit playing.', 
        fill = 'blue', font = 'Arial 10 bold')
    elif len(app.winner) == 3:
        canvas.create_text(app.width/2, app.height/2 - 350, 
        text = f'The winners are {app.winner[0]} and {app.winner[1]} and {app.winner[2]} with\na {app.handOfWinner}!Click the n key to move on to the next round\nor exit the game to quit playing.', 
        fill = 'blue', font = 'Arial 10 bold')
    elif len(app.winner) == 4:
        canvas.create_text(app.width/2, app.height/2 - 350, text = 
        f'The winners are {app.winner[0]} and {app.winner[1]} and {app.winner[2]} and\n{app.winner[3]} with a {app.handOfWinner}! Click the n key to move on\nto the next round or exit the game to quit playing.', 
        fill = 'blue', font = 'Arial 10 bold')

def drawErrorMessage(app, canvas):
# if you press the wrong key
    canvas.create_rectangle(app.width/2 - 250, app.height/2 - 400, app.width/2 + 250, 
    app.height/2 - 300, fill = 'white', outline = 'black', width = 3)
    canvas.create_text(app.width/2, app.height/2 - 350, 
    text = 'You pressed the wrong arrow key. Try again.', 
    fill = 'blue', font = 'Arial 16 bold')

def drawCantChooseThisMove(app, canvas):
    canvas.create_rectangle(app.width/2 - 250, app.height/2 - 400, app.width/2 + 250, 
    app.height/2 - 300, fill = 'white', outline = 'black', width = 3)
    canvas.create_text(app.width/2, app.height/2 - 350, 
    text = 'You cannot choose this move. If you already\n folded,continue to click fold to progress.', 
    fill = 'blue', font = 'Arial 16 bold')

def redrawAll(app, canvas):
    if (app.waitingForFirstKeyPress):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = 'blue')
        canvas.create_text(app.width/2, app.height/2 - 350, 
        text = 'Governor of Poker (112 Version)!', fill = 'chocolate3', font = 'Verdana 30 bold')
        canvas.create_text(app.width/2, app.height/2 + 20, 
        text = '''
        This is a traditional game of Texas Hold'em with some exceptions and things to know.\n
        You are always the last player to make a move. Everyone starts out with $2,000.\n
        To start the pre-flop (no community cards), press the left arrow key. To start the flop\n
        (three community cards), press the up arrow key. To start the turn (4th community card),\n
        press the right arrow key. To start the river (5th community card), press the down arrow\n
        key. To show the winner,press the s key for show. Finally, to move on to the next round,\n 
        press the n key for next. If you fold, then you can quit or continue the game by clicking\n 
        'fold' to see the winner. However, you cannot fold or check continuously for more than\n
        three rounds, or else you'll automatically lose 20 dollars. Also, all straights are equal,\n 
        all flushes are equal, and all straight flushes are equal. Lastly, you can click the\n
        'Show Cards' button at most three times during the game to reveal all of the players'\n
        cards at any time during a round, but you will lose $200 eah time as a result. Now, have\n
        fun and press any key to start the game!
        ''', 
        fill = 'chocolate3', font = 'Arial 16 bold')
    else:
        drawTiledFloor(app, canvas)
        drawTable(app, canvas)
        drawBodies(app, canvas)
        drawHats(app, canvas)
        drawMoveBoxes(app, canvas)
        drawScores(app, canvas)
        if app.playersCards == True:
            drawYourCards(app, canvas)
        drawChipsOnTable(app, canvas)
        drawYourTurn(app, canvas)
        drawTotalMoneyOnTable(app, canvas)
        drawShowCardsButton(app, canvas)
        if app.threeCards == True:
            drawThreeCards(app, canvas)
        if app.fourCards == True:
            drawFourthCard(app, canvas)
        if app.fiveCards == True:
            drawFifthCard(app, canvas)
        if app.keyPresses == 5 or app.showCards == True:
            drawShowAllCards(app, canvas)
        if app.winner != None and app.handOfWinner != None:
            drawWinner(app, canvas)
        drawTextBubbles(app, canvas)
        if app.errorMessage == True:
            drawErrorMessage(app, canvas)
        if app.cantChooseThisMove == True:
            drawCantChooseThisMove(app, canvas)
        if (app.winner != app.playerFacts[0][0] and app.playerFacts[0][2] == 0
        and app.keyPresses == 5):
            # app.time = time.time()
            # while time.time() < app.time + 1:
                # pass
            canvas.create_rectangle(0, 0, app.width, app.height, fill = 'purple')
            canvas.create_text(app.width/2, app.height/2 - 200, 
            text = 'You lose! Press any key to restart the game\nor exit the game if do not wish to play again.', 
            fill = 'brown', font = 'Arial 30 bold')
        for i in range(4):
            if (app.winner == app.playerFacts[i][0] and 3999.5 <= app.playerFacts[i][2] <= 4000.5
            and app.keyPresses == 5):
                if app.winner == app.playerFacts[0][0]:
                # if you won the game
                    # app.time = time.time()
                    # while time.time() < app.time + 1:
                        # pass
                    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'yellow')
                    canvas.create_text(app.width/2, app.height/2 - 200, 
                    text = 'You win! Press any key to restart the game\nor exit the game if do not wish to play again.', 
                    fill = 'red', font = 'Arial 30 bold')
                else:
                # if another player won the game
                    # app.time = time.time()
                    # while time.time() < app.time + 1:
                        # pass
                    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'purple')
                    canvas.create_text(app.width/2, app.height/2 - 200, 
                    text = f'{app.playerFacts[i][0]} wins! Press any key to restart the game\nor exit the game if do not wish to play again.', 
                    fill = 'brown', font = 'Arial 30 bold')

runApp(width=400, height=400)