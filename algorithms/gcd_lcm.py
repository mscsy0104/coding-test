'''
24 % 18 = 4 % 3 = 1
gcd(n, m) = gcd(m, n % m) = gcd(m, r)

n = gcd * q1, m = gcd * q2(q1, q2: 몫)
lcm = gcd * q1 * q2
lcm = n * m / gcd
'''

# recursive gcd
def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

# iterative gcd
def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

# lcm using gcd
def lcm(n, m):
    return n * m // gcd(n, m)