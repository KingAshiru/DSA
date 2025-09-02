class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = sum(weights)

        def canShip(cap):
            ship, currCap = 1, cap
            for weight in weights:
                if currCap - weight < 0:
                    ship += 1
                    currCap = cap
                currCap -= weight
            return ship <= days

        while left <= right:
            cap = (left + right) // 2
            if canShip(cap):
                result = min(result, cap)
                right = cap - 1
            else:
                left = cap + 1
        
        return result
