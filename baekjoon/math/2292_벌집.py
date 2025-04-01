'''
https://www.acmicpc.net/problem/2292
벌집

18:26 ~ 18:49

input(입력 제약조건: 1 ≤ N ≤ 1,000,000,000))
13

output
3
'''

'''
지나는 문 개수 + 1(= 지나는 방 개수)
1 차이 2 ~ 7 (6개)
2 차이 8 ~ 19(12개)
3 차이 20 ~ 37(18개)
4 차이 38 ~ 61(24개)
t 차이 (t * 6개)
'''

# sol1. 선형 탐색 - 시간복잡도 O(sqrt(n))
n = int(input())

cnt = 1
q = 1

while n > 1:
    cnt += 1
    n -= 6 * q
    q += 1
    
print(cnt)


# sol2. 백준 imjaegon 님 풀이 
# 이진 탐색을 통해 구하기 - 우선 점화식을 먼저 떠올려야 함. 시간복잡도: O(logn)
'''
expr(t) = 1 + 6 * (1 + 2 + 3 + ... + t)
6 * (1 + 2 + 3 + ...)는 6이 곱해진 등차수열의 합
expr(t) = 1 + 6 * t * (t + 1)/2 = 3 * t * (t + 1)
'''
def expr(n):
    return 3 * n * (n + 1)

def binary_search(n):
    result = 0
    l, r = 0, 100000 # 입력 제약조건 참고

    while l <= r:
        m = (l + r) >> 1 # (l + r) >> 1 == (l + r) // 2

        if expr(m) >= n:
            result = m
            r = m - 1
        else:
            l = m + 1

    return result + 1

