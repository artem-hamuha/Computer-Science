def del_nth(str1: str, i):
    half = str1[:i-1]
    end = str1[i:]

    print(half + end)

del_nth("python", 4)