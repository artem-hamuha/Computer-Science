import collections
class Solution:
    def firstNonRepeating(s: str):
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

print(Solution.firstNoneRepeating('loveleetcode'))

