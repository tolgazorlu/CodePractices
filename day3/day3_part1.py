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

print(solution(1, 3, test))


