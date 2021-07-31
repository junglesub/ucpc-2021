# Data Type
def findlogic(x, to, k, down):
    pathval = x[0].findPath(to, k)
    pathval[1].append(x[0].no)
    if pathval[0] == -1:
        return (-1, pathval[1])
    if down:
        # print(">>>>", pathval, x[1])
        return (pathval[0] + x[1], pathval[1])
    else:
        return (pathval[0], pathval[1])


class MidPoint:
    no = 0
    up = []
    down = []

    def __init__(self, no):
        self.no = no
        self.up = []
        self.down = []

    def options(self):
        print(f"---- {self.no} ----")
        print("Down:", tuple(map(lambda x: (x[0].no, x[1]), self.down)))
        print("Up:", tuple(map(lambda x: (x[0].no, x[1]), self.up)))
        print(f"-------------------")

    def findPath(self, to, K):
        # print("Hit", self.no, K)
        # self.options()
        upMax = downMax = (-1, [])

        if K > 0 and len(self.up) > 0:
            upMax = max(map(lambda up: findlogic(
                up, to, K-1, False), self.up), key=lambda x: x[0])

        if to == self.no:
            return (0, [])

        if(len(self.down) > 0):
            downMax = max(
                map(lambda down: findlogic(down, to, K, True), self.down), key=lambda x: x[0])

        print(self.no, K, upMax, downMax)
        # print("LOOK HERRE:", max((upMax, downMax), key=lambda x: x[0]))
        # return (0, [])
        return max((upMax, downMax), key=lambda x: x[0])


N, M, K, S, T = map(int, input().split())

midpoints = []
for i in range(N):
    midpoints.append(MidPoint(i + 1))

course = []

for _ in range(M):
    temp = list(map(int, input().split()))
    a, b, t = temp
    midpoints[a-1].down.append((midpoints[b-1], t))
    midpoints[b-1].up.append((midpoints[a-1], t))

currentLoc = midpoints[S - 1]

# currentLoc.options()

print(currentLoc.findPath(T, K))


# Process
