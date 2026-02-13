from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1): # k + 1 since start doesn't count as a stop
            tempPrices = prices.copy()

            for source, destination, price in flights:
                if prices[source] == float("inf"):
                    continue
                curCost = prices[source] + price
                if curCost < tempPrices[destination]:
                    tempPrices[destination] = curCost

            prices = tempPrices

        return prices[dst] if prices[dst] != float("inf") else -1

