class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        prevUpper = 0
        amtProcessed = 0

        for upper, percentage in brackets:
            if amtProcessed >= income:
                break
            amt = min(upper, income) - prevUpper
            tax = (amt * percentage) / 100
            
            res += tax
            amtProcessed += amt
            prevUpper = upper

        return res