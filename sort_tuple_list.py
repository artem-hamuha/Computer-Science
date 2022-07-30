#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def last(tuple):
    return tuple[-1]
def sort_tuple_list(Tlist: list[tuple]):
    print(sorted(Tlist, key=last))

sort_tuple_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
            