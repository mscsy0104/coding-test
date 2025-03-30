'''
https://www.acmicpc.net/problem/1316
그룹 단어 체커

19:19 ~ X

input
3
happy
new
year

output
3
'''

# n = int(input())
# words = [input() for _ in range(n)]

word = 'abcabc'

from collections import Counter

counter = Counter(word)

print(counter)

for i in counter.keys():
    print(i)
    print(word.find(i))
    print('-')