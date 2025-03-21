# https://softeer.ai/practice/7368
import sys

def get_taken_time(steps_to_touch, steps_to_reach, d):
    start_count = d // steps_to_touch
    start_remain_count = d % steps_to_touch
    if start_remain_count > 0:
        stop_count = start_count
    else:
        stop_count = start_count - 1
    
    return start_count * steps_to_touch + start_remain_count + stop_count * steps_to_reach

def solve():
    a, b, d = map(int, sys.stdin.readline().split())
    first_time = get_taken_time(a,b,d)
    second_time = get_taken_time(b,a,d)
    total_time = first_time + second_time
    sys.stdout.write(str(total_time))

if __name__ == "__main__":
    solve()