"""
- Create a hashmap with the hand card counts
- Pick the lowest start num possible, build up a straight hand with that hand,
  decrementing the card count for that card value in the hashmap
- If you use up all the cards without hitting a bad path (meaning, you're trying to use
  a card count that is 0) -> that means success
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        cardCounts = defaultdict(int)
        for num in hand:
            cardCounts[num] += 1

        totalCardsUsed = 0
        
        for num in hand:
            if totalCardsUsed >= len(hand): break
            print(f'num: {num}')
            start = num
            while cardCounts[start - 1]:
                # while there exists a lower start number, that exists in `cardCounts`
                start -= 1
            if cardCounts[start] <= 0: continue
            print(f'start: {start}')
            for i in range(groupSize): 
                cardCounts[start + i] -= 1
                totalCardsUsed += 1
                if cardCounts[start + i] < 0:
                    print(start + i)
                    return False

        return True
