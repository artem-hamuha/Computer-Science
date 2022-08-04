def remove(words: list[str]):
    w1, w2, w3 = words[0], words[4], words[5]
    words.remove(w1)
    words.remove(w2)
    words.remove(w3)

    print(words)


remove(["black", "yellow", "red", "blue", "white", "cyan"])