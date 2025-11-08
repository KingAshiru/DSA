class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        print(stack[-1])

        for char in s[1:]:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
