# input = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

import re, time

rules = []
instructions = []

with open("C:/Projetos/Advent Of Code/2024/puzzle inputs/5.txt", "r") as arquivo:
    input = arquivo.read()

rules = input.split("\n\n")[0].split("\n")
instructions = input.split("\n\n")[1].split("\n")

rules = [rule.split("|") for rule in rules]
instructions = [instruction.split(",") for instruction in instructions]

def isCorrectOrder(rule, instruction):
    regex = f"{rule[0]}.*{rule[1]}"  # Regra: item1 deve vir antes de item2
    newInstruction = ", ".join(map(str, instruction))
    match = re.findall(regex, newInstruction)
    return len(match) > 0

def invertItens(instruction, rule):
    new_instruction = instruction[:]
    index1 = new_instruction.index(rule[0])
    index2 = new_instruction.index(rule[1])

    # Inverte os itens
    new_instruction[index1], new_instruction[index2] = new_instruction[index2], new_instruction[index1]

    return new_instruction

def checkInstruction(rules, instruction):
    correct = True
    invertedInstruction = instruction[:]  # Faz uma cópia da instrução inicial

    while True:
        modified = False
        for item in instruction:
            # Regras que envolvem o item atual
            rulesHaveItem = [rule for rule in rules if item in rule]

            # Filtra regras onde ambos os elementos da regra estão na instrução
            newRules = [rule for rule in rulesHaveItem if rule[0] in instruction and rule[1] in instruction]

            for rule in newRules:
                if not isCorrectOrder(rule, invertedInstruction):  # Verifica a ordem
                    invertedInstruction = invertItens(invertedInstruction, rule)  # Ajusta a ordem
                    correct = False
                    modified = True

        if not modified:
            break

    # Retorna o status de correção e a instrução ajustada
    return [correct, invertedInstruction[len(instruction) // 2]]

total = 0
tempo = time.time()

for instruction in instructions:
    result = checkInstruction(rules, instruction)

    if not result[0]:
        total += int(result[1])

tempo = time.time() - tempo

print(total, tempo.__round__(2))