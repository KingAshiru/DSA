class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, nxt = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[nxt], nums[i] = nums[i], nums[nxt]
                nxt += 1
            i += 1
