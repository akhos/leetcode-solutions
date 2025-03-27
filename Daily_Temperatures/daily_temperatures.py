from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        starting from the end of the temperatures list, insert the first item 
        in the stack, when encountering a new number temperature[i], pop the elements from the stack, 
        until reaching an element which is larger than temperature[i]. Then we find the answer[i] through
        the difference of i and index of this element. We push temperature[i] to the stack and continue
        with temperature[i-1]
        '''
        indexStack = deque()
        numStack = deque()
        if not temperatures:
            return []
        indexStack.append(len(temperatures) - 1)
        numStack.append(temperatures[-1])
        answers = [0]
        for i in range(len(temperatures) - 2, -1, -1):
            while numStack and numStack[-1] <= temperatures[i]:
                numStack.pop()
                indexStack.pop()
            
            if numStack:
                answers.append(indexStack[-1] - i)
            else:
                answers.append(0)
            numStack.append(temperatures[i])
            indexStack.append(i)
        return answers[::-1]
