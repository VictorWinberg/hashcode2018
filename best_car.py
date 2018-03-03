from sys import argv
from util import Ride, Car, validate, dist, read, write

def getBestCar(ride, cars, T):
    start, end = ride.from_pos, ride.to_pos
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

def moveCar(carIndex, cars, ride):
    steps = dist(ride.from_pos, cars[carIndex].pos) + dist(ride.from_pos, ride.to_pos)
    cars[carIndex].pos = ride.to_pos
    cars[carIndex].steps = steps

def bestCarSolve(rides_clone, F, B, T):
    rides = [ride for ride in rides_clone]
    rides.sort(key=lambda x: x.start)
    vehicles = [[] for i in range(F)]
    cars = [ Car(0, 0, 0) for i in range(F)]

    while len(rides) > 0:
        ride_index = 0
        ride = rides.pop(ride_index)
        closestCar = getBestCar(ride, cars, T)
        moveCar(closestCar, cars, ride)
        vehicles[closestCar].append(ride.index)

    return [ [len(vehicle), *vehicle] for vehicle in vehicles]

if __name__ == "__main__":
    fname = 'inputs/a_example.in'

    if len(argv) == 2:
        fname = argv[1]

    R, C, F, N, B, T, rides = read(fname)

    vehicle_rides = bestCarSolve(rides, F, B, T)
    
    score = validate(rides, vehicle_rides, B, T)
    print("{:,}".format(score))

    write('outputs/' + fname.split('/')[1], vehicle_rides)
