from typing import List

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        cnt = {}

        for r, c in coordinates:
            if r > 0 and c > 0:
                key = (r - 1) * n + (c - 1)
                cnt[key] = cnt.get(key, 0) + 1

            if r > 0 and c < n - 1:
                key = (r - 1) * n + c
                cnt[key] = cnt.get(key, 0) + 1

            if r < m - 1 and c > 0:
                key = r * n + (c - 1)
                cnt[key] = cnt.get(key, 0) + 1

            if r < m - 1 and c < n - 1:
                key = r * n + c
                cnt[key] = cnt.get(key, 0) + 1

        ans = [0] * 5
        for v in cnt.values():
            ans[v] += 1

        total_blocks = (m - 1) * (n - 1)
        ans[0] = total_blocks - sum(ans[1:])

        return ans
