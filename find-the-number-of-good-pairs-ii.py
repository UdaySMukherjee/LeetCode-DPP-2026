class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        nums1 = list(map(lambda x: x//k, filter(lambda x: x%k == 0, nums1)))
        mx1 = max(nums1, default = 0) + 1

        ctr1 = defaultdict(int)
        ctr2 = Counter(nums2)
        
        for n2 in ctr2:
            for i in range(n2, mx1, n2):
                ctr1[i]+= ctr2[n2]

        return sum(map(lambda x: ctr1[x], nums1))
