from sys import argv
from math import floor, sqrt
from random import randint

if __name__ == "__main__":
  fname = 'inputs/a_example.in'

  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, F, N, B, T = map(int, f.readline().split(' '))
    content = f.readlines()
    rides = [list(x.strip()) for x in content]

  rides = list(range(N))
  vehicles = [[] for i in range(F)]
  vehicle_index = 0

  while len(rides) > 0:
    ride_index = randint(0, len(rides) - 1)
    ride = rides.pop(ride_index)
    vehicles[vehicle_index % F].append(ride)
    vehicle_index += 1

  vehicles_rides = [ [len(vehicle), *vehicle] for vehicle in vehicles]

  with open('outputs/solution.txt', 'w') as f:
    for vehicle in vehicles_rides:
      f.write(' '.join([str(ride) for ride in vehicle]) + '\n')
