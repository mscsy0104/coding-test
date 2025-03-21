'''
https://codeup.kr/problem.php?id=3011
3011 : 거품 정렬(Bubble Sort)

17:20 ~ 18:01(해설)

input
5
10 50 30 20 40

output
2
'''

import sys

def bubble_sort_count(arr):
    n = len(arr)
    count = -1

    for i in range(n):
        swapped = False
        count += 1
        
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]    
                swapped = True

        if not swapped:
            return count

    return count


# n = int(input())
# arr = list(map(int, input().split()))
# print(bubble_sort_count(arr))
 
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(bubble_sort_count(arr))

