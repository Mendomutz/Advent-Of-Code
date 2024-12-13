with open("2015\\3\\input.txt", "r") as file:
    input = file.read().splitlines()

def getNextHouse(x, y, direction):
    if direction == '^':
        y += 1

    elif direction == '>':
        x += 1

    elif direction == 'v':
        y -= 1

    elif direction == '<':
        x -= 1

    return x, y

for item in input:
    Sx, Sy, Rx, Ry = 0, 0, 0, 0
    isSanta = True
    visitedHousesBySanta = [(0,0)]
    visitedHousesByRoboSanta = [(0,0)]

    for i in range(len(item)):
        if isSanta:
            Sx, Sy = getNextHouse(Sx, Sy, item[i])
            visitedHousesBySanta.append((Sx, Sy))

        else:
            Rx, Ry = getNextHouse(Rx, Ry, item[i])
            visitedHousesByRoboSanta.append((Rx, Ry))

        isSanta = not isSanta

    visitedHouses = list(set(visitedHousesBySanta + visitedHousesByRoboSanta))

    print(len(visitedHouses))