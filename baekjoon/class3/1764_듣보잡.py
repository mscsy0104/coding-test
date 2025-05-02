'''
https://www.acmicpc.net/problem/1764
듣보잡

14:09 ~ 14:45

input
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

output
2
baesangwook
ohhenrie
'''
lines = open(0).read().splitlines()

n, _ = map(int, lines[0].split())
common = set(lines[1:n+1]) & set(lines[n+1:])

print(len(common))
print('\n'.join(sorted(list(common))))