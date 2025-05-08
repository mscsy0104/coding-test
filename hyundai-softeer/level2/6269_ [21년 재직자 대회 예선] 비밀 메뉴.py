'''
https://softeer.ai/practice/6269
[21년 재직자 대회 예선] 비밀 메뉴

1:16 ~ 1:24

input
3 10 5
1 4 5
3 3 1 2 4 1 4 5 1 4

output
secret
'''
import sys

input = sys.stdin.readline

input()
m_nums = input().split()
n_nums = input().split()

m_str = ''.join(m_nums)
n_str = ''.join(n_nums)

if m_str in n_str:
    print('secret')
else:
    print('normal')