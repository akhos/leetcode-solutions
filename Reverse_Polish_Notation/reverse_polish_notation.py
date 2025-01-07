from collections import deque
import math
import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''
        start checking the tokens from the beginning of the tokens list,
        when we encounter an operand, push it into the stack, when we encounter an 
        operation, we pop two numbers from the stack, apply the operation on them and push
        the result into the stack, when we reach to the end of the tokens list, the final result
        is on top of the stack
        '''
        polishStack = deque()
        for elem in tokens:
            if elem in ['+', '-', '*', '/']:
                num1 = polishStack.pop()
                num2 = polishStack.pop()
                match elem:
                    case '+':
                        polishStack.append(num1 + num2)
                    case '*':
                        polishStack.append(num1 * num2)
                    case '-':
                        polishStack.append(num2 - num1)
                    case '/':
                        polishStack.append(math.trunc(num2 / num1))
            else:
                polishStack.append(int(elem))
        return polishStack.pop()
