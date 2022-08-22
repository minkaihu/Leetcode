class Solution:
    def maxProfit(self, prices) -> int:

        if len(prices) == 0:
            return 0
        max_sell = prices[-1]
        profit = 0

        for x in prices[::-1]:
            print(x)
            if max_sell - x > profit:
                profit = max_sell - x
            if x > max_sell:
                max_sell = x


        return ((profit))



















test=Solution()


test.maxProfit([7,1,5,3,6,4])