class Solution:
    def isValid(self, s: str) -> bool:
        pair = { ")":"(","}":"{","]":"["}
        stack = []

        for char in s:
            if char not in pair:
                stack.append(char)
            else:
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
