'''
https://www.acmicpc.net/problem/4153
직각삼각형

13:38 ~ 13:58

input
6 8 10
25 52 60
5 12 13
0 0 0

output
right
wrong
right
'''

# sol1. max, remove 사용
lines = open(0).readlines()

for line in lines:
    nums = list(map(int, line.split()))

    if sum(nums) == 0:
        break

    max_val = max(nums)
    nums.remove(max_val)

    if max_val ** 2 == sum(map(lambda x: x**2, nums)):
        print('right')
    else:
        print('wrong')


# sol2. 정렬 사용
lines = open(0).readlines()

for line in lines:
    nums = list(map(int, line.split()))

    if sum(nums) == 0:
        break

    nums.sort()

    if nums[-1] ** 2 == nums[0] ** 2 + nums[1] ** 2:
        print('right')
    else:
        print('wrong')

# sol3. 정렬(sorted) 사용 및 언패킹 + pythonic
lines = open(0).readlines()
for line in lines:
    a, b, c = sorted(map(int, line.split()))
    if a + b + c == 0:
        break
    print("right" if c**2 == a**2 + b**2 else "wrong")


'''
|sol1|sol2|sol3|
|----|----|----|
|max로 필요한 값 짚어내는 건 좋음|sort는 3개 원소까진 최적화돼있음|가독성 + 성능 우수|
|remove|sort는 큰수로 넘어가면 X||

결론: sol3 추천
'''