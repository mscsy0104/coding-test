'''
https://codeup.kr/problem.php?id=6130
6130 : 일차 방정식 ax±b=0의 해 구하기

input
5x+4

output
-0.80
'''

exp = input()
x_loc = exp.find('x')

a = int(exp[:x_loc])
oper = exp[x_loc+1]
b = int(exp[x_loc + 2:])

if oper == '+':
    result = -b/a
elif oper == '-':
    result = b/a

print(format(result, ".2f"))