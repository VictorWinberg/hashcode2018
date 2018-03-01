from sys import argv
from math import floor, sqrt
from random import randint

def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def validate(rides, vehicles_rides, B, T):
    score = 0
    for vehicle in vehicles_rides:
        vehicle_start = (0, 0)
        steps = 0
        for v in vehicle[1:]:
            v_dist = dist(vehicle_start, rides[v].from_pos)
            steps += v_dist
            if steps <= rides[v].start:
                steps = rides[v].start
                score += B
            ride_dist = dist(rides[v].from_pos, rides[v].to_pos)
            steps += ride_dist
            vehicle_start = rides[v].to_pos
            if steps > rides[v].finish: continue
            score += ride_dist

    print("SCORE: {}".format(score))
    return score

class Ride:
  def __init__(self, index, a, b, x, y, s, f):
    self.index = index
    self.from_pos = (a, b)
    self.to_pos = (x, y)
    self.start = s
    self.finish = f

if __name__ == "__main__":
  fname = 'inputs/b_should_be_easy.in'

  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, F, N, B, T = map(int, f.readline().split(' '))
    content = f.readlines()
    rides = [ Ride(i, *list(map(int, x.strip().split(' ')))) for i, x in enumerate(content)]
    val_rides = [r for r in rides]
  vehicles = [[] for i in range(F)]

  rides.sort(key=lambda x: x.start, reverse=False)
  vehicle_index = 0

  while len(rides) > 0:
    ride_index = 0 # randint(0, len(rides) - 1)
    ride = rides.pop(ride_index)
    vehicles[vehicle_index % F].append(ride.index)
    vehicle_index += 1

  vehicles_rides = [ [len(vehicle), *vehicle] for vehicle in vehicles]
  validate(val_rides, vehicles_rides, B, T)

  with open('outputs/' + fname.split('/')[1], 'w') as f:
    for vehicle in vehicles_rides:
      f.write(' '.join([str(ride) for ride in vehicle]) + '\n')
