import re

# multiplications = []
# input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# regex = "mul\\(\\d{1,3},\\d{1,3}\\)"

# instructions = re.findall(regex, input)

# for item in instructions:
#     numbers = re.findall("\\d{1,3}", item)
#     multiplications.append(int(numbers[0]) * int(numbers[1]))

# print(sum(multiplications))

multiplications = []
do_list = []
dont_list = []

current_instructions = 'do'

input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
regex = r"do(?:n't)?\(\)|mul\(\d{1,3},\d{1,3}\)"

instructions = re.findall(regex, input)

for item in instructions:
    inst = re.findall(r"do(?:n't)?|mul", item)

    if inst[0] == 'do':
        current_instructions = 'do'
    elif inst[0] == "don't":
        current_instructions = "don't"
    elif inst[0] == 'mul':
        if current_instructions == 'do':
            do_list.append(item)
        elif current_instructions == "don't":
            dont_list.append(item)

for item in do_list:
    numbers = re.findall(r"\d{1,3}", item)
    multiplications.append(int(numbers[0]) * int(numbers[1]))

print(instructions)
print(do_list, dont_list)
print(sum(multiplications))