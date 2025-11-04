class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def f(opened,closed,s):
            if opened == closed and opened + closed == n *2:
                res.append(s)
                return
            if opened < n:
                f(opened+1,closed,s + "(")
            if closed < opened:
                f(opened,closed+1,s + ")")
        f(0,0,"")
        return res
        
