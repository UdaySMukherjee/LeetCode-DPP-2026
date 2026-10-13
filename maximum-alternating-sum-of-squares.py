class Solution:
    def maxAlternatingSum(self, a: List[int]) -> int:
        return sum(s:=sorted(v*v for v in a))-2*sum(s[:len(a)//2])
