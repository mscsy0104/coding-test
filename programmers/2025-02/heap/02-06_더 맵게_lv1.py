'''
12:40 ~ 2:40
https://school.programmers.co.kr/learn/courses/30/lessons/42626

input:
scoville = [1, 2, 3, 9, 10, 12]
K = 7

output: 2
'''

from heapq import heappush, heappop, heapify

def cal_mixed_scoville(scoville):
    min = heappop(scoville)
    min2 = heappop(scoville)
    return min + min2 * 2


def solution(scoville, K):
    answer = 0 # count
    heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        mixed_scoville = cal_mixed_scoville(scoville)
        answer += 1
        heappush(scoville, mixed_scoville)
        
    if scoville[0] >= K:
        return answer
    return -1