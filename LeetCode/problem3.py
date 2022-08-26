def rotateArray(array: list[int], k: int):
    for i in range(k % len(array)):
            array.insert(0, array.pop())

    print(array)

rotateArray([1,2,3,4,5,6,7], k = 3)