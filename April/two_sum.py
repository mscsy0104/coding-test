class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums[:-1]):
            for j, m in enumerate(nums[i + 1:]):
                if target == n + m: return [i, i + j + 1]
