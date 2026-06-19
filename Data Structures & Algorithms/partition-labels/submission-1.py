class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        active = set()
        size = 0
        result = []

        for ch in s:
            freq[ch] -= 1
            active.add(ch)
            size += 1

            if freq[ch] == 0:
                active.remove(ch)

            if not active:
                result.append(size)
                size = 0

        return result