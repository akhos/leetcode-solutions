class Solution:
    def convert(self, s: str, numRows: int) -> str:
        words = ["" for _ in range(numRows)]
        index = 0
        if numRows == 1:
            return s
        for ch in s:
            words[index] += ch
            if index == numRows - 1:
                increasing = False
            if index == 0:
                increasing = True
            if increasing:
                index += 1
            else:
                index -= 1
        
        output = ""
        for word in words:
            output += word
        return output