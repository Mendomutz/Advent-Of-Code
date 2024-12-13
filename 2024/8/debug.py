# input = """..........
# ..........
# ..........
# ....a.....
# ..........
# .....a....
# ..........
# ..........
# ..........
# .........."""

rows = []

with open("2024\\8\\input.txt", "r") as file:
    content = file.readlines()

    for line in content:
        rows.append(line.strip())

positions = {}

for x, row in enumerate(rows):
    for y, c in enumerate(row):
        if c.isalnum():
            positions.setdefault(c, [])
            positions[c].append((x, y))

distances = {}

for character, pos_list in positions.items():
    for pos in pos_list:
        for j in range(len(pos_list)):
            dis = ((pos[0] - pos_list[j][0]), (pos[1] - pos_list[j][1]))
            distances.setdefault(pos, [])

            if dis != (0, 0):
                distances[pos].append(dis)

marked_puzzle = [list(row) for row in rows]

for pos, dis_list in distances.items():
    for dis in dis_list:
        adjusted_x = pos[0] + dis[0]
        adjusted_y = pos[1] + dis[1]

        if 0 <= adjusted_x < len(rows) and 0 <= adjusted_y < len(rows[adjusted_x]):
            marked_puzzle[adjusted_x][adjusted_y] = "#"

marked_puzzle = ["".join(row) for row in marked_puzzle]

antinode_count = sum(1 for row in marked_puzzle for c in row if c == "#")

print(antinode_count)