class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def canMakeBouquet(days):
            count = 0
            numOfBouquets = 0

            for day in bloomDay:
                if day <= days:
                    count += 1
                else:
                    count = 0
                if count == k:
                    numOfBouquets += 1
                    count = 0
            return numOfBouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        minDays = -1 

        if m * k > len(bloomDay):
            return -1

        while left <= right:
            days = (left + right) // 2
            if canMakeBouquet(days):
                minDays = days
                right = days - 1
            else:
                left = days + 1
        return minDays
