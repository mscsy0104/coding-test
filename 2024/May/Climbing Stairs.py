
def dp_tab(n: int):
    d = [0 for _ in range(n+1)]
    if n==1: return 1
    elif n==2: return 2

    d[1] = 1
    d[2] = 2
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]

def dp_memo(n: int):
    d = dict()
    if n < 3:
        return n
    if n not in d.keys():
        d[n] = dp_memo(n-1) + dp_memo(n-2)
    return d[n]


# print(dp_tab(38))
# print(dp_memo(38))

'''
dp_tab은 바로 되는데
dp_memo는 시간이 더 오래 걸린다. (TimelimitExceeded)
같은 시간복잡도(O(n))여도 재귀로 인한 중복호출로 시간이 더 오래 걸리는 것을 확인할 수 있다.
'''

'''
d[1]
1 => 1
d[2]
1+1 2 => 2
d[3]
2+1 / 1+1+1 1+2 => d[1] + d[2] = 3 
d[4]
2+1+1, 2+2 / 1 + ((2+1), (1+1+1), (1+2))  => d[2] + d[3] => 5

...
d[n] = d[n-1] + d[n-2] 
'''