import sys

class Ride:
    def __init__(self, index, a, b, x, y, s, f):
        self.index = index
        self.from_pos = (a, b)
        self.to_pos = (x, y)
        self.start = s
        self.finish = f

class Car:
    def __init__(self, a, b, steps):
        self.pos = a, b
        self.steps = steps
        self.rides = []

    def __str__(self):
        return self.rides

    def __repr__(self):
        return str(self.rides)

    def addRide(self, ride):
        self.rides.append(ride.index)
        self.steps += dist(self.pos, ride.from_pos)
        if self.steps < ride.start:
            self.steps = ride.start
        self.steps += dist(ride.from_pos, ride.to_pos )
        self.pos = ride.to_pos

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

    return score

def read(fname):
    with open(fname) as f:
        R, C, F, N, B, T = map(int, f.readline().split(' '))
        content = f.readlines()
        rides = [ Ride(i, *list(map(int, x.strip().split(' ')))) for i, x in enumerate(content)]
    
    return R, C, F, N, B, T, rides

def write(fname, vehicle_rides):
    with open(fname, 'w') as f:
        for vehicle in vehicle_rides:
            f.write(' '.join([str(ride) for ride in vehicle]) + '\n')

def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])
    
def progressBar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rProgress: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    if value == endvalue:
        sys.stdout.write("\n")
    sys.stdout.flush()
