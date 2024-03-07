
col = 0
row = 0
count = 0
for testedCol in range(col-1, col+2):
    for testedRow in range(row-1, row+2):
        print()
        print("testedCol = ", testedCol)
        print("testedRow = ", testedRow)
        if testedCol == col and testedRow == row:
            continue
        elif testedCol < 0 or testedRow < 0 :
            continue
        else:
            print("Checking")
            # if isAlive(frame[testedCol][testedRow]):
            count = count + 1
print("count = ", count)
    