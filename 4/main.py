#!/usr/bin/env python3



import sys


def is_palindrome(s):
    return s == s[::-1]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    max_i = 0
    max_j = 0
    max_palindrome = 0
    for i in range(10, n):
        for j in range(10, n):
            product = i * j
            if is_palindrome(str(product)):
                if product > max_palindrome:
                    max_i, max_j = i, j
                    max_palindrome = product
    print(f"{max_i} * {max_j} = {max_palindrome}")


if __name__ == "__main__":
    main()
