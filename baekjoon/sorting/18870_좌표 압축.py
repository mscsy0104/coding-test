'''
https://www.acmicpc.net/problem/18870
좌표 압축

input
5
2 4 -10 4 -9

output
2 3 0 3 1
'''



import sys

input = sys.stdin.readline
input()
arr = list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))
hashmap = {val:idx for idx, val in enumerate(sorted_arr)}

print(hashmap)
for i in arr:
    print(hashmap[i], end=' ')