def check_list(l1: list[int], l2: list[int]):
    set1 = l1 + l2
    set2 = set(set1)

    if set1 == set2:
        print(False)

    else:
        print(True)

check_list([1,2,3,4,5], [5,6,7,8,9])