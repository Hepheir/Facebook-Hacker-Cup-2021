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

from collections import Counter, deque


BOTH_HAND = 'F'
LEFT_HAND = 'X'
RIGHT_HAND = 'O'

MOD = 1000000007


def solve():
    N = int(stdin.readline())
    S = stdin.readline().strip()

    comp_s = deque()
    comp_c = deque()

    for c in S:
        if comp_s and (c == comp_s[-1] or c == 'F'):
            comp_c[-1] += 1
        else:
            comp_s.append(c)
            comp_c.append(1)

    if len(comp_s) > 1 and comp_s[0] == 'F':
        comp_s.popleft()
        c = comp_c.popleft()
        comp_c[0] += c

    for pivot in range(N):
        pass

    counter = Counter()
    hand = S[0]

    for pivot in range(N):
        if pivot == 0:
            continue

        is_switched = False

        if S[pivot] == BOTH_HAND:
            pass
        else:
            if S[pivot] != hand:
                is_switched = True
                if S[pivot] == RIGHT_HAND:
                    counter['R'] = counter['L']+1
                elif S[pivot] == LEFT_HAND:
                    counter['L'] = counter['R']+1
            hand = S[pivot]

        if is_switched:
            counter['G'] += max(pivot-1, 0)

        counter['ANSWER'] += counter['G']
        counter['ANSWER'] %= MOD
    return counter['ANSWER']


def main():
    T = int(stdin.readline())
    for i in range(1, T+1):
        stdout.write(f'Case #{i}: {solve()}\n')


if __name__ == "__main__":
    main()
