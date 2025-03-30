'''
https://codeup.kr/problem.php?id=3506
3506 : 블럭 채우기 1 (Small)

14:30 ~ x(해설)

input
3

output
3
'''

'''
fn = fn-1 + fn-2
fn : 2*n 크기 채우는 방법 수
fn-1 : 세로로 타일 1개
fn-2 : 가로로 타일 2개
f1 = 1
f2 = 2
'''


def tile_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = int(input())
print(tile_ways(n))