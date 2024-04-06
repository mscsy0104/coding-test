prices = [7,1,5,3,6,4]

# def return_(prices):
    # RuntimeError
    # li = []
    # for i in range(len(prices[:-1])):
    #     max_ = max(prices[i + 1:])
    #     li.append(max_ - prices[i])
    # max_ = max(li)
    # if max_ > 0:
    #     return max_
    # else:
    #     return 0

    # Time Limit Exceeded
    # if len(prices) == 1:
    #     return 0
    # elif len(prices) == 2:
    #     sub = prices[1] - prices[0]
    #     if sub > 0:
    #         return sub
    #     else:
    #         return 0
    # for i in range(len(prices[:-1])):
    #     max_ = max(prices[i + 1:])
    #     li.append(max_ - prices[i])
    # max_ = max(li)
    # if max_ > 0:
    #     return max_
    # else:
    #     return 0

    # 책 풀이-카데인 알고리즘
    # def maxProfit(self, prices:List[int]) -> int:
    #     profit = 0
    #     min_price = sys.maxsize
    #
    #     for price in prices:
    #         min_price = min(min_price, price)
    #         profit=max(profit, price - min_price)
    #     return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = max(prices)
        sub = 0
        li = []
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                pass
            sub = prices[i] - min
            li.append(sub)

        return max(li)