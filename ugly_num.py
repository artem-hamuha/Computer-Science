#ugly number is when its factors are limited to 2,3,5
def ugly_num(num):
    no_nums = [1,2,3,5]
    if num % 2 == 0:
        ans = num / 2

        if ans == 1:
            return True

        if ans % 2 == 0:
            ans = ans / 2
            if ans in no_nums:
                return True
            else:
                return False

        elif ans % 3 == 0:
            ans = ans / 3
            if ans in no_nums:
                return True
            else:
                return False

        elif ans % 5 == 0:        
            ans = ans / 5
            if ans in no_nums:
                return True
            else:
                return False
        
        else:
            return False

    elif num % 3 == 0:
        ans = num / 3
        
        if ans == 1:
            return True

        if ans % 2 == 0:
            ans = ans / 2
            if ans in no_nums:
                return True
            else:
                return False

        elif ans % 3 == 0:
            ans = ans / 3
            if ans in no_nums:
                return True
            else:
                return False

        elif ans % 5 == 0:        
            ans = ans / 5
            if ans in no_nums:
                return True
            else:
                return False
                
        else:
            return False

    elif num % 5 == 0:        
        ans = num / 5
        
        if ans == 1:
            return True

        if ans % 2 == 0:
            ans = ans / 2
            if ans in no_nums:
                return True
            else:
                return False

        elif ans % 3 == 0:
            ans = ans / 3
            if ans in no_nums:
                return True
            else:
                return False

        elif ans % 5 == 0:        
            ans = ans / 5
            if ans in no_nums:
                return True
            else:
                return False
                
        else:
            return False

print(ugly_num(100))