class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        path = []
        self.getSubset(all_subsets, path, nums, 0)
        return all_subsets

    def getSubset(self, all_subsets, path, nums, i):
        if i == len(nums):
            all_subsets.append(path[:])
            return
        
        #include the current element
        path.append(nums[i])
        self.getSubset(all_subsets, path, nums, i+1)

        #Omit the current element
        path.pop()
        self.getSubset(all_subsets, path, nums, i+1)
