'''
It took a long time to solve this problem...
https://school.programmers.co.kr/learn/courses/30/lessons/86491
input:
sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

output: 120
'''

def solution(sizes):
    answer = 0
    
    widths, heights = zip(*sizes)
    max_w = max(widths)
    max_h = max(heights)
    
    if max_w >= max_h: # 기준: w
        for idx, size in enumerate(sizes):
            if size[0] < size[1]:   
                sizes[idx] = sizes[idx][::-1]
            
        _, heights = zip(*sizes)
        max_h = max(heights)
    else: # 기준: h
        for idx, size in enumerate(sizes):
            if size[0] >= size[1]:
                sizes[idx] = sizes[idx][::-1]
        
        widths, _ = zip(*sizes)
        max_w = max(widths)
        
    answer = max_w * max_h
    
    return answer