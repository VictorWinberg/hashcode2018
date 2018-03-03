from sys import argv
from random import randint
from util import Ride, validate, read, write

def randomSolve(rides_clone, F, B, T):
    scores = {}
    count = 100

    for i in range(count):
        rides = [ride for ride in rides_clone]
        vehicles = [[] for i in range(F)]
        vehicle_index = 0

        while len(rides) > 0:
            ride_index = randint(0, len(rides) - 1)
            ride = rides.pop(ride_index)
            vehicles[vehicle_index % F].append(ride.index)
            vehicle_index += 1

        vehicles_rides = [ [len(vehicle), *vehicle] for vehicle in vehicles]
        score = validate(rides_clone, vehicles_rides, B, T)
        scores[score] = vehicles_rides
    
    m_score = max(scores, key=float)

    if i % (count // 10) == 0:
        print("Progress {}/{}".format(i, count))

    return scores[m_score]

if __name__ == "__main__":
    fname = 'inputs/a_example.in'

    if len(argv) == 2:
        fname = argv[1]

    R, C, F, N, B, T, rides = read(fname)

    vehicle_rides = randomSolve(rides, F, B, T)

    score = validate(rides, vehicle_rides, B, T)
    print(score)

    write('outputs/' + fname.split('/')[1], vehicle_rides)
