from sys import argv
from math import floor, sqrt
from random import randint

if __name__ == "__main__":
  fname = 'inputs/a_example.in'

  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    rows, columns, vehicles, rides, bonus, steps = map(int, f.readline().split(' '))
    content = f.readlines()
    rides = [list(x.strip()) for x in content]