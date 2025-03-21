'''
https://codeup.kr/problem.php?id=1409
1409 : 기억력 테스트 1

input
10 9 8 7 6 5 4 3 2 1
3
'''

import sys
import time

start1 = time.time()
arr = list(map(int, input().split()))
k = int(input())

print(arr[k-1])

end1 = time.time()



start2= time.time()

arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

print(arr[k-1])

end2 = time.time()

notice = f'''
time1: {end1- start1}
time2: {end2 - start2}
'''
print(notice)