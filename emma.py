from sys import argv
from math import floor, sqrt
from random import randint

class Car:
    def __init__(self, a, b, steps):
        self.pos = a, b
        self.steps = steps
    def __str__(self):
        return self.pos
    def __repr__(self):
        return str(self.pos)

def getClosestCar(start, cars):
    distToStart = dist(start, cars[0].pos)
    carIndex = 0
    for x in range(1, len(cars)):
        distToCar = dist(start, cars[x].pos)
        if(distToStart > distToCar):
            distToStart = distToCar
            carIndex = x
    return carIndex

def getBestCar(start, end, cars, T):
    distToStart = dist(start, cars[0].pos)
    carIndex = 0
    for x in range(1, len(cars)):
        distToCar = dist(start, cars[x].pos)
        if(distToStart > distToCar):
            stepsToTake = distToCar + dist(start, end)
            if((stepsToTake + cars[x].steps) <= T):
                distToStart = distToCar
                carIndex = x
    return carIndex

def AppendRideToCar(indexOnCar, cars, end, steps):
    cars[indexOnCar].pos = end
    cars[indexOnCar].steps = steps

def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

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

if __name__ == "__main__":
    fname = 'inputs/a_example.in'
    # fname = 'inputs/b_should_be_easy.in'

    if len(argv) == 2:
        fname = argv[1]

    with open(fname) as f:
        R, C, F, N, B, T = map(int, f.readline().split(' '))
        content = f.readlines()
        rides = [list(x.strip()) for x in content]

    start, end, e_start, l_finish = fillVectors(content, N)

    rides = list(range(N))
    vehicles = [[] for i in range(F)]
    cars = [ Car(0, 0, 0) for i in range(F)]

    vehicle_index = 0

    while len(rides) > 0:
        ride_index = randint(0, len(rides) - 1)
        ride = rides.pop(ride_index)
        closestCar = getBestCar(getStart(start, ride_index), end[ride_index], cars, T)
        stepsToTake = dist(getStart(start, ride_index), cars[closestCar].pos) + dist(start[ride_index], end[ride_index])
        AppendRideToCar(closestCar, cars, end[ride_index], stepsToTake)
        vehicles[closestCar].append(ride)
        vehicle_index += 1
    print(cars)

    vehicles_rides = [ [len(vehicle), *vehicle] for vehicle in vehicles]

    with open('outputs/solution.txt', 'w') as f:
        for vehicle in vehicles_rides:
          f.write(' '.join([str(ride) for ride in vehicle]) + '\n')
