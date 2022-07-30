#Write a Python program to count the number of strings
#where the string length is 2 or more and the first and last character are same from a given list of strings.
def string_count(words: list[str]):
    count = 0

    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
    
    print(count)

string_count(['abc', 'xyz', 'aba', '1221'])