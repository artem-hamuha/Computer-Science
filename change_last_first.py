def change(string: str):
    string = string[-1] + string[1:len(string)-1] + string[0]

    print(string)

change("abcd")
