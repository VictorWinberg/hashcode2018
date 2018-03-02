def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

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

def getClosestCar(start, cars):
    distToStart = dist(start, cars[0].pos)
    carIndex = 0
    for x in range(1, len(cars)):
        distToCar = dist(start, cars[x].pos)
        if(distToStart > distToCar):
            distToStart = distToCar
            carIndex = x
    return carIndex

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
