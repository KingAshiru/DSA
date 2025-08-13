class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        freq_map = {}
        max_freq = 0
        for num, freq in count.items():
            if freq in freq_map:
                freq_map[freq].append(num)
            else:
                freq_map[freq] = [num]
            max_freq = max(freq, max_freq)
        
        output = []
        for freq in range(max_freq, -1, -1):
            if freq in freq_map:
                output += freq_map[freq]
            if len(output) >= k:
                return output
        
        return output
