input = ")())())"

with open("C:/Projetos/Advent Of Code/2015/puzzle inputs/1.txt", "r") as file:
    input = file.read()

floor = 0

for i in range(len(input)):
    if input[i] == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        print(i + 1)
        break
