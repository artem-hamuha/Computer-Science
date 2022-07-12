def swapPositions(list, pos1, pos2):
    num1 = list[pos1-1]
    num2 = list[pos2-1]

    list[pos1-1] = num2
    list[pos2-1] = num1

    print(list)

swapPositions([23, 65, 19, 90], 1, 3)