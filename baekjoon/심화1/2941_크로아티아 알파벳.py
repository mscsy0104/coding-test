'''
https://www.acmicpc.net/problem/2941
크로아티아 알파벳

16:48 ~ 17:05

input
ljes=njak

output
6

input
nljj

output
3

input
c=c=

output
2
'''

# 크로아티아 알파벳 담은 배열이 중요
# sol1. 조금 복잡할수도? 
# word = input()
# cnt = 0
# for i in ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
#     if i in word:
#         cnt += word.count(i)
#         word = word.replace(i, '-')

# cnt += len(word)
# cnt -= word.count('-')
# print(cnt)


# sol2. 
word = input()
for i in ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
    word = word.replace(i, '*')

print(len(word))