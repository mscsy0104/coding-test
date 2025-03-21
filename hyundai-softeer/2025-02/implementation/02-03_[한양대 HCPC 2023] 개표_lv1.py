# https://softeer.ai/practice/7698
import sys

def get_number_by_symbols(arr: list):
    five_symbol = '++++ '
    one_symbol = '|'
    five_count = 0
    result = []
    
    for i in arr:
        five_count = i // 5
        one_count = i % 5

        result.append(five_symbol * five_count + one_symbol * one_count + '\n')

    return result

def solve():
    t = int(input())
    arr = [int(sys.stdin.readline()) for _ in range(t)]
    result = get_number_by_symbols(arr)
    sys.stdout.write(''.join(result))

if __name__ == "__main__":
    solve()