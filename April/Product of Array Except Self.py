from functools import reduce
import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li=[]
        if 0 in nums:
            for i in nums:
                temp=copy.copy(nums)
                if i != 0:
                    li.append(0)
                else:
                    temp.remove(i)
                    li.append(reduce(lambda x, y: x * y, temp))
        else:
            m = reduce(lambda x, y: x * y, nums)
            for i in nums:
                li.append(m // i)

        return li