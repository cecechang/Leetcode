class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        final = 0
        final += numBottles
        while numBottles >= numExchange:
            final += numBottles//numExchange
            numBottles = numBottles//numExchange + numBottles%numExchange

        return final
        