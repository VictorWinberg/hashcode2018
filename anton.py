from sys import argv
from math import floor, sqrt
from random import randint



def dist(start, end):
    return abs(start[0] - end[0] + start[1] - end[1])

def validate(rides, vehicles_rides, B, T):
    score = 0
    for vehicle in vehicles_rides:
        vehicle_start = (0, 0)
        temp = T
        for v in vehicle[1:]:
            r_start = (rides[v][0], rides[v][1])
            v_dist = dist(vehicle_start, r_start)
            temp -= v_dist
            if temp <= rides[v][4]:
                score += B
            r_end = (rides[v][2], rides[v][3])
            score += dist(r_start, r_end)
            vehicle_start = r_end
            # if vehicle_start[0] == rides[v][0] and vehicle_start[1] == rides[v][1]:
            # vehicle_start[0] = rides[v][2]
            # vehicle_start[1] = rides[v][3]

    print(score)
if __name__ == '__main__':
 fname = 'inputs/a_example.in'

 if len(argv) == 2:
   fname = argv[1]

 with open(fname) as f:
   R, C, F, N, B, T = map(int, f.readline().split(' '))
   content = f.readlines()

   rides1 = [list(map(int, x.strip().replace(" ", ""))) for x in content]
   print(rides1)
 rides = list(range(N))
 vehicles = [[] for i in range(F)]
 vehicle_index = 0

 while len(rides) > 0:
   ride_index = randint(0, len(rides) - 1)
   ride = rides.pop(ride_index)
   vehicles[vehicle_index % F].append(ride)
   vehicle_index += 1

 vehicles_rides = [ [len(vehicle), *vehicle] for vehicle in vehicles]
 validate(rides1, vehicles_rides, B, T)
 with open('outputs/solution.txt', 'w') as f:
   for vehicle in vehicles_rides:
     f.write(' '.join([str(ride) for ride in vehicle]) + '\n')
