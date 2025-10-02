class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numEmpty = numBottles

        while numEmpty >= numExchange:
            newBottles = numEmpty // numExchange
            res += newBottles
            numEmpty = numEmpty % numExchange + newBottles

        return res