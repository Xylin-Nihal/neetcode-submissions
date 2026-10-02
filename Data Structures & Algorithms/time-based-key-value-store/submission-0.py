from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.h = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.h[key]

        l = 0
        r = len(arr) - 1
        ans = ""

        while l <= r:
            m = (l + r) // 2

            if arr[m][1] <= timestamp:
                ans = arr[m][0]
                l = m + 1
            else:
                r = m - 1

        return ans