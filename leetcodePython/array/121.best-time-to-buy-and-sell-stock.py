class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)-1):
            maxIndex = prices.index(max(prices[i+1:]))
            if prices[i] < prices[maxIndex] and prices[maxIndex]-prices[i] > maxP:
                maxP = prices[maxIndex] - prices[i]

        return maxP
