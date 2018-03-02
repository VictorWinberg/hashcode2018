from sys import argv
import sys
from random import randint
from util import Ride, validate, Car, dist


def getBestRide(c, rides, T, B):
    index = {}
    for i in range(len(rides)):
        points = 0
        steps = dist(c.pos, rides[i].from_pos)
        if (steps  + c.steps) < rides[i].start:
            steps =  rides[i].start - c.steps
            points = B
        elif (steps  + c.steps) == rides[i].start:
            points = B
        tot_steps = steps  + c.steps + dist(rides[i].from_pos, rides[i].to_pos)
        if tot_steps > T or tot_steps > rides[i].finish:
            continue
        else:
            points +=  dist(rides[i].from_pos, rides[i].to_pos)
            index[i] =  steps # Different values: steps, points, points - steps
    if len(index) == 0:
        return None
    return min(index, key=index.get) #Change this to min or max

def highscore(rides_clone, F, B, T):
    scores = {}
    rides = [ride for ride in rides_clone]
    cars = [Car(0, 0, 0) for i in range(F)]
    for c in cars:
        if len(rides) == 0: break
        while len(rides) > 0 and T - c.steps > 0:
            ride_index = getBestRide(c, rides, T, B)
            if ride_index is None:
                break
            ride = rides.pop(ride_index)
            c.addRide(ride)

    vehicles_rides = [ [len(c.rides), *c.rides] for c in cars]
    score = validate(rides_clone, vehicles_rides, B, T)
    scores[score] = vehicles_rides
    m_score = max(scores, key=float)
    print(m_score)

    return scores[m_score]

if __name__ == "__main__":
    # fname = 'inputs/a_example.in'
    fname = 'inputs/b_should_be_easy.in'

    if len(argv) == 2:
        fname = argv[1]

    with open(fname) as f:
        R, C, F, N, B, T = map(int, f.readline().split(' '))
        content = f.readlines()
        rides = [ Ride(i, *list(map(int, x.strip().split(' ')))) for i, x in enumerate(content)]

    vehicle_rides = highscore(rides, F, B, T)

    with open('outputs1/' + fname.split('/')[1], 'w') as f:
        for vehicle in vehicle_rides:
            f.write(' '.join([str(ride) for ride in vehicle]) + '\n')
