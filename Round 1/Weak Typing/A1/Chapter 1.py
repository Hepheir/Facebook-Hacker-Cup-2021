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


BOTH_HAND = 'F'
LEFT_HAND = 'X'
RIGHT_HAND = 'O'


def solve():
    N = int(stdin.readline())
    W = stdin.readline().strip()

    last_char = W[0]
    left_hand = 0
    right_hand = 0

    for c in W:
        if c == last_char:
            pass

        elif c == BOTH_HAND:
            if last_char == RIGHT_HAND: # Right hand
                left_hand = right_hand+1
            elif last_char == LEFT_HAND: # Left hand
                right_hand = left_hand+1
            else:
                raise ValueError()

        elif c == RIGHT_HAND: # Right hand
            if last_char == BOTH_HAND:
                right_hand = min(left_hand+1, right_hand)
            elif last_char == LEFT_HAND: # Left hand
                right_hand = left_hand+1
            else:
                raise ValueError()

        elif c == LEFT_HAND: # Left hand
            if last_char == BOTH_HAND:
                left_hand = min(left_hand, right_hand+1)
            elif last_char == RIGHT_HAND:
                left_hand = right_hand+1
            else:
                raise ValueError()
        else:
            raise ValueError()

        last_char = c

    if last_char == BOTH_HAND:
        return min(left_hand, right_hand)
    elif last_char == RIGHT_HAND:
        return right_hand
    elif last_char == LEFT_HAND:
        return left_hand
    else:
        raise ValueError()



def main():
    T = int(stdin.readline())
    for i in range(1, T+1):
        stdout.write(f'Case #{i}: {solve()}\n')


if __name__ == "__main__":
    main()
