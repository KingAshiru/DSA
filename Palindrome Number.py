class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        

        old_x = x
        reversed_x = 0
        while x > 0:
            rem = x % 10
            x = x // 10 # This line optimize our algo from O(N) to O(log N) time. The log is to base 10 though.
            reversed_x = reversed_x * 10 + rem 

        return old_x == reversed_x
