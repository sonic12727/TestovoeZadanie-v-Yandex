import sys


def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]);
    ptr += 1
    m = int(input[ptr]);
    ptr += 1
    x = int(input[ptr]);
    ptr += 1
    y = int(input[ptr]);
    ptr += 1

    threshold = (x * y + 1) // 2
    awake = 0

    for _ in range(n):
        for _ in range(m):
            lit = 0
            for _ in range(x):
                row = input[ptr];
                ptr += 1
                for c in row:
                    if c == 'X':
                        lit += 1
                        if lit >= threshold:
                            break
                if lit >= threshold:
                    break
            if lit >= threshold:
                awake += 1

    print(awake)


if __name__ == "__main__":
    main()