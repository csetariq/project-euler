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
    max_factor = int(n**0.5) + 1
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n //= factor
            last_factor = factor
            while n % factor == 0:
                n //= factor
            max_factor = int(n**0.5) + 1
        factor += 2

    if n > 1:
        last_factor = n

    print(last_factor)


if __name__ == "__main__":
    main()
