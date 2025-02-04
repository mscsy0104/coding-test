# nums= [1,2,3,1]
# nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,4]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == len(set(nums)): return False
        else: return True
