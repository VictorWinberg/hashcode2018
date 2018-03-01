
def dist(start, end):
    return abs(start[0] - end[0] + start[1] - end[1])


if __name__ == '__main__':
    M = [[0 for x in range(5)] for y in range(5)]
    print(M)
    print(dist((0, 1), (4, 1)))
