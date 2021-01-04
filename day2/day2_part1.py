def testInput(testFile):
    arr = []
    test = open(testFile, "r")
    for i in test:
        arr.append(i)

    test.close()
    return arr

def validPassword(arr):
    count = 0
    for i in range(len(arr)):
        c = 0
        List = (arr[i].split("-"))
        minNumber = List[0]
        maxNumberList = List[1].split(": ")
        password = maxNumberList[1].split("\\")
        password = password[0]
        maxNumberList = maxNumberList[0].split(" ")
        maxNumber = maxNumberList[0]
        letter = maxNumberList[1]

        for x in password:
            if letter in x:
                c = c + 1
        if( (int(minNumber) <= c) and  (c <= int(maxNumber)) ):
            count = count + 1
            
    return count
    
        
arr = testInput("test.txt")
print(validPassword(arr))
        
    
