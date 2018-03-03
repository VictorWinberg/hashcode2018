from sys import argv
from random import randint
from util import Ride, validate, read, write

def sortSolve(rides_clone, F, B, T):
    rides = [ride for ride in rides_clone]
    rides.sort(key=lambda x: x.start)
    vehicles = [[] for i in range(F)]
    vehicle_index = 0

    while len(rides) > 0:
        ride_index = 0
        ride = rides.pop(ride_index)
        vehicles[vehicle_index % F].append(ride.index)
        vehicle_index += 1

    return [ [len(vehicle), *vehicle] for vehicle in vehicles]

if __name__ == "__main__":
    fname = 'inputs/a_example.in'

    if len(argv) == 2:
        fname = argv[1]

    R, C, F, N, B, T, rides = read(fname)

    vehicle_rides = sortSolve(rides, F, B, T)

    score = validate(rides, vehicle_rides, B, T)
    print(score)

    write('outputs/' + fname.split('/')[1], vehicle_rides)
