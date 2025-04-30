'''
https://www.acmicpc.net/problem/4949
균형잡힌 세상

13:20 ~ X

input
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.

output
yes
yes
no
no
no
yes
yes
'''
from collections import deque


def ballance(line):
    stack = deque()

    for i in line:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    
    return not stack
        

for i in open(0):
    line = i.rstrip()

    if line == ".":
        break

    print("yes" if ballance(line) else "no")



# 입력 처리
# sol1.
lines = open(0).read().splitlines()

for line in lines:
    if line == ".":
        break

# sol2.
for i in open(0):
    line = i.rstrip() # 문제 특징 참고해서 strip 말고 rstrip 쓴 것임.

