# Consistency - Chapter 1

from glob import glob
from os import path

for input_file in glob(path.join(path.dirname(__file__), "*_input.txt")):
    if input(f'Use this file?\n "{path.basename(input_file)}"" [y(/n)]: ') != 'n':
        break

INPUT_FILE = input_file
OUTPUT_FILE = INPUT_FILE.replace('input', 'output')

stdin = open(INPUT_FILE, 'r', encoding='utf-8')
stdout = open(OUTPUT_FILE, 'w', encoding='utf-8')


#######################################################################
#######################################################################


from collections import deque


def solve():
    N = int(stdin.readline())

    BOARD = [[None]*N for _ in range(N)]
    queue = deque()
    for y in range(N):
        C = stdin.readline().strip()
        for x in range(N):
            if C[x] == '.':
                queue.append((y,x))
        BOARD[y] = list(C)

    # TODO
    ...

    return 'Impossible'


def main():
    T = int(stdin.readline())
    for i in range(1, T+1):
        stdout.write(f'Case #{i}: {solve()}\n')


if __name__ == "__main__":
    main()
