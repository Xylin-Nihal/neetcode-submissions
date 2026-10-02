class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def back(s, open, close):

            if len(s) == 2 * n:
                res.append(s)
                return

            # Add '(' if we still have some left
            if open < n:
                back(s + "(", open + 1, close)

            # Add ')' only if there is an unmatched '('
            if close < open:
                back(s + ")", open, close + 1)

        back("", 0, 0)

        return res