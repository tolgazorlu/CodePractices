def readFile(file):
    arr = []
    test = open(file, "r")
    for i in test:
        arr.append(int(i))
    test.close();
    return arr

def check(arr):
    maxNumber = 0
    for i in range(len(arr) - 2):
        for j in range(i,(len(arr) - 1)):
            if((arr[i] + arr[j] == 2020) and ((arr[i] * arr[j]) > maxNumber)):
                maxNumber = arr[i] * arr[j]

    return maxNumber


newArr = readFile("test.txt")
result = check(newArr)

print(result)
        


