class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        h = {}

        for i in hand:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

        x = min(h)

        i = 0
        while i < len(hand):

            if i > 0 and i % groupSize == 0:
                x = min(h)

            curr = x + (i % groupSize)

            if curr not in h:
                return False

            h[curr] -= 1

            if h[curr] == 0:
                h.pop(curr)

            i += 1

        return True