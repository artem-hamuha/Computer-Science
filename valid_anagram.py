word1 = "interpersonal"
word2 = "niretpernaso"

def valid_anagram(word1, word2):
    if word1 == word2:
        print(True)
    elif len(word1) == len(word2):
        word1 = list(word1)
        word2 = list(word2)
        word1.sort()
        word2.sort()
        if word1 == word2:
            print(True)
    else:
        print(False)

valid_anagram(word1, word2)