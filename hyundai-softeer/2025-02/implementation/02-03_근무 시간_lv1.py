#  https://softeer.ai/practice/6254
import sys

def calculate_total_working_time(data: list):
    sch = 0
    for i in data:
        s, l = i.split()
        lh, lm = map(int, l.split(':'))
        sh, sm = map(int, s.split(':'))
        
        h = lh - sh
        m = lm - sm
        if lm - sm < 0:
            m += 60
            h -= 1 
        m += h * 60
        sch += m
    return sch

def solve():
    times = [sys.stdin.readline() for _ in range(5)]
    sch = calculate_total_working_time(times)
    sys.stdout.write(str(sch))

if __name__ == "__main__":
    solve()