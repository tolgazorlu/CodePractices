import math

file = open('input.txt').read().strip('\n')
boardingList = file.splitlines()

highestId = 0
idList = []

for boarding in boardingList:
    minRow = 0
    maxRow = 127
    minColumn = 0
    maxColumn = 7

    for letter in boarding[0:7]:
        if letter == "F":
            maxRow = (minRow + maxRow)//2
        else:
            minRow = math.ceil((minRow+maxRow)/2)
    row = minRow

    for letter in boarding[7:10]:
        if letter == "L":
            maxColumn = (minColumn + maxColumn)//2
        else:
            minColumn = math.ceil((minColumn+maxColumn)/2)
    column = minColumn

    seatID = (row * 8) + column
    idList.append(seatID)

idList.sort()

for i in range(len(idList) - 1):
    if i-1 in idList and i+1 in idList and i not in idList:
        print(i)



