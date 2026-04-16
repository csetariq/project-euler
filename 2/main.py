#!/usr/bin/env python3

def main():
  sum = 0
  prev, cur = 1, 2
  while cur < 4000000:
    if cur % 2 == 0:
      sum += cur
    prev, cur = cur, prev + cur
  print(sum)

if __name__ == "__main__":
  main()
