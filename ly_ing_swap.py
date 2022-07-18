def add_string(str1: str):
    length = len(str1)

    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    
    print(str1)


add_string('ab')
add_string('abc')
add_string('abcing')