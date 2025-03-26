class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aBin = bin(a)
        bBin = bin(b)
        cBin = bin(c)
        maxi = max(len(aBin), len(bBin), len(cBin))
        aBin = (maxi - len(aBin))*'0' + aBin[2:]
        bBin = (maxi - len(bBin))*'0' + bBin[2:]
        cBin = (maxi - len(cBin))*'0' + cBin[2:]
        counter = 0
        for i in range(maxi - 2):
            if cBin[i] == '0':
                if aBin[i] == '1':
                    counter  += 1
                if bBin[i] == '1':
                    counter += 1
            else:
                if aBin[i] == '0' and bBin[i] == '0':
                    counter += 1
        return counter