class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n, mod = len(nums), 10**9 + 7
        tree = [0] * (4*n)
        sq = [0] * (4*n)
        lazy = [0] * (4*n)
        last, ans = {}, 0

        def update(v, l, r, a, b):
            if a <= l and r <= b:
                sq[v] += 2*tree[v] + r-l+1
                tree[v] += r-l+1
                lazy[v] += 1
                return
            m = (l+r)//2
            if lazy[v]:
                for c, x, y in ((2*v,l,m),(2*v+1,m+1,r)):
                    sq[c] += 2*lazy[v]*tree[c] + lazy[v]**2*(y-x+1)
                    tree[c] += lazy[v]*(y-x+1)
                    lazy[c] += lazy[v]
                lazy[v] = 0
            if a <= m:
                update(2*v,l,m,a,b)
            if b > m:
                update(2*v+1,m+1,r,a,b)
            tree[v] = tree[2*v] + tree[2*v+1]
            sq[v] = sq[2*v] + sq[2*v+1]

        for i, x in enumerate(nums):
            update(1, 0, n-1, last.get(x, -1)+1, i)
            last[x] = i
            ans = (ans + sq[1]) % mod

        return ans
