from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathStack = deque()
        phrase = ''
        for i in range(len(path)):
            if path[i] != '/':
                phrase += path[i]
            if path[i] == '/' or i == len(path) - 1:
                if phrase:
                    if phrase == '..':
                        if pathStack:
                            pathStack.pop()
                    elif phrase != '.':
                        pathStack.append(phrase)
                    phrase = ''
        
        output = ''
        while pathStack:
            elem = pathStack.pop()
            output = elem + '/' + output
        return('/' + output[:-1])