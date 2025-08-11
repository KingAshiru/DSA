class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_1 = {}
        counter_2 = {}
        for char in s:
            counter_1[char] = counter_1.get(char,0) + 1

        for char in t:
            counter_2[char] = counter_2.get(char,0) + 1
        
        print(counter_1)
        print(counter_2)
        return counter_1 == counter_2
        
