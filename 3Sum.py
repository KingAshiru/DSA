class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums, idx, result):
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            if nums[idx] + nums[left] + nums[right] < 0:
                left += 1
            elif nums[idx] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                result.append([nums[idx], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
