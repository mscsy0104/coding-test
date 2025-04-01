# '''
# https://www.acmicpc.net/problem/2720
# 세탁소 사장 동혁

# 13:59 ~ 14:17

# input
# 3
# 124
# 25
# 194

# output
# 4 2 0 4
# 1 0 0 0
# 7 1 1 4
# '''


# COIN_TABLE = {
#     'q': 0.25, 'd': 0.10, 'n': 0.05, 'p': 0.01
# }

# t = int(input())
# for _ in range(t):
#     c = int(input()) 
#     q_li = []

#     for k, v in COIN_TABLE.items():
#         q, mod = divmod(c, v*100)
#         q_li.append(int(q))
#         c = mod

#     print(*q_li)

# # sol2. 
# n = int(input())

# for _ in range(n):
#     num = int(input())
#     for i in [25, 10, 5, 1]:
#         print(num // i, end= ' ' )
#         n %= i


# # sol3. egwkim님 풀이 - 간결한데에다 다양한 걸 배울 수 있었음.(open(0), 비트연산 5&1)
# for i in [*open(0)[1:]]:
#     i = int(i)
#     print(i//25, i%25//10, i%25//5&1, i%5)

n = int(input())

for _ in range(n):
    num = int(input())
    for i in [25, 10, 5, 1]:
        print(num // i, end= ' ' )
        num = num % i
