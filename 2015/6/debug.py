import re

matrix = [[0] * 1000 for _ in range(1000)]

# input = [
#     "turn on 0,0 through 0,0",
#     "toggle 0,0 through 999,0",
# ]

with open("2015\\6\\input.txt", "r") as file:
    input = file.read().splitlines()

totalBrightness = 0

for item in input:
    coordinates = re.findall(r"\d+,\d+", item)
    instructions = re.findall(r"(turn on|turn off|toggle)+", item)

    begining = coordinates[0]
    ending = coordinates[1]
    print(begining, ending, instructions)

    for i in range(int(begining.split(",")[0]), int(ending.split(",")[0]) + 1):
        for j in range(int(begining.split(",")[1]), int(ending.split(",")[1]) + 1):
            if instructions[0] == "turn on":
                matrix[i][j] += 1

            elif instructions[0] == "turn off":
                if matrix[i][j] > 0:
                    matrix[i][j] -= 1

                else:
                    matrix[i][j] = 0

            else:
                matrix[i][j] += 2

for i in range(1000):
    for j in range(1000):
        totalBrightness += matrix[i][j]

print(totalBrightness)