class Solution:
    def minWindow(self, s: str, t: str) -> str:

        h = {}
        x = {}

        for char in t:
            h[char] = h.get(char, 0) + 1

        l = 0
        match = 0
        required = len(h)

        res = ""
        min_len = float("inf")

        for r in range(len(s)):

            x[s[r]] = x.get(s[r], 0) + 1

            # Character requirement satisfied
            if s[r] in h and x[s[r]] == h[s[r]]:
                match += 1

            # Window is valid
            while match == required:

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]

                # Remove left character
                x[s[l]] -= 1

                if s[l] in h and x[s[l]] < h[s[l]]:
                    match -= 1

                l += 1

        return res