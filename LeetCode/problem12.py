#Longest substring wo/repeating chars
def lenOfLongestSubstring(s: str):
    d={}
    res = 0
    k=0

    for i in s:
        if i not in d:
            d[i]=1
            res = len(d)
            k = max(k, res)

        else:
            while i in d.keys():
                val = next(iter(d))
                del d[val]
            d[i]=1
            
    return k

print(lenOfLongestSubstring("pwwkew"))