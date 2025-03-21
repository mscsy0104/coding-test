'''
https://codeup.kr/problem.php?id=1451
1451 : 데이터 정렬 (small)

17:16 ~ 17:19

input
5
7
3
10
2
1

output
1
2
3
7
10
'''

n = int(input())
arr = [int(input()) for _ in range(n)]
sorted_arr = sorted(arr)

for i in sorted_arr:
    print(i)