def remove_odd(string: str):
    even_str = ''
    for i in string:
        if string.index(i) % 2 == 0:
            even_str += i
    
    print(even_str)

remove_odd('abcdef')
remove_odd('python')