'''
https://school.programmers.co.kr/learn/courses/30/lessons/1845

input: [3,1,2,3]
output: 2
'''

from collections import Counter

def solution(nums):
    answer = 0
    hashmap = Counter(nums)

    half_len_nums = len(nums) // 2
    len_keys = len(hashmap.keys())
    
    if half_len_nums >= len_keys:
        answer = len_keys
    else:
        answer = half_len_nums
    return answer