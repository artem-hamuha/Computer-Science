#get a string from a given string where all occurrences of its first char have been changed to '$'
#except the first char itself
def first_char(string: str):
    f_char = string[0]
    string = string[1:]
    string = string.replace(f_char, '$')
    string = f_char + string

    print(string)

first_char("return")