# tic tac toe


##### Constant vars  #####

circle = "O"
axe = "X"
cols, rows = (3,3)
boardGame = [[ ' ' for i in range(cols)] for j in range(rows)]

## Players
player1Name = ""
player2Name = ""

player1Score = 0
player2Score = 0

amountOfGames = 0
tieMatches = 0

player1Mark = axe
player2Mark = circle

# By default player with the axe will start the next game
nextToPlay = player1Name



#######   Functions    ########

def replacingMarksBetweenplayers():
    if player1Mark == axe:
        player1Mark = circle
        player2Mark = axe
    else:
        player1Mark = axe
        player2Mark = circle
    return player1Mark, player2Mark


# returns value to nextToPlay variable who is the next player in the next game
def whoStarts():
    if player1Mark == axe:
        return player1Name
    return player2Name
    

def whatIsThePlayersMarks():
    print(player1Name, "is : ", player1Mark)
    print(player2Name, "is : ", player2Mark)


def SetPlayers():
    print("Player 1")
    player1Name = setPlayerName()
    print("Player 2")
    player2Name = setPlayerName()
    return player1Name, player2Name # in order to upate the variables in the main scope we need to return the values and to update them


def setPlayerName():
    player = input('Enter your name: ') 
    return player


def scores():
    print("Scores")
    print(player1Name, ": ", player1Score)
    print(player2Name, ": ", player2Score)
    print("Total matches: ", amountOfGames)
    print("Ties: ", tieMatches)


def tableView(score = False):
    for row in boardGame:
        print(row)
    if score: # True or False
        scores()


def testValue(value):
    if value == circle or value == axe :
        return True
    return False


def isPlaceTaken(value, col, row):
    if boardGame[col, row] == axe or boardGame[col][row] == circle:
        print("Place taken, select a different place")
        return True
    return False


def insertValue(value, col, row):
    if testValue(value):
        if not isPlaceTaken(value, col, row):
            boardGame[col][row] = value
            return True # action was done successfully
    else:
        print("value is not correct", value)
        sys.exit(1)
    return False


##########  MAIN   ###########

player1Name, player2Name = SetPlayers()

tableView(False)

play()