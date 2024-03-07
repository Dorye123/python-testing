import time


def settingValueInNextFrame(nextFrame, value, col,row):
    nextFrame[col][row] = value

# how to view the frames correctly
def testingView(frame):
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
        # print("frame with ", col, " and ", row, " with value ", value, " will remain alive")
        makeAlive(newFrame, col, row)
    elif isAlive(value) and (count < 2 or count > 3 ):
        # print("frame with ", col, " and ", row, " with value ", value, " will change to dead")
        makeDead(newFrame, col, row)
    elif (not isAlive(value)) and (count == 3):
        makeAlive(newFrame, col, row)

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
                if isAlive(frame[testedCol][testedRow]):
                    count = count + 1
    # print("count = ", count)
    return count
        



# Creating the Blinker
# I will be storing the frames in memory , in 2D lists 
rows, cols = (5, 5)
# Called unevenFrame because it will be representing the uneven frame numbers for example, frame1, frame3, frame5 ....
# And evenFrame represents the even frames.
unevenFrame = [[' ' for i in range(cols)] for j in range(rows)]
evenFrame = [[' ' for i in range(cols)] for j in range(rows)]
# Using lists instead of basic array is better because with arrays we have a bug that all subarrays gets the value if we do this : 
# unevenFrame[3][3] = 1


initPrepareOfUnevenFrame(unevenFrame)
# settingValueInNextFrame(evenFrame, '*', 1, 1 )


print("printing uneven as table")
testingView(unevenFrame)


print("printing even as table")
testingView(evenFrame)

# Going over on uneven and updating even accordingly
# Next level will be to run this in a while true loop to have more than 2 frames presented

# Need to change this to be a temp frame and current frame . and only presenting currentFrame which gets updated once we finish going over the currentFrame and preparing the next frame
# while True: 
#     time.sleep(5)
#     for col in range(0, len(unevenFrame)):
#         for row in range(0, len(unevenFrame[0])):
#         # time.sleep(5) # sleeping 10 seconds
#             checkingSpecificElementConditions(unevenFrame, col, row, evenFrame)
#     print("printing uneven as table")
#     testingView(unevenFrame)
#     print("printing even as table")
#     testingView(evenFrame)



print("printing uneven as table")
testingView(unevenFrame)
print("printing even as table")
testingView(evenFrame)