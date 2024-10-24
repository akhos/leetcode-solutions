class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        remove starting and ending spaces of the string, split the string to words, put words in a list
        print the words of the list starting from the end of the list with one space between
        '''
        s = s.rstrip()
        s = s.lstrip()
        words = []
        startIndex = 0
        endIndex = 0
        while endIndex < len(s):
            if s[endIndex] == " ":
                if endIndex > startIndex and s[startIndex:endIndex] != " ":
                    word = s[startIndex:endIndex]
                    words.append(word)
                startIndex = endIndex + 1
            endIndex += 1
        words.append(s[startIndex:endIndex])
        print(words)
        stringInReverse = ""
        for i in range(len(words) - 1, -1 , -1):
            stringInReverse += words[i]
            if i != 0:
                stringInReverse += " "
        return stringInReverse
