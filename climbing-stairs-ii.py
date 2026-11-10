class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        costs = [0] + costs  # step 0 is free, step i costs costs[i]

        @cache
        def climb(i: int = 0) -> int:  # cheapest way from i to n
            if i > n:
                return inf  # jumped past the top
            if i == n:
                return costs[n]  # on top: just pay for it
            return costs[i] + min(climb(i + 1) + 1, climb(i + 2) + 4, climb(i + 3) + 9)

        return climb()
