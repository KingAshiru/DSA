class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
		
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            freq[s_char] = freq.get(s_char, 0) + 1
            freq[t_char] = freq.get(t_char, 0) - 1

        for char in freq:
            if freq[char] != 0:
                return False
        return True
