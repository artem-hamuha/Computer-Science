def len_of_last_word(s: str):
    sl = s.split()
    return len(sl[len(sl)-1])

print(len_of_last_word("   fly me   to   the  moon  "))