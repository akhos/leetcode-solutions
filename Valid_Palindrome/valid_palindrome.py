class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        while i < len(s):
            if not s[i].isalpha() and not s[i].isdigit():
                s = s[:i] + s[i+1:]
            else:
                i = i+1
        return s == s[::-1]