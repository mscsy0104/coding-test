'''
https://www.acmicpc.net/problem/1436
영화감독 숌 

input
187

output
66666
'''




# sol1.
def test():
    n = int(input())

    nums = []

    for i in range(666, 3000000):
        if '666' in str(i):
            nums.append(i)

    print(nums[n-1])

# sol2. 메모리 절약 - 불필요한 리스트 제거
n = int(input())
count = 0
num = 666

while 1:
    if '666' in str(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1
