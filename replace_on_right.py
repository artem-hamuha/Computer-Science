#Given an array arr, replace every element in that array with the greatest element
#among the elements to its right, and replace the last element with -1.
def replace_on_right(arr: list[int]):
    final_arr = []
    on = True
    while on:
        arr.remove(arr[0])

        if len(arr) == 0:
            final_arr.append(-1)
            on = False
            return final_arr

        else:
            final_arr.insert(len(final_arr), max(arr))
    
    

print(replace_on_right([17,18,5,4,6,1]))