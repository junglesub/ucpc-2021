import random
from subprocess import Popen, PIPE, STDOUT, run


def buildTC():
    A = random.randint(1, 999)
    B = random.randint(A, 999)

    tc = ""
    for i in range(A, B + 1):
        tc += str(i)

    print(f"A={A} B={B}")
    # print(tc)
    return A, B, tc


tested = set()
alreadyTested = 0
i = 0
while alreadyTested < 10:
    A, B, tc = buildTC()

    if tuple((A, B)) in tested:
        alreadyTested += 1
        continue

    alreadyTested = 0

    pmy = run(['python3', 'A.py'], stdout=PIPE,
              input=f'{tc}\n', encoding='ascii')
    my = tuple(map(int, pmy.stdout.strip().split()))

    print(f"TC #{i} : a={A} b={B}")
    print("MY:", my)
    print("Match:", (A, B) == my)
    print()
    # break
    if (A, B) != my:
        break
