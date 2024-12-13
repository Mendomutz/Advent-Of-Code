import itertools

# input = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

with open("2024\\7\\input.txt", "r") as arquivo:
    input = arquivo.read()

operators = ['+', '*', '||']

soma = [item.split(':')[0].strip() for item in input.split('\n')]
numeros = [item.split(':')[1].strip() for item in input.split('\n')]

result = []

def operation(total, numbers):
    totalSoma = numbers[0]

    for ops in itertools.product(operators, repeat=len(numbers) - 1):
        for i, op in enumerate(ops):
            if op == '+':
                totalSoma += numbers[i + 1]
            elif op == '*':
                totalSoma *= numbers[i + 1]
            elif op == '||':
                number = eval(f"{totalSoma}{numbers[i + 1]}")
                totalSoma = number

        if totalSoma == total:
            result.append(total)
            return
        else:
            totalSoma = numbers[0]

for i in range(len(soma)):
    currentItem = numeros[i]
    currentSoma = soma[i]

    operation(int(currentSoma), [int(x) for x in currentItem.split()])

print(sum(result))