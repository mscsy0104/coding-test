'''
https://www.acmicpc.net/problem/1259
11:36 ~ 11:59

input
121
1231
12421
0

output
yes
no
yes
'''

# sol1. for문 이용해서 필요한 위치까지만 비교(조기종료)
import sys

input = sys.stdin.readline

def palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word) - i - 1]:
            return False
        else:
            continue
    
    return True


while True:
    t = input()

    if t == '0': break

    if palindrome(t):
        print('yes')
    else:
        print('no')

# sol2. 슬라이싱 이용해서 간단히 비교
while True:
    word = input()
    if word == '0': 
        break

    print("yes" if word == word[::-1] else 'no')


'''
|sol1 v.s. sol2|
|-------|-------|
|속도|느림|빠름(이유: python 슬라이싱 및 문자열 비교가 C로 최적화 돼 있음.)|
|메모리 효율|적게 씀|많이 씀(복사)|
|조기종료 가능성|있음|없음|

메모리 민감하면 for로 특정 위치까지만 비교
일반적인 경우 -> 슬라이싱 쓰자.
'''