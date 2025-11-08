class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k =  k % len(nums)
        #Full array reverse
        
        self.swapElements(nums, 0, len(nums)-1)
        self.swapElements(nums, 0, k-1)
        self.swapElements(nums, k, len(nums)-1)

    def swapElements(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
    
