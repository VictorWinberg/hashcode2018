from sys import argv
from math import floor, sqrt
from random import randint

def getStart(start, rideNbr):
    return start[rideNbr]

def getEnd(end,rideNbr):
    return end(rideNbr)

def fillVectors(rides, N):
  start = [range(N)]
  end = [range(N)]
  e_start = [range(N)]
  l_finish = [range(N)]
  for ride in range(N):
    digits = [int(s) for s in rides[ride].split() if s.isdigit()]
    start.append((digits[0], digits[1]))
    end.append((digits[2],digits[3]))
    e_start.append(digits[4])
    l_finish.append(digits[5])
  return start, end, e_start, l_finish


if __name__ == "__main__":
  fname = 'inputs/a_example.in'

  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, F, N, B, T = map(int, f.readline().split(' '))
    content = f.readlines()
    rides = [list(x.strip()) for x in content]

  start, end, e_start, l_finish = fillVectors(content, N)
  rides = list(range(N))
  vehicles = [[]] * F
  vehicle_index = 0

  while len(rides) > 0:
    ride_index = randint(0, len(rides) - 1)
    ride = rides.pop(ride_index)
    vehicles[vehicle_index % F].append(ride)
    vehicle_index += 1

  print(vehicles)
