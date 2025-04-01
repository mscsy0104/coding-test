'''
https://www.acmicpc.net/problem/1157
단어 공부

input
Mississipi

output
?

input 
z

output
Z
'''


# sol1. collections.Counter 메소드 most_common() 이용 - 배열(컨테이너 역할) 제일 앞과 비교
from collections import Counter

word = input().upper()
most_common = Counter(word).most_common()

if len(most_common) > 1:
    if most_common[0][1] == most_common[1][1]:
        print('?')
    else:
        print(most_common[0][0])
elif len(most_common) == 1:
    print(most_common[0][0])


# sol2. collections.Counter dictionary의 메소드 values(), items() 이용 - 배열(컨테이너 역할) 요소 출력
from collections import Counter

word = input().upper()
counter = Counter(word)

max_freq = max(counter.values())
most_common = [char for char, cnt in counter.items() if cnt == max_freq]

if len(most_common) == 1:
    print(most_common[0])
else:
    print('?')


# sol3. 배열(인덱스 체크 역할) 이용
word = input().upper()
freq = [0] * 26

for char in word:
    freq[ord(char) - ord('A')] += 1

max_freq = max(freq)
if freq.count(max_freq) > 1:
    print('?')
else:
    print(chr(freq.index(max_freq) + ord('A')))