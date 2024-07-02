# import sys
# from itertools import combinations as combi
# n = int(input())
# grades = [int(sys.stdin.readline().strip()) for _ in range(n)]
# print(f'grades:{grades}')
#
# k = 0
# combi_li = []
# sum_li = []
# if n == 1:
#     result = grades[0]
# elif n == 2:
#     result = sum(grades)
# elif n == 3:
#     if grades[0] + grades[2] > grades[1] + grades[2]:
#         result = grades[0] + grades[2]
#     else:
#         result = grades[1] + grades[2]
# else:
#     if grades[n-1] > grades[n-2]:
#         k = n-1
#     else:
#         k = n-2
#     combi_li = list(combi(grades[:k], k-2))
#     for c in combi_li:
#         print(f'c:{c}')
#         sum_li.append(c)
#     sum_li = [sum(i) for i in sum_li]
#     result = max(sum_li)
#     print(result)


import sys
n = int(input())
stairs = [int(sys.stdin.readline().strip()) for _ in range(n)]

def step(n, stairs):
    if n <= 0:
        pass
    elif