input = "2333133121414131402356"

with open("2024\\9\\input.txt", "r") as file:
    input = file.read().strip()

disk = []
id = 0

for i, item in enumerate(input):
    num = int(item)

    if i % 2 == 0:
        disk.extend([id] * num)
        id += 1

    else:
        disk.extend(['.'] * num)

def get_checksum(disk):
    return sum(i * x for i, x in enumerate(disk) if x != '.')

def solve1(disk):
    front = 0
    back = len(disk) - 1

    while True:
        while disk[front] != '.':
            front += 1

        while disk[back] == '.':
            back -= 1

        if front > back:
            break

        disk[front], disk[back] = disk[back], disk[front]

    return get_checksum(disk)


def solve2(disk):
    back = len(disk) - 1

    while True:
        id = None
        from_indicies = []
        to_indicies = []

        while back >= 0:
            item = disk[back]

            if item != '.' and (id == None or id == item):
                id = item
                from_indicies.append(back)
                back -= 1

            elif item == '.' and len(from_indicies) == 0:
                back -= 1

            else:
                break

        front = 0

        while front <= back:
            item = disk[front]

            if item == '.':
                to_indicies.append(front)

                if len(to_indicies) == len(from_indicies):
                    for a, b in zip(from_indicies, to_indicies):
                        disk[a], disk[b] = disk[b], disk[a]

                    break
            else:
                to_indicies = []

            front += 1

        if back < 0:
            break

    return get_checksum(disk)

part1 = solve1(disk.copy())
part2 = solve2(disk)

print(part1)
print(part2)