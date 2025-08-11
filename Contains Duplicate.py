class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num in counter:
                return True
            counter[num] = 1
        return False
