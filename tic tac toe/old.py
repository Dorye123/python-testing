# # Switch case was added to Python in version 3.10  , so make sure to have this version or newer
# def translateColAndRowToPlace(col, row):
#     switch (col, row):
#         case (0,0):
#             place = 1
#         case (1,0):
#             place = 2
#         case (2,0):
#             place = 3
#         case (0,1):
#             place = 4
#         case (1,1):
#             place = 5
#         case (2,1):
#             place = 6
#         case (0,2):
#             place = 7
#         case (1,2):
#             place = 8
#         case (2,2):
#              place = 9
#         case _:
#             print("Error switching col and row to place failed")
#             sys.exit(1)
#     return place


# # Switch case was added to Python in version 3.10  , so make sure to have this version or newer
# def translatePlaceToColAndRow(place):
#     switch place:
#         case 1:
#             col, row = (0,0)
#         case 2:
#             col, row = (1,0)
#         case 3:
#             col, row = (2,0)
#         case 4:
#             col, row = (0,1)
#         case 5:
#             col, row = (1,1)
#         case 6:
#             col, row = (2,1)
#         case 7:
#             col, row = (0,2)
#         case 8:
#             col, row = (1,2)
#         case 9:
#             col, row = (2,2)
#         case _:
#             print("Error switching place to col and row failed")
#             sys.exit(1)
#     return col, row



# def setInitialValuesToAssistPlacing():
#     intList = range(1,10)
#     intListindex = 0
#     for i in range(0,cols):
#         for j in range(0,rows):
#             boardGame[i][j] = intList[intListindex]
#             intListindex = intListindex + 1
#     # print
#     # for row in boardGame:
#     #     print(row)