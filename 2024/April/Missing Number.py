class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = range(min(nums), len(nums)+1)
        l = list(r)

        s_n = sum(nums)
        s_l = sum(l)
        if s_n != s_l: return s_l - s_n
        else: return 0 