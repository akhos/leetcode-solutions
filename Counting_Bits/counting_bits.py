class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            b = bin(i)
            counter = 0
            for i in range(2, len(b)):
                if b[i] == '1':
                    counter += 1
            output.append(counter)
        return output 