a = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
b = '''"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
'''
c = '''"재귀함수가 뭔가요?"
"재귀함수는 자기 자신을 호출하는 함수라네"
라고 답변하였지.
'''
d = '라고 답변하였지.'
line = '____'

def print_lines(start, text):
    for i, v in enumerate(text.splitlines()):
        print(line * start + v)

def recursion(start, n, text):
    if start < n:
        print_lines(start,text)
        start += 1
        recursion(start, n, text)
    else:
        pass

def recursion_re(n, text):
    if n >= 0:
        print_lines(n,text)

        recursion_re(n-1, text)
    else:
        pass


n = int(input())
start = 0

print(a)
recursion(start, n, b)
print_lines(n, c)
recursion_re(n-1, d)