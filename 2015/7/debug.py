def parse_input():
    with open("2015\\7\\input.txt", "r") as file:
        data = file.read()

    return [row for row in data.splitlines()]

INPUT = parse_input()
MATRIX = dict()
WIRES = dict()

for command in INPUT:
    (ops, res) = command.split('->')
    MATRIX[res.strip()] = ops.strip().split(' ')

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in WIRES:
        ops = MATRIX[name]

        if len(ops) == 1:
            res = calculate(ops[0])

        else:
            op = ops[-2]

            if op == 'AND':
              res = calculate(ops[0]) & calculate(ops[2])

            elif op == 'OR':
              res = calculate(ops[0]) | calculate(ops[2])

            elif op == 'NOT':
              res = ~calculate(ops[1]) & 0xffff

            elif op == 'RSHIFT':
              res = calculate(ops[0]) >> calculate(ops[2])

            elif op == 'LSHIFT':
              res = calculate(ops[0]) << calculate(ops[2])

        WIRES[name] = res

    return WIRES[name]

print("a: %d" % calculate('a'))