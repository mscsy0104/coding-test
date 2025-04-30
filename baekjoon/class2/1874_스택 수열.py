'''
https://www.acmicpc.net/problem/1874

9:53 ~ 10:34(X, 해설)

input
8
4
3
6
8
7
5
2
1

output
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

intput2
5
1
2
5
3
4

output
NO
'''

import sys
from collections import deque

input = sys.stdin.readline

current = 1
possible = True
stack = deque()
result = []

n = int(input())

for _ in range(n):
    num = int(input())

    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1

    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break

print("\n".join(result) if possible else "NO")


'''
# 토막 상식
# for-loop print하고 싶으면 join을 이용하기
# 의미
if not possible:
    print("NO")
else:
    for i in result:
        print(i)

# O
print("\n".join(result) if possible else "NO")

# X
# print(i for i in result if possible else "NO")
'''