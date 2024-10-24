class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        counter = 0
        previousCounter = 0
        for ch in s:
            if ch == ' ':
                counter = 0
            else:
                counter += 1
        return counter