class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        print(costs)
        costs.sort(key=lambda person: person[1] - person[0])
        print(costs)
        total_cost = 0

        n = len(costs) // 2

        A_idx, B_idx = 0, 1

        for i in range(n):
            total_cost += costs[i][B_idx] + costs[i + n][A_idx]

        return total_cost
