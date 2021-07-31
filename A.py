DEBUG = False


def ans():
    # 입력
    inp = input()

    before = inp[0]
    initNumDigit = numdigit = 1
    index = 1

    if before == "9":
        numdigit += 1

    while True:
        if index >= len(inp):
            break
        DEBUG and print(">", inp[index:index+numdigit])
        currentNo = int(inp[index:index+numdigit])
        DEBUG and print("CN", currentNo)
        if int(before) + 1 != currentNo:
            DEBUG and print("NM:", before, currentNo)
            # Failed back to start
            index = numdigit = initNumDigit = initNumDigit + 1
            before = inp[0:numdigit]

            if str(before) == '9' * numdigit:
                numdigit += 1

            DEBUG and print("NINDEX", index, before)
            continue
        before = currentNo
        index += numdigit
        if str(before) == '9' * numdigit:
            numdigit += 1
    print(inp[0:initNumDigit], before)


# Run answer
ans()
