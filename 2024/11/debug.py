# from collections import Counter

# def parse_input():
#     with open("2024\\11\\input.txt", "r") as file:
#         data = file.read()

#     input = "125 17"

#     return list(map(int, input.split(' ')))

# def process_stone(stone, count):
#     result = Counter()

#     if stone == 0:
#         result [1] += count
#     elif len(str(stone)) % 2 == 0:
#         mid = len(str(stone)) // 2
#         stone1 = int(str(stone)[:mid])
#         stone2 = int(str(stone)[mid:])

#         result[stone1] += count
#         result[stone2] += count
#     else:
#         result[stone * 2024] += count

#     return result

# blinking = 75
# input_stones = parse_input()
# stones_count = Counter(input_stones)

# for _ in range(blinking):
#     new_counts = Counter()

#     for stone, count in stones_count.items():
#         new_counts.update(process_stone(stone, count))

#     stones_count = new_counts

# print(sum(stones_count.values()))

import time
from concurrent.futures import ProcessPoolExecutor

def parse_input():
    with open("2024\\11\\input.txt", "r") as file:
        data = file.read()

    return list(map(int, data.split(' ')))

def process_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        stone1 = int(str(stone)[:mid])
        stone2 = int(str(stone)[mid:])

        return [stone1, stone2]

    else:
        return [stone * 2024]

def process_stones_chunk(stones_chunk):
    new_chunk = []

    for stone in stones_chunk:
        new_chunk.extend(process_stone(stone))

    return new_chunk

if __name__ == '__main__':
    blinking = 75
    old_list = parse_input()
    start = time.time()

    for _ in range(blinking):
        chunk_size = len(old_list) // 16 + 1
        chunks = [old_list[i:i + chunk_size] for i in range(0, len(old_list), chunk_size)]

        with ProcessPoolExecutor() as executor:
            results = list(executor.map(process_stones_chunk, chunks))

        old_list = [stone for result in results for stone in result]

        step = time.time()
        print(f"{step - start:2f} seconds, Iteration {_ + 1}, Objects: {len(old_list)}, Chunk size: {chunk_size}, Number of threads: {len(results)}")

    finish = time.time()

    print(len(old_list))
    print(f"{finish - start} seconds")
