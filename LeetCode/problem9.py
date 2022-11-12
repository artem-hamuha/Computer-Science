#Isomorphic Strings
class Solution(object):
    def isIsomorphic(self, s: str, t: str):
        s_dup, t_dup = 0, 0
        s_list, t_list = list(s), list(t)
        s_set, t_set = set(s_list), set(t_list)
        
        if s_list != s_set and t_list != t_set:
            for i in s_set:
                if s_list.count(i) == 2:
                    s_dup = s_list.index(i)
            
            for i in t_set:
                if t_list.count(i) == 2:
                    t_dup = t_list.index(i)

            if s_dup == t_dup:
                return True
            
            else:
                return False

        else:
            if s_list == s_set and t_list == t_set:
                return True
            else:
                return False

s = Solution()
print(s.isIsomorphic("egg", "sat"))
print(s.isIsomorphic("dad", "mom"))