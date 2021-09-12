from __future__ import annotations


USE_FILE_IO = True

if USE_FILE_IO:
    from glob import glob
    from os import path

    for input_file in glob(path.join(path.dirname(__file__), "*_input.txt")):
        if input(f'Use this file?\n "{path.basename(input_file)}"" [y(/n)]: ') != 'n':
            break

    INPUT_FILE = input_file
    OUTPUT_FILE = INPUT_FILE.replace('input', 'output')

    stdin = open(INPUT_FILE, 'r', encoding='utf-8')
    stdout = open(OUTPUT_FILE, 'w', encoding='utf-8')
else:
    from sys import stdin, stdout


#######################################################################
#######################################################################

# from __future__ import annotations

import typing as t


BOTH_HAND = 'F'
LEFT_HAND = 'X'
RIGHT_HAND = 'O'

MOD = 1000000007


def next_hand(prev_c, curr_c, left, right) -> t.Tuple[int, int]:
    if prev_c == RIGHT_HAND:
        if curr_c != RIGHT_HAND:
            left = right+1
    elif prev_c == LEFT_HAND:
        if curr_c != LEFT_HAND:
            right = left+1
    else:
        if curr_c == RIGHT_HAND:
            right = min(left+1, right)
        elif curr_c == LEFT_HAND:
            left = min(left, right+1)
    return left, right


def solve():
    N = int(stdin.readline())
    S = stdin.readline().strip()
    answer = 0
    count = 0
    total = N*(N+1)//2
    for s in range(N):
        prev = s
        left = 0
        right = 0
        for e in range(s, N):
            count += 1
            print(f'{count}/{total}', end='\r')
            left, right = next_hand(S[prev], S[e], left, right)
            if S[e] == RIGHT_HAND:
                answer += right
            elif S[e] == LEFT_HAND:
                answer += left
            else:
                answer += min(right, left)
            answer %= MOD
            prev = e
    return answer
345
350

def main():
    T = int(stdin.readline())
    for i in range(1, T+1):
        print(f'Case #{i}/{T}                            ')
        stdout.write(f'Case #{i}: {solve()}\n')


if __name__ == "__main__":
    main()
