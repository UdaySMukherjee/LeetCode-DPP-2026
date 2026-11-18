class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    continue
                l = 0
                while i - l - 1 >= 0 and j - l - 1 >= 0 and s[i - l - 1] == t[j - l - 1]:
                    l += 1
                r = 0
                while i + r + 1 < n and j + r + 1 < m and s[i + r + 1] == t[j + r + 1]:
                    r += 1
                cnt += (l + 1) * (r + 1)
        return cnt
