n = int(input())

def solution(n):
    if n>0:
        print(n)
        n = n-1
        return solution(n)
    else:
        return

solution(n))


