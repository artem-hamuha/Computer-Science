#reversing integer but if its outside 32 bit range , [-2^31, 2^31 - 1], return 0
def rev_int(num):
    min = -2**31
    max = 2**31 - 1
    if num < 0:
        num *= -1
        remember = True

    num2 = str(num)
    num2 = [i for i in num2]
    num2.reverse()
    num = ""

    for i in num2:
        num += i
    
    num = int(num)

    if remember:
        num *= -1
        if num < min or num > max:
            return 0
        
        else:
            return num
    
    else:
        if num < min or num > max:
            return 0
        
        else:
            return num

print(rev_int(-321))