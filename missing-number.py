class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        missing = n
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
