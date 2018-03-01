from sys import argv
from random import randint

class Ride:
  def __init__(self, index, a, b, x, y, s, f):
    self.index = index
    self.from_pos = (a, b)
    self.to_pos = (x, y)
    self.start = s
    self.finish = f

if __name__ == "__main__":
  fname = 'inputs/a_example.in'

  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, F, N, B, T = map(int, f.readline().split(' '))
    content = f.readlines()
    rides = [ Ride(i, *list(map(int, x.strip().split(' ')))) for i, x in enumerate(content)]

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
