import time

def settingValueInNextFrame(nextFrame, value, col,row):
    nextFrame[col][row] = value

# how to view the frames correctly
def tableView(frame):
    for row in frame:
        print(row)

# for a 5*5 frame
def initPrepareOfUnevenFrame(frame):
    frame[1][2] = '*'
    frame[2][2] = '*'
    frame[3][2] = '*'

# conditions of the blinker:
# if alive and surronded by less than 2 alive. make it dead
# if alive and surronded by more than 3 alive. make it dead
# if alive and surronded by 2 or 3 exactly . stay alive
# if dead and surronded by 3 alive. make it alive.
def checkingSpecificElementConditions(frame, col, row, newFrame):
    count = howManyAliveAroundCurrent(frame, col, row)
    value = frame[col][row]
    if (isAlive(value)) and ((count == 2) or (count == 3)) :
        # print("frame with col:", col, " and row:", row, " with value", value, " will remain alive")
        makeAlive(newFrame, col, row)
    elif isAlive(value) and (count < 2 or count > 3 ):
        # print("frame with col:", col, " and row:", row, " with value", value, " will change to dead")
        makeDead(newFrame, col, row)
    elif (not isAlive(value)) and (count == 3):
        # print("frame with col:", col, " and row:", row, " with value", value, " will become alive")
        makeAlive(newFrame, col, row)
    else:
        # print("frame with col:", col, " and row:", row, " with value", value, " will remain dead")
        makeDead(newFrame, col, row)

# Alive is '*', Dead is ' ' 
def isAlive(valueFromFrame):
    if valueFromFrame == '*': 
        return True
    return False

def isAliveStr(valueFromFrame):
    if valueFromFrame == '*': 
        return "alive"
    return "dead"

def makeDead(frame, col, row):
    frame[col][row] = ' '

def makeAlive(frame, col, row):
    frame[col][row] = '*'

def howManyAliveAroundCurrent(frame, col, row):
    count = 0
    # print("Testing element in location col: ", col, " row: ", row, " which is ", isAliveStr(frame[col][row]))
    for testedCol in range(col-1, col+2):
        for testedRow in range(row-1, row+2):
            # print()
            # print("testedCol = ", testedCol)
            # print("testedRow = ", testedRow)
            if testedCol == col and testedRow == row:
                continue
            elif testedCol < 0 or testedRow < 0 or testedCol >= len(frame) or testedRow >= len(frame[col]) :
                continue
            else:
                # print("Counting")
                if isAlive(frame[testedCol][testedRow]):
                    count = count + 1
                    # print("count is ", count)
    # print("count = ", count)
    return count
        
def printingFrame(frame, frameCount):
    print()
    print("Printing frame", frameCount, "as table")
    tableView(frame) 

####################    MAIN     #################
# Creating the Blinker
# I will be storing the frames in memory , in 2D lists 
rows, cols = (5, 5)
mainFrame = [[' ' for i in range(cols)] for j in range(rows)]
tempFrame = [[' ' for i in range(cols)] for j in range(rows)]
initPrepareOfUnevenFrame(mainFrame)
frameCount = 1
printingFrame(mainFrame, frameCount)
while True: 
    for col in range(0, len(mainFrame)):
        for row in range(0, len(mainFrame[0])):
            checkingSpecificElementConditions(mainFrame, col, row, tempFrame)
    mainFrame = tempFrame
    tempFrame = [[' ' for i in range(cols)] for j in range(rows)]
    frameCount = frameCount + 1
    printingFrame(mainFrame, frameCount)
    time.sleep(2)