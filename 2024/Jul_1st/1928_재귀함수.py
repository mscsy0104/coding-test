n = int(input())

def solution(n):
    if n == 1:
        print(n)
    elif n > 1:
        if n % 2 == 1:
            print(n)
            n = 3*n + 1
            return solution(n)
        elif n % 2 == 0:
            print(n)
            n = int(n/2)
            return solution(n)
        else:
            return
    else:
        return

solution(n)
