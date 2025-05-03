'''

16:22 ~ 16:30
16:51 ~ 17:04

# input
2
6
22

# output
5 8
10946 17711
'''

# 재귀함수 사용 - 시간 초과
import sys

input = sys.stdin.readline

t = int(input())

zero_cnt = one_cnt = 0

def fibonacci(n, zero_cnt, one_cnt):
    if n == 0:
        zero_cnt += 1
        return 0, zero_cnt, one_cnt
    elif n == 1:
        one_cnt += 1
        return 1, zero_cnt, one_cnt
    else:
        result = fibonacci(n - 1, zero_cnt, one_cnt)[0] + fibonacci(n - 2, zero_cnt, one_cnt)[0]
        zero_cnt += fibonacci(n - 1, zero_cnt, one_cnt)[1] + fibonacci(n - 2, zero_cnt, one_cnt)[1]
        one_cnt += fibonacci(n - 1, zero_cnt, one_cnt)[2] + fibonacci(n - 2, zero_cnt, one_cnt)[2]
        return result, zero_cnt, one_cnt
    

for _ in range(t):
    n = int(input())
    print(*fibonacci(n, zero_cnt, one_cnt)[1:])


# sol1. DP 이용
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0:
        print(1, 0)
    else:
        m = [0] * (n + 1)
        m[1] = 1
        for i in range(2, n + 1):
            m[i] = m[i - 1] + m[i - 2]

        print(*m[-2:])


# sol2. 백준 mercury0502 님 풀이
# 횟수만을 계산해서 메모리도 낭비하지 않고 아주 깔끔하다..!
# 근데 이해하기에 다소 난해
for i in range(t):
    n = int(input())
    
    zero, one = 1, 0
    
    for _ in range(n):
        zero, one= one, one+zero

    print(zero, one)