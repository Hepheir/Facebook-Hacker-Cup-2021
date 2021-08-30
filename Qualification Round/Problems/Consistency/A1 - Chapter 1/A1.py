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


from collections import Counter
# from sys import stdin, stdout

def is_vowel(c: str) -> bool:
    return c in "AEIOU"


def sub_prob(chosen_counter: Counter, unchosen_counter: Counter):
    answer = 0
    if chosen_counter:
        answer += 2*(sum(chosen_counter.values()) -
                     chosen_counter.most_common(1)[0][1])
    if unchosen_counter:
        answer += sum(unchosen_counter.values())
    return answer


def solve():
    S = stdin.readline().strip()
    counter_of_vowels = Counter()
    counter_of_consonants = Counter()
    for c in S:
        if is_vowel(c):
            counter_of_vowels[c] += 1
        else:
            counter_of_consonants[c] += 1
    return min(sub_prob(counter_of_vowels, counter_of_consonants), sub_prob(counter_of_consonants, counter_of_vowels))


def main():
    T = int(stdin.readline())
    for i in range(1, T+1):
        stdout.write(f'Case #{i}: {solve()}\n')


if __name__ == "__main__":
    main()
