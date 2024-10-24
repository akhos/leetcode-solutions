class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        start a counter from 0, and continue comparing str[i] for all s in strs
        when we reach to a character which is not the same as the other ones or 
        '''
        index = -1
        flag = True
        if len(strs) == 0 or strs[0] == "":
            return ""
        while flag:
            index += 1
            if index < len(strs[0]):
                letter = strs[0][index]
            else:
                flag = False
            
            for st in strs:
                if index < len(st) and st[index] != letter: 
                    flag = False
                elif index >= len(st):
                    flag = False
        return strs[0][:index]