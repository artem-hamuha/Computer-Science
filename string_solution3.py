class Solution:
    def anagram(s: str, t: str):
        return ''.join(sorted(s)) == ''.join(sorted(t))

print(Solution.anagram('rat', 'car'))
print(Solution.anagram('anagram', 'nagaram'))