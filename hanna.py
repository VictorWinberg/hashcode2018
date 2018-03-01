from sys import argv
from math import floor, sqrt
from random import randint

class Ride:
  def __init__(self, index, a, b, x, y, s, f):
    self.index = index
    self.from_pos = (a, b)
    self.to_pos = (x, y)
    self.start = s
    self.finish = f

def getStart(start, rideNbr):
    return start[rideNbr]

def getEnd(end,rideNbr):
    return end(rideNbr)

def fillVectors(rides, N):
  start, end, e_start, l_finish = [], [], [], []
  for ride in range(N):
    digits = [int(s) for s in rides[ride].split() if s.isdigit()]
    start.append((digits[0], digits[1]))
    end.append((digits[2],digits[3]))
    e_start.append(digits[4])
    l_finish.append(digits[5])
  return start, end, e_start, l_finish

def dist(start, end):
  return abs(start[0] - end[0] + start[1] - end[1])

def solve(content, rides, F, N):
    start, end, e_start, l_finish = fillVectors(content, N)
    vehicles = [[] for i in range(F)]
    rides.sort(key=lambda x: x.start, reverse=False)
    vehicle_index = 0

    while len(rides) > 0:
      ride_index = 0 # randint(0, len(rides) - 1)
      ride = rides.pop(ride_index)
      vehicles[vehicle_index % F].append(ride.index)
      vehicle_index += 1

    vehicles_rides = [ [len(vehicle), *vehicle] for vehicle in vehicles]

    with open('outputs/' + fname.split('/')[1], 'w') as f:
      for vehicle in vehicles_rides:
        f.write(' '.join([str(ride) for ride in vehicle]) + '\n')
    return vehicles_rides

if __name__ == "__main__":
  fname = 'inputs/a_example.in'

  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, F, N, B, T = map(int, f.readline().split(' '))
    content = f.readlines()
    rides = [ Ride(i, *list(map(int, x.strip().split(' ')))) for i, x in enumerate(content)]

  times = 1000
  while times > 0:
    vehicle_rides = solve(content, rides, F, N)
