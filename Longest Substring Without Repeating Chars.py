class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        seen = {}
        
        for end in range(len(s)):
            seen[s[end]] = seen.get(s[end],0) + 1
            while seen[s[end]] > 1:
                seen[s[start]] -= 1
                start += 1
            maxLength = max(maxLength, end - start + 1)
        return maxLength
