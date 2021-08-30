# Consistency - Chapter 1

from collections import defaultdict, deque
from glob import glob
from os import path
from typing import List, Optional, Set

for input_file in glob(path.join(path.dirname(__file__), "*_input.txt")):
    if input(f'Use this file?\n "{path.basename(input_file)}"" [y(/n)]: ') != 'n':
        break

INPUT_FILE = input_file
OUTPUT_FILE = INPUT_FILE.replace('input', 'output')

stdin = open(INPUT_FILE, 'r', encoding='utf-8')
stdout = open(OUTPUT_FILE, 'w', encoding='utf-8')


#######################################################################
#######################################################################


INF = float('inf')


def is_consistent_string(string: str) -> bool:
    return len(set(string)) == 1


def solve():
    S = list(stdin.readline().strip())
    K = int(stdin.readline())

    possible_chars = set(S)
    switchable = defaultdict(lambda: list())
    for i in range(K):
        Ai, Bi = stdin.readline().strip()
        switchable[Ai].append(Bi)
        possible_chars.add(Ai)
        possible_chars.add(Bi)

    # Use Floyd-Warshall
    distances = defaultdict(lambda: defaultdict(lambda: dict()))
    for char_src in possible_chars:
        for char_dst in possible_chars:
            if char_src == char_dst:
                distances[char_src][char_dst] = 0
            elif char_dst in switchable[char_src]:
                distances[char_src][char_dst] = 1
            else:
                distances[char_src][char_dst] = INF
    for char_route in possible_chars:
        for char_src in possible_chars:
            for char_dst in possible_chars:
                distances[char_src][char_dst] = min(
                    distances[char_src][char_dst],
                    distances[char_src][char_route] + distances[char_route][char_dst]
                )

    shortest_distance = INF
    for char_dst in possible_chars:
        dist = 0
        for char_src in S:
            dist += distances[char_src][char_dst]
        shortest_distance = min(dist, shortest_distance)

    # If not solvable returns `-1`
    return shortest_distance if shortest_distance != INF else -1


def main():
    T = int(stdin.readline())
    for i in range(1, T+1):
        stdout.write(f'Case #{i}: {solve()}\n')


if __name__ == "__main__":
    main()
