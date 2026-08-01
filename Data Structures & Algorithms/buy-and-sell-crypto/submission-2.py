class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices, reverse=True) == prices:
            return 0
        else:
            low = float('inf')
            max_prof = 0
            for cur_price in prices:
                if cur_price < low:
                    low = cur_price
                cur_prof = cur_price - low
                if cur_prof > max_prof:
                    max_prof = cur_prof
            return max_prof
            
                

        