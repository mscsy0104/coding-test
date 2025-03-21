'''
https://codeup.kr/problem.php?id=1094
1094 : [기초-1차원배열] 이상한 출석 번호 부르기2

input
10
10 4 2 3 6 6 7 9 8 5

output
5 8 9 7 6 6 3 2 4 10

'''

import time

start1 = time.time()
n = int(input())
nums = input().split()

nums.reverse()
print(' '.join(nums))
end1 = time.time()


start2 = time.time()
n = int(input())
nums = input().split()

print(' '.join(list(reversed(nums))))

end2 = time.time()

notice = f'''
time1: {end1 - start1}
time2: {end2 - start2}
'''
print(notice)

'''
time1: 6.952122926712036
time2: 1.9921348094940186
'''