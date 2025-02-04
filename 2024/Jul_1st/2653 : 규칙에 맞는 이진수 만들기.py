# from itertools import product as prod
# n = int(input())
#
# def solution(n):
#     prod_li = list(prod('01', repeat=n))
#
#     li_ = [''.join(bits) for bits in prod_li]
#     print(li_)
#     result_li = []
#     for i in li_:
#         if '00' in i:
#             pass
#         else:
#             result_li.append(i)
#
#     return len(result_li)
#
# print(solution(n))
length = int(input())
def solution(length):
    bits = [format(i, f'0{length}b') for i in range(2**length)]

    result_li = []
    for i in bits:
        if '00' in i:
            pass
        else:
            result_li.append(i)

    return len(result_li)

print(solution(length))

