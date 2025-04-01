'''
https://www.acmicpc.net/problem/1316
그룹 단어 체커

13:45 ~ 13:53

input
3
happy
new
year

output
3
'''

# sol1. collections.Counter 이용
from collections import Counter

n = int(input())

total = 0
for _ in range(n):
    word = input()
    counter = Counter(word)

    no_group_cnt = 0
    for k, v in counter.items():
        if v >= 2 and k * v not in word:
            no_group_cnt += 1
            break

    if no_group_cnt:
        continue
    else:
        total += 1

print(total)


# sol2. sorted(word, key=word.find) 이용
n = int(input())
cnt = 0

for _ in range(n):
    word = input()

    if list(word) == sorted(word, key=word.find):
        cnt += 1

print(cnt)

# sol3. 2중 loop
n = int(input())

for _ in range(n):
    word = input()

    for i in range(n - 1):
        if word[i] == word[i + 1]:
            continue
        elif word[i] in word[i + 1:]:
            n -= 1
            break

print(n)