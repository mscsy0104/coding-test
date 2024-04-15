nums = [2,3,-2,4]
import reduce
li = []
for i, n in enumerate(nums):
    if n>0:
        li.append(i)



prod =reduce(lambda x,y:x*y, nums)
if prod>0: print(prod)
elif prod<0:
    for i, n in enumerate(nums):
        right = len(nums) - (i + 1)
        left = len(nums) - right
        if n<0:
            if left > right: print(nums[0])
else:
    nums = [n for n in nums if n>0]



if len(nums) == 1: print(nums[0])
elif len(nums) > 1:
####
'''
1. 다 곱한게 0
1.1 0 다 제거하고 곱한게 >0, 
'''