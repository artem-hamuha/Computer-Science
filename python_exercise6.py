class Solution:
    def longestCommonPrefix(strs: list[str]):
        if not strs:
            return ""
        
        strs.sort(key= lambda x: len(x))
        prefix = strs[0]
        while prefix:
            total = sum(prefix in s[:len(prefix)] for s in strs)
            if total == len(strs):
                break
            else:
                prefix = prefix[:len(prefix) - 1]

        return prefix

print(Solution.longestCommonPrefix(["read", "reach"]))