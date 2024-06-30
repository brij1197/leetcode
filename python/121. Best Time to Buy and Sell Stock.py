class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,max_profit=0,0
        
        for right in range(1,len(prices)):
            profit=prices[right]-prices[left]
            if profit>=0:
                max_profit=max(max_profit,profit)
            else:
                left=right
        return max_profit