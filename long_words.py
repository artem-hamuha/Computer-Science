def check_words(n: int, words: str):
    words = words.lower()
    w_list = set(words.split(" "))
    big_words = []

    for word in w_list:
        if len(word) > n:
            big_words.append(word)

    if big_words == []:
        print("None are longer than your specified number")
    else: 
        print(big_words)

check_words(5, "The quick brown fox jumps over the lazy dog")