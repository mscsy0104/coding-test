'''
https://www.acmicpc.net/problem/11005
진법 변환 2

13:48 ~ 13:55

input
60466175 36

output
ZZZZZ
'''
# sol1. 
from string import ascii_uppercase

n, b = map(int, input().split())

uppers = list(ascii_uppercase)
nums = list(range(10, 36))
CHR_TABLE = dict(zip(nums, uppers))

def jinbub(n, b):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, b)
        if mod >= 10:
            mod = CHR_TABLE[mod]
        rev_base += str(mod)

    return rev_base[::-1]

print(jinbub(n, b))