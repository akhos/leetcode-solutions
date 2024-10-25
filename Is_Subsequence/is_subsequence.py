class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1 = 0
        if s == "":
            return True
        for ch in t:
            if ch == s[ptr1]:
                ptr1 += 1
                if ptr1 == len(s):
                    return True
        return False