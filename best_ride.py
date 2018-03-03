from sys import argv
from util import Ride, Car, validate, dist, read, write

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

def bestRideSolve(rides_clone, F, B, T):
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

    return [ [len(c.rides), *c.rides] for c in cars]

if __name__ == "__main__":
    fname = 'inputs/a_example.in'

    if len(argv) == 2:
        fname = argv[1]

    R, C, F, N, B, T, rides = read(fname)

    vehicle_rides = bestRideSolve(rides, F, B, T)

    score = validate(rides, vehicle_rides, B, T)
    print("{:,}".format(score))

    write('outputs/' + fname.split('/')[1], vehicle_rides)
