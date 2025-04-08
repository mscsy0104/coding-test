'''
https://www.acmicpc.net/problem/10101
삼각형 외우기 

input
60
70
50

output
Scalene
'''


arr = list([int(input()) for _ in range(3)])

sum_val = sum(arr)

if arr[0] == 60 and arr[1] == 60 and arr[2] == 60:
    print('Equilateral')
elif sum_val == 180:
    arr.sort()
    if arr[0] == arr[1] or arr[1] == arr[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')


# sol2. scvhero 님 풀이
# 코드 골프: 가능한 짧게
print(['Error', 'Equilateral', 'Isosceles', 'Scalene'][(sum(l:=[*map(int, open(0))]) == 180) * len({*l})])


# sol3. GPT 추천
arr = [int(input()) for _ in range(3)]

if sum(arr) != 180:
    print("Error")
elif arr[0] == arr[1] == arr[2]:
    print("Equilateral")
elif len(set(arr)) == 2:
    print("Isosceles")
else:
    print("Scalene")


'''
sol2는 코드 골프로 가장 짧은 코딩방식
해석하면서 근사하다고 느꼈다.
실무에서 쓰긴 어렵고(유지보수성, 코드 가독성) 
대회나 게임 풀이 개념으로 쓸 때 좋다고 한다.

sol3는 유지보수성, 코드 가독성, 성능 효율적으로 무난함.
'''