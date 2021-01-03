def testInput(testFile):
    arr = []
    test = open(testFile, "r")
    for i in test:
        arr.append(i)

    test.close()
    return arr

def validPassword(arr):
    count = 0
    for i in range(len(arr) - 1):
        c = 0
        List = (arr[i].split("-"))
        minNumber = int(List[0])
        maxNumberList = List[1].split(": ")
        password = maxNumberList[1].split("\\")
        password = password[0]
        maxNumberList = maxNumberList[0].split(" ")
        maxNumber = int(maxNumberList[0])
        letter = maxNumberList[1]

        
        if((password[minNumber-1] == letter) and (password[maxNumber-1] == letter)):
            count = count + 1
            
            
    return count
    
        
arr = testInput("test.txt")
print(validPassword(arr))
        
    
