
def dp(n: int):
    d = [0 for i in range(n+2)]
    d[1] = 1
    d[2] = 2

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]

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