class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = {}
        for i in range(len(nums)):
            if nums[i] in counter:
                if abs(counter[nums[i]] - i) <= k:
                    return True
            counter[nums[i]] = i
        return False
