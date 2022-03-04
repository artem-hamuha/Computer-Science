#your can jump 1 or 2 times each turn
def climb_stairs(stairs):
    answ = [0 for i in range(stairs +1)]
    answ[-1], answ[-2] = 1, 1
    count = -3
    on = True
    while on:
        last_total = answ[count+2] + answ[count+1]
        answ[count] = last_total
        count -= 1
        if count == stairs * -1 -2:
            on = False
        
    return answ[0]

print(climb_stairs(5))

