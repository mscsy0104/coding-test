'''
https://softeer.ai/practice/6284
바이러스

13:04 ~ X(해설)

input 
2 3 2

output
18
'''
# k * p ** n / 1000000007

# 시간 초과
import sys

input = sys.stdin.readline

k, p, n = map(int, input().split())

result = k * p ** n % 1000000007

print(result)


# sol. 내장함수 pow 사용
'''
pow O(logn), 일반곱 O(n)
입력값 범위가 크기 때문에 pow 사용.

제약조건
1 <= k <= 10^8
1 <= p <= 10^8
1 <= n <= 10^6
'''
import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

MOD = 1000000007
result = (k * pow(p, n, MOD)) % MOD
print(result)