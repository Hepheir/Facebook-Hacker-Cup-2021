from __future__ import annotations


USE_FILE_IO = True

if USE_FILE_IO:
    from glob import glob
    from os import path

    for input_file in glob(path.join(path.dirname(__file__), "*_input.txt")):
        if input(f'Use this file?\n "{path.basename(input_file)}"" [y(/n)]: ') != "n":
            break

    INPUT_FILE = input_file
    OUTPUT_FILE = INPUT_FILE.replace("input", "output")

    stdin = open(INPUT_FILE, "r", encoding="utf-8")
    stdout = open(OUTPUT_FILE, "w", encoding="utf-8")
else:
    from sys import stdin, stdout


#######################################################################
#######################################################################

# from __future__ import annotations

import typing as t


BOTH_HAND = "F"
LEFT_HAND = "X"
RIGHT_HAND = "O"

MOD = 1000000007


def next_hand(prev_c, curr_c, left, right) -> t.Tuple[int, int]:
    if prev_c == RIGHT_HAND:
        if curr_c != RIGHT_HAND:
            left = right + 1
    elif prev_c == LEFT_HAND:
        if curr_c != LEFT_HAND:
            right = left + 1
    else:
        if curr_c == RIGHT_HAND:
            right = min(left + 1, right)
        elif curr_c == LEFT_HAND:
            left = min(left, right + 1)
    return left, right


def F(char: str, left: int, right: int) -> int:
    if char == RIGHT_HAND:
        return right
    elif char == LEFT_HAND:
        return left
    else:
        return min(right, left)


def G(S: str) -> int:
    left = 0
    right = 0



def solve():
    K = int(stdin.readline())
    U = stdin.readline().strip()
    S = []
    for i in range(K):
        if U[i] in 'FOX':
            S.append(U[i])
        else:
            S.extend(S)
    return 0


def main():
    T = int(stdin.readline())
    for i in range(1, T + 1):
        print(f"Case #{i}/{T}                            ")
        stdout.write(f"Case #{i}: {solve()}\n")


if __name__ == "__main__":
    main()
