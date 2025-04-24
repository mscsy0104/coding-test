'''
https://www.acmicpc.net/problem/1676
13:56 ~ 14:10

input 
10

output
2
'''

# sol1. 직관적인 방법
import sys

n = int(sys.stdin.readline())

def factorial():
    f_num = 1
    for i in range(1, n + 1):
        f_num *= i
    
    return f_num

f_num = factorial()
cnt = 0

for i in str(f_num)[::-1]:
    if i == '0':
        cnt += 1
        continue
    else:
        print(cnt)
        break

    

# sol2. 백준 zzae_yon 님 풀이 - 공식을 이용한 방법
'''
팩토리얼 끝에 붙는 0의 개수 = N! 안에 포함된 5의 개수
따라서
n // 5 + n // 25 + n // 125 + ...
= sigma(k, (n // 5**k)

N = 100
5를 나누는 이유
5의 배수를 확인하기 위해

5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100(20개)
(5가 1번 들어간 경우 체크)


25 나누는 이유
25, 50, 75, 100
(5가 2번 들어간 경우 1번 더 체크)


125 나누는 이유
100//125 = 0(커서 더 없음)
'''
# 0 <= n <= 500이므로 125까지만 나눠주면 되지요.
n = int(open(0).read())
print(n//5 + n//25 + n // 125)