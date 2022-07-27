def sentance_count(string: str):
    words = string.split(" ")
    count = dict()


    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    print(count)

sentance_count("the quick brown fox jumps over the lazy dog")
