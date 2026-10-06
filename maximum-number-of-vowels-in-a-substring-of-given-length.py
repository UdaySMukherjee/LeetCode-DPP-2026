class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        return max(accumulate(range(len(s)),lambda q,i,w='aeiou':
            q+(s[i] in w)-(i>=k and s[i-k] in w),initial=0))
