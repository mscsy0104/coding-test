
def recursion(s, l, r):
    if l >= r:
        return 1, l+1
    else:
        if s[l] != s[r]:
            return 0, l+1
        else:
            return recursion(s, l+1, r-1)

def is_palindrome(s):
    return recursion(s, 0, len(s)-1)


def main():
    r, c = is_palindrome(s)
    print(r, c)



t = int(input())
for _ in range(t):
    s = input()
    main()
