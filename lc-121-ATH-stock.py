class Solution:
    def maxProfit(self, prices) -> int:


        
        buy = prices[0]
        sell = 0
        profit = 0
        for xind, x in enumerate(prices[:-1]):
            
            if x <= buy:
                buy = x
                sell = (max(prices[xind+1:]) - buy)
                print(buy, x, profit, sell)

                if  profit < sell:
                    profit= sell
        return ((profit))



















test=Solution()


test.maxProfit([7,1,5,3,6,4])