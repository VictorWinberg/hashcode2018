from sys import argv
from random import randint
from anton import validate

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
    rides_clone = [ride for ride in rides]

  scores = {}
  count = 1000
  
  for i in range(count):
    rides = [ride for ride in rides_clone]
    rides.sort(key=lambda x: x.start, reverse=False)
    vehicles = [[] for i in range(F)]
    vehicle_index = 0

    while len(rides) > 0:
      ride_index = randint(0, len(rides) // 2)
      ride = rides.pop(ride_index)
      vehicles[vehicle_index % F].append(ride.index)
      vehicle_index += 1

    vehicles_rides = [ [len(vehicle), *vehicle] for vehicle in vehicles]
    score = validate(rides_clone, vehicles_rides, B, T)
    scores[score] = vehicles_rides

    if i % (count // 10) == 0: # Just to see progress for big/medium
      print("Progress {}/{}".format(i, count))

  m_score = max(scores, key=float)
  print(m_score)
  m_vehicle_rides = scores[m_score]

  with open('outputs/' + fname.split('/')[1], 'w') as f:
    for vehicle in m_vehicle_rides:
      f.write(' '.join([str(ride) for ride in vehicle]) + '\n')
