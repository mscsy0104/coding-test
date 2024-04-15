# from itertools import combinations as combi
from random import sample
nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]
l_li = []
r_li = []
z_li = []
li = []
for n in nums:
    if n<0:
        l_li.append(n)
    elif n>0:
        r_li.append(n)
    else: z_li.append(n)
if len(l_li)==0 or len(r_li)==0: print([])
breaker= 0
for l in l_li:
    for r in r_li:
        if abs(l) == abs(r):
            li.append(l)
            li.append(r)
            breaker = 1
            break
        else:

    if breaker ==1: break

# TimeoutExceed
# from itertools import combinations as combi
#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#
#         li=[]
#         c_li = list(combi(nums,3))
#         for c in c_li:
#             if sum(c) == 0:
#                 c = list(c)
#                 c.sort()
#                 li.append(c)
#         li = [tuple(l) for l in li]
#         li = list(set(li))
#         li = [list(l) for l in li]
#         return li
#

