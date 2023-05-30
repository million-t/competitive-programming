class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort(reverse = True)
        queue = deque([deck[0]])
        
        for ind in range(1, len(deck)):
            queue.appendleft(queue.pop())
            queue.appendleft(deck[ind])
        
        return list(queue)