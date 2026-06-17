class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        h = {}

        for num in hand:
            h[num] = h.get(num, 0) + 1

        while h:
            x = min(h)

            for i in range(groupSize):
                curr = x + i

                if curr not in h:
                    return False

                h[curr] -= 1

                if h[curr] == 0:
                    del h[curr]

        return True