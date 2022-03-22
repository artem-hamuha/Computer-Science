#get 2 heaviest stones and smash together
#x <= y
#if x == y they both get smashed
#if x != y, x is totaly destroyed and y stone = y-x
#do for all stones

def last_stone_weight(stones: list[int]):
    while len(stones) > 1:
        max_y = max(stones)
        stones.remove(max_y)
        max_x = max(stones)
        if max_x == max_y:
            stones.remove(max_x)
        
        else:
            max_y = max_y - max_x
            stones.remove(max_x)
            stones.append(max_y)
    
    return stones[0]

print(last_stone_weight([2,7,4,1,8,1]))
