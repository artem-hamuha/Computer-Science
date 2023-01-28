#Regular expression matching
class Solution(object):
    def isMatch(self, s: str, p: str):
        final_list = []
        s = list(s)
        p = list(p)
        y = 0

        if len(s) != len(p):
            return False

        for x in s:
            if x == p[y]:
                final_list.append(x)
                y += 1
                continue

            if x != p[y]:
                if p[y] == ".":
                    final_list.append(x)
                    y += 1
                    continue

                if p[y] == "*":
                    final_list.append(x)
                    y += 1
                    continue

                else:
                    return False
            
        return True

ans = Solution()
print(ans.isMatch("ab", ".*"))