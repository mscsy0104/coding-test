# 입력
## input(built-in function)
```python
s = input() # 스트링
n = int(input()) # 정수
a, b = input().split() # 스트링, 언패킹
a, b = map(int, input().split()) # 정수, 언패킹
```

### 한 줄 입력
```python
arr = sys.stdin.readline().split()
n_arr = list(map(int, sys.stdin.readline().split()))
```

### 여러 줄 입력
```python
t = 5
arr = [input() for _ in range(t)] # 배열 - 스트링 요소
n_arr = [int(input()) for _ in range(t)] # 배열 - 정수 요소
```

## sys(built-in module)
```python
import sys

s = sys.stdin.readline() # 스트링 
n = int(sys.stdin.readline()) # 정수
a, b = sys.stdin.readline().split() # 스트링, 언패킹
a, b = map(int, sys.stdin.readline().split()) # 정수, 언패킹
```

```python
### 한 줄 입력
arr = sys.stdin.readline().split()
n_arr = list(map(int, sys.stdin.readline()))
```


### 여러 줄 입력
```python
t = 5
arr = [sys.stdin.readline() for _ in range(5)]
n_arr = [int(sys.stdin.readlnie()) for _ in range(5)]
```

<br>

# 출력
## print(built-in function)
```python
print()
print(a, b, sep=', ')
print(a, b, end=' ')
```

## sys(built-in module)
```python
x = '문제의 답'
sys.stdout.write(str(x)) # 꼭 string 처리해줘야 함.
```

# 기타
### 2차원 배열
```python
arr_arr = [[] for _ in range(t)] # 배열 - 배열 요소
```

<br>

# 회사별 input, output 방식 차이
### 1. def solve - return / print answer(자동입력 O)
- 입력 처리 불필요.
- return / print 

### 2. def solve - return / print answer(자동입력 X)
- 입력 처리 필요.
- return / print 

### 3. solution - print answer(함수 없어도 됨.)
- 입력 처리 필요.
- print


<br>

## 참고
> python에서 input(), print() 보다는 sys.stdin.readline(), sys.stdin.write(str()) 을 쓰면 코드 실행시간을 줄일 수 있다. 
하지만 일반적인 코드에서는 input()과 print()가 가독성이 좋으므로 무조건 바꿀 필요는 없다.<br><br><b>1. sys.stdin.readline() vs. input()</b><br>
input()은 내부적으로 버퍼링 + 개행 문자 제거 과정이 포함되어 있어서 느림.
반면, sys.stdin.readline()은 버퍼에서 한 줄을 통째로 읽어오는 방식이라서 더 빠름.
특히 반복문에서 여러 줄을 입력받을 때 차이가 커짐.<br><br><b>2. sys.stdout.write() vs. print()</b><br>
print()는 기본적으로 출력 후 개행(\n)을 자동 추가하고, 내부적으로 버퍼를 관리해서 상대적으로 느림.
반면, sys.stdout.write(str())는 버퍼링을 최소화하고 개행을 자동으로 추가하지 않음, 그래서 더 빠름.
다만, 개행을 원하면 \n을 직접 추가해야 함.