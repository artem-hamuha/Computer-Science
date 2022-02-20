word1 = "interpersonal"
word2 = "niretpernaso"
import datetime
start_time = datetime.datetime.now()

def valid_anagram(word1, word2):
    if word1 == word2:
        return True
    elif len(word1) == len(word2):
        word1 = list(word1)
        word2 = list(word2)
        word1.sort()
        word2.sort()
        if word1 == word2:
            return True
    else:
        return False

valid_anagram(word1, word2)

end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()

#solution 2
def valid_anagram(word1, word2):
    return sorted(word1) == sorted(word2)