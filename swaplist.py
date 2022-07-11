def swapList(newList: list):
    l = len(newList) - 1

    first = newList[0]
    last = newList[l]

    newList[0] = last
    newList[l] = first

    print(newList)

swapList([162, 35, 9, 56, 24])