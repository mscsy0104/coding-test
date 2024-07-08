a, b = map(int, input().split())

def compare(a,b):
    if a >= b:
        return a, b
    else:
        return b, a

def gcf(big, small):
    big, small = compare(big, small)

    q = big // small
    r = big % small

    if big % small != 0:
        return gcf(small, r)
    else:
        return small


print(gcf(a, b))