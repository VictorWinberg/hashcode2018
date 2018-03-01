from sys import argv
from math import floor, sqrt
from random import randint



def dist(start, end):
    return abs(start[0] - end[0] + start[1] - end[1])

if __name__ == "__main__":
  fname = 'inputs/a_example.in'

  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, F, N, B, T = map(int, f.readline().split(' '))
    content = f.readlines()
    rides = [list(x.strip()) for x in content]

  rides = list(range(N))
  vehicles = [[]] * F
  vehicle_index = 0

  while len(rides) > 0:
    ride_index = randint(0, len(rides) - 1)
    ride = rides.pop(ride_index)
    vehicles[vehicle_index % F].append(ride)
    vehicle_index += 1

  print(vehicles)
