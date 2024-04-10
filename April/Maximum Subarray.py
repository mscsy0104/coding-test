# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums= [31,-41,59,26,-53,58,97,-93,-23,84]
nums=[-2,1,-3,4,-1,2,1,-5,4]
# Time Exceed
i_li = []
for i, n in enumerate(nums):
    if n >= 0: i_li.append(i)
#
sum_li = []
# if len(i_li)==0: print(max(nums))
# for i, n in enumerate(i_li):
#     for m in i_li[i:]:
#         sum_li.append(sum(nums[n:m+1]))

for i in i_li:
    sum_li.append(nums[i:])