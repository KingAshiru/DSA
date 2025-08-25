class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        if len(tokens) == 1:
            return int(tokens[0])

        for i, token in enumerate(tokens):
            if self.isInteger(token):
                stack.append(token)
            elif len(stack) > 1:
                #print(stack)
                rhs = int(stack.pop())
                lhs = int(stack.pop())
                result = self.performOperation(lhs,rhs,token)
                if i < (len(tokens) - 1):
                    stack.append(result)
        return int(result)
    
    def performOperation(self,left,right,operator):
        if operator == "+":
            return (left + right)
        elif operator == "-":
            return (left - right)
        elif operator == "*":
            return (left * right)
        elif operator == "/":
            return (left / right)

    def isInteger(self, string):
        if string[0] == "-":
            return string[1:].isdigit()
        else:
            return string.isdigit()
