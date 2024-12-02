from itertools import combinations

def isSorted(report):
    crescente = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
    decrescente = all(report[i] >= report[i + 1] for i in range(len(report) - 1))

    return crescente or decrescente

def checkDistance(report):
    return all(1 <= abs(report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1))

def isTolerable(report):
    for newReport in combinations(report, len(report) - 1):
        if isSorted(newReport) and checkDistance(newReport):
            return True
    return False

safeReports = 0

with open("C:/Projetos/Advent Of Code/2024/puzzle inputs/2.txt", 'r') as arquivo:
    for linha in arquivo:
        report = list(map(int, linha.strip().split()))

        if isSorted(report) and checkDistance(report):
            safeReports += 1
        elif isTolerable(report):
            safeReports += 1

print(safeReports)
