class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        keep = set(nums)

        for num in nums:
            if num - 1 not in keep:
                cur_streak = 1 
                cur_num = num
                while cur_num + 1 in keep:
                    cur_streak += 1
                    cur_num += 1
                longest_streak = max(longest_streak, cur_streak)

        return longest_streak
