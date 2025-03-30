'''
    *
   **
  ***
 ****
*****
'''

# sol1. 띄어쓰기를 중심으로
n = int(input())

for i in range(n - 1, -1, -1):
    print(' ' * i + '*' * (n - i))

# sol2. 별을 중심으로
n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)


# 개인적으로는 먼저 나오는 것을 중심으로(sol1처럼) 해주는 게 좋은 것 같음.