class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        m = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in m.values():
                stack.append(c)
            elif c in m.keys():
                if not stack or m[c] != stack.pop():
                    return False

        return not stack          
            
