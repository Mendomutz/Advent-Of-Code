with open("2015\\2\\input.txt", "r") as file:
    input = file.read().splitlines()

l, w, h = 0, 0, 0
total, ribbon, bow = 0, 0, 0

for i in input:
    l, w, h = map(int, i.split('x'))

    ribbon = min(2*l + 2*w, 2*w + 2*h, 2*h + 2*l)
    bow = l*w*h

    total += ribbon + bow

print(total)