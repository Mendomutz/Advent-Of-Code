input = [
    "qjhvhtzxzqqjkmpb",
    "xxyxx",
    "uurcxstgmygtbstg",
    "ieodomkazucvgmuy"
]

totalNice = 0

def has_repeated_pair(string):
    for i in range(len(string) - 1):
        pair = string[i:i+2]

        if pair in string[i+2:]:
            return True

    return False

def contains_separated_pair(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True

    return False

for item in input:
    if has_repeated_pair(item) and contains_separated_pair(item):
        totalNice += 1
        print(item)

print(totalNice)
