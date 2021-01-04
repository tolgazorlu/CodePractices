file = open('test.txt').read().strip('\n')
test = file.splitlines()

def solution(down, right, area):
    count = 0
    x = 0
    y = 0

    while True:
        y = y + down
        if y >= len(area):
            break
        x = (x + right) % len(area[y])
        if area[y][x] == "#":
            count = count + 1

    return count


arr = [[1,1],[1,3],[1,5],[1,7],[2,1]]

result = 1

for x in arr:
    result = result * solution(x[0], x[1], test)

print(result)
