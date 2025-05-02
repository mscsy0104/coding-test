'''
https://www.acmicpc.net/problem/11399
ATM

14:54 ~ 15:03

input
5
3 1 4 3 2

output
32
'''
# sol1. 배열 인덱싱 이용
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

cum = 0
for i in range(n):
    cum += sum(arr[:i+1])

print(cum)

# 누적계 구할 때 풀이 차이
# sol1. 배열 인덱싱 이용
cum = 0
for i in range(n):
    cum += sum(arr[:i+1])

# sol2. 반복된 요소 중복해서 합 처리
'''
핵심 아이디어

1은 5번 사용됨 (1부터 5까지 모두에게 영향)

2는 4번 사용됨 (2~5번에게 영향)

3은 3번 사용됨

3은 2번 사용됨

4는 1번 사용됨
'''
for i in range(n):
    cum += arr[i] * (n - i)


# sol3. 정석 누적합 방식
'''
핵심 아이디어

1번 사람: 1분
2번 사람: 1 + 2 = 3분
3번 사람: 1 + 2 + 3 = 6분
4번 사람: 1 + 2 + 3 + 4 = 9분
5번 사람: 1 + 2 + 3 + 4 + 5 = 13분
'''
arr = sorted(arr)

acc = 0
total = 0

for i in arr:
    cum += i
    total += cum
