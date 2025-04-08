'''
https://www.acmicpc.net/problem/1978
소수 찾기

input
4
1 3 5 7

output
3
'''

n = input()
nums = list(map(int, input().split()))

cnt = 0
for i in nums:
    breaker = False
    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0:
            breaker = True
            break

    if breaker:
        continue

    cnt += 1


print(cnt)

# # sol2. 백준 euno657님의 풀이
'''
수학 개념을 이용해서 근사하다.
n이 소수인지 판별할 때는 √n보다 작은 범위에 대해서만 확인해도 충분하다.
이유
n이 소수가 아닌 경우
1, 본인 제외 약수 존재: a * b = n
둘다 √n보다 크다면: a * b > n 이므로 n의 약수되는 것은 불가능 
약수배수 관계이면 a, b 적어도 하나는 √n 이하이다.
예시
12 = 3 * 4
25 = 5 * 5 -> √25까지만 봐도 됨. 소수가 아니라면 그 전에 판명남.
18 = 2 * 9 -> √18이면 4보다 크기 때문에 2는 그보다 작다. 결국 소수가 아님이 확인된다.
'''
input()
arr = list(map(int, input().split()))

for i in arr:
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            arr.remove(i)
            break

if 1 in arr:
    print(len(arr) - 1)
else:
    print(len(arr))    