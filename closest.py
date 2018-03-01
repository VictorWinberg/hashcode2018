from sys import argv
from random import randint
from util import Ride, Car, validate, moveCar, getBestCar

def highscore(rides_clone, F, B, T):
  scores = {}
  count = 10
  
  for i in range(count):
    rides = [ride for ride in rides_clone]
    vehicles = [[] for i in range(F)]
    cars = [ Car(0, 0, 0) for i in range(F)]

    while len(rides) > 0:
      ride_index = randint(0, len(rides) - 1)
      ride = rides.pop(ride_index)
      closestCar = getBestCar(ride, cars, T)
      moveCar(closestCar, cars, ride)
      vehicles[closestCar].append(ride.index)

    vehicles_rides = [ [len(vehicle), *vehicle] for vehicle in vehicles]
    score = validate(rides_clone, vehicles_rides, B, T)
    scores[score] = vehicles_rides

    if i % (count // 10) == 0: # Just to see progress for big/medium
      print("Progress {}/{}".format(i, count))

  m_score = max(scores, key=float)
  print(m_score)

  return scores[m_score]

if __name__ == "__main__":
  fname = 'inputs/a_example.in'

  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, F, N, B, T = map(int, f.readline().split(' '))
    content = f.readlines()
    rides = [ Ride(i, *list(map(int, x.strip().split(' ')))) for i, x in enumerate(content)]

  vehicle_rides = highscore(rides, F, B, T)

  with open('outputs/' + fname.split('/')[1], 'w') as f:
    for vehicle in vehicle_rides:
      f.write(' '.join([str(ride) for ride in vehicle]) + '\n')
