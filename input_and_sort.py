#Write a Python program that accepts a comma separated sequence of words
#as input and prints the unique words in sorted form (alphanumerically).
def sort(string: str):
    words = string.split(", ")

    print(sorted(words))

sort("yellow, black, 0, green, white, purple, 200")