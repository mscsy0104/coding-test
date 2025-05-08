'''
13:07 ~ 13:12
13:37 ~ 

1 <= n <= 500000
'''

# 시간초과
n = int(input())

result = ''

for _ in range(n):
    s, t = input().split()
    if 'x' in s:
        p = s.index('x')
    elif 'X' in s:
        p = s.index('X')

    result += t[p]

print(result.upper())


# sol. immutable은 join이 빠르다!
'''
result 문자열일 경우, 
result += ... n번 반복 시, O(n^2) 됨.
이유: 매번 새로운 문자열을 복사해서 붙이는 작업 발생

해결: 문자열은 immutable이라 리스트 누적 후 join 출력이 가장 빠르다.
'''
result = []

for _ in range(n):
    s, t = input().split()
    s = s.lower()
    p = s.index('x')
    result.append(t[p])

print(''.join(result).upper())
