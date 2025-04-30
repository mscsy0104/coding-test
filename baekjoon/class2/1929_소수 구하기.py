'''
https://www.acmicpc.net/problem/1929
소수 구하기

17:56 ~ (X, 해설)

input
3 16

output
3
5
7
11
13
'''
# sol1. 소수 구하기 함수 이용
import sys
import math

input = sys.stdin.readline

def is_premium(x):
    if x == 1:
        return False
    
    for div in range(2, int(math.sqrt(x)) + 1):
        if x % div == 0:
            return False
        
    return True

m, n = map(int, input().split())

for i in range(m, n + 1):
    if is_premium(i):
        print(i)


# sol2. 에라토스테네스의 체 방법
# 범위의 가장 작은 수의 배수는 전부 지워나간다. 이 때 1은 합성수도 소수도 아니니 미리 제거한다.
m, n = map(int, input().split())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False


for i in range(2, int(n**0.5) + 1):
    if is_prime(i):
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

# n이 16일 때 2부터 5까지 range => (2, 3, 4)
# 2일 때, 4부터 17까지 2계단씩 2의 배수 전멸 
# 3일 때, 9부터 17까지 3계단씩 3의 배수 전멸
# 4일 때, 건너뜀.

# i * i 하는 이유
# 전 단계에서 지워지기 때문이다.
# 어떤 수 k = i * m(i의 배수)
# 만약, m < i 이라면 k는 이미 m 단계에서 지워진다.
# m >= i 일 때부터 지우면 중복 안 되게 지울 수 있다.

for i in range(m, n + 1):
    if is_prime[i]:
        print(i)