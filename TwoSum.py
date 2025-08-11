class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            if (target - nums[i] ) in compliments:
                compliment_index = compliments[target-nums[i]]
                return [ compliment_index, i]
            compliments[nums[i]] = i
