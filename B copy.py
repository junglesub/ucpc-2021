# Data Type
def findlogic(x, to, k, down):
    pathval = x[0].findPath(to, k)
    if pathval == -1:
        return -1
    if down:
        return pathval + x[1]
    else:
        return pathval


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

    def findPath(self, to, K) -> int:
        # print("Hit", self.no)
        # self.options()
        upMax = downMax = -1

        if K > 0 and len(self.up) > 0:
            upMax = max(map(lambda up: findlogic(up, to, K-1, False), self.up))

        if(len(self.down) > 0):
            downMax = max(
                map(lambda down: findlogic(down, to, K, True), self.down))

        if to == self.no:
            return 0

        # print(self.no, upMax, downMax)

        return max(upMax, downMax)


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
