#!/usr/bin/env python3

import sys


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 13195

    factor = 2
    last_factor = 1
    if n % 2 == 0:
        n //= 2
        last_factor = 2
        while n % 2 == 0:
            n //= 2

    factor = 3
    while n > 1:
        if n % factor == 0:
            n //= factor
            last_factor = factor
            while n % factor == 0:
                n //= factor
        factor += 2

    print(last_factor)


if __name__ == "__main__":
    main()
