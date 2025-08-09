class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        netWorth = -prices[0]
        profit = 0

        for i in range(1, len(prices)):
            netWorth = max(netWorth, profit - prices[i])
            profit = max(profit, netWorth + prices[i] - fee)

        return profit