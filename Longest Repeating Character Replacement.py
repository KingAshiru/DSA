class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        max_freq = 0
        max_length = 0
        start = 0

        for end in range(len(s)):
            seen[s[end]] = seen.get(s[end],0) + 1
            max_freq = max(max_freq, seen[s[end]])

            if k + max_freq < end - start + 1:
                seen[s[start]] -= 1
                start += 1
            
            max_length = max(max_length, end - start + 1)
        return max_length
