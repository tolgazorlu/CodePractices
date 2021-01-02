def readFile(file):
    arr = []
    test = open(file, "r")
    for i in test:
        arr.append(int(i))
    test.close();
    return arr

def check(arr):
    maxNumber = 0
    for i in range(len(arr) - 3):
        for j in range(i,(len(arr) - 2)):
            for k in range(j,(len(arr) - 1)):
                if((arr[i] + arr[j] + arr[k] == 2020) and ((arr[i] * arr[j] * arr[k]) > maxNumber)):
                    maxNumber = arr[i] * arr[j] * arr[k]

    return maxNumber


newArr = readFile("test.txt")
result = check(newArr)

print(result)
        


