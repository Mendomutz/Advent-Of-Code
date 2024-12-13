input = '''""
"aaa\\"aaa"
"abc"
"\\x27"'''

def parse_input():
    with open("2015\\8\\input.txt", "r") as file:
        data = file.read()

    return [row for row in input.splitlines()]

def count_encoded_chars(string):
  size = 2

  for i in range(len(string)):
    if string[i] in ['"', '\\']:
      size += 1

  return len(string) + size

def count_chars(string):
    return len(string)

STRINGS = parse_input()
CODE = 0
CHARS = 0

for item in STRINGS:
  CODE += count_encoded_chars(item)
  CHARS += count_chars(item)

print(f"Total encoded code chars: {CODE}")
print(f"Total code chars: {CHARS}")
print(f"Difference: {CODE - CHARS}")