'''
https://codeup.kr/problem.php?id=2653
2653 : 규칙에 맞는 이진수 만들기 (Small)

15:30 ~ X(해설)

input 
3

output
5
'''

n = int(input())
# 이진수, 연속 x(순서문제)
dp = [[0, 0] for _ in range(n + 1)]
dp[1][0] = 1 # '0' 1개
dp[1][1] = 1 # '1' 1개

def count_binary(n):
    for i in range(2, n + 1): # 초깃값 있기 때문.
        dp[i][0] = dp[i - 1][1]
        dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

    return dp[n][0] + dp[n][1]

print(count_binary(n))





