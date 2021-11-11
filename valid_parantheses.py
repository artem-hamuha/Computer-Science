class Solution:
    def isValid(s: str) -> bool:
        matches = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack = []
        for char in s:
            if char not in matches:
                stack.append(char)
            else:
                if not stack or stack.pop() != matches[char]: return False
        if stack: return False
        return True

print(Solution.isValid('{[]}'))
print(Solution.isValid('(})})'))