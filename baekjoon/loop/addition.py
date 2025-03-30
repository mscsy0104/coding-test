# 제한 없을 때
# for line in sys.stdin 방식은 EOF를 키보드 입력으로 처리해주는데, 코딩 테스트 플랫폼에서는 보통 OK된다.
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)


# 제한 있을 때
# sol1. 
while True:
    a, b = map(int, input.split())
    if a == 0 and b == 0:
        break

    print(a + b)

# sol2.
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    if a + b == 0:
        print(a + b)