'''
https://codeup.kr/problem.php?id=1425
1425 : 자리 배치


input
9 6
160 165 164 165 150 165 168 145 170 

output
145 150 160 164 165 165 
165 168 170 

---
input
11 3
144 160 148 153 165 161 155 155 166 155 155 

output
144 148 153
155 155 155
155 160 161
165 166
'''

n, c = map(int, input().split())
heights = list(map(int, input().split()))
sorted_heights = sorted(heights)

lines = []
for idx, val in enumerate(sorted_heights):
    if (idx+1)%c == 0:
        lines.append(idx)

while lines:
    for idx, val in enumerate(sorted_heights):
        if lines:
            if idx == lines[0]:
                print(val, end='\n')
                lines.pop(0)
            else:
                print(val, end=' ')
        else:
            print(val, end=' ')